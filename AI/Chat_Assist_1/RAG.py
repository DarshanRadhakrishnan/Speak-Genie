from langchain.prompts import ChatPromptTemplate

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = ""#since the open api key is not free i just left it for fre here

# Multi Query: Different Perspectives
template = """You are a helpful and friendly AI assistant designed to support a child’s learning. 
Your task is to generate five different simple and creative versions of the child’s 
spoken question to help retrieve the most relevant answers from a vector database. 

Make sure the variations are age-appropriate, easy to understand, and reflect how 
kids might naturally ask or rephrase things. These alternate questions will improve 
document retrieval by overcoming limitations of single-query similarity search.

Provide each alternate question on a new line.

Original question: {question}"""
prompt_perspectives = ChatPromptTemplate.from_template(template)
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

generate_queries = (
    prompt_perspectives 
    | ChatOpenAI(temperature=0) 
    | StrOutputParser() 
    | (lambda x: x.split("\n"))
)

generate_queries.invoke("What is a noun")

#Now we need to index the docs effectively and store them up in storage space and for that we are gonna use Multi-Representation-Indexing

from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    UnstructuredPowerPointLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 🌐 Load blog posts (Web)
web_loader_1 = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
web_loader_2 = WebBaseLoader("https://lilianweng.github.io/posts/2024-02-05-human-data-quality/")
docs = web_loader_1.load()
docs.extend(web_loader_2.load())
# 2. 📄 Load PDFs
pdf_loader = PyPDFLoader("data/sample_ebook.pdf")  # local PDF path
docs.extend(pdf_loader.load())
# 3. 📊 Load PowerPoint presentations
ppt_loader = UnstructuredPowerPointLoader("data/sample_ppt.pptx")  # local PPT path
docs.extend(ppt_loader.load())
# 4. 📝 Load local blog-style text or markdown files
text_loader = TextLoader("data/blog_1.txt")  # plain text file
md_loader = UnstructuredMarkdownLoader("data/blog_2.md")  # markdown file
docs.extend(text_loader.load())
docs.extend(md_loader.load())
# ✅ Ready for embedding into your vector store (Chroma, FAISS, etc.)
print(f"Total chunks: {len(docs)}")
print(docs[0].page_content[:300])  # Preview first chunk



#No we have constructed the chain for creating the summaries 
import uuid
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
chain = (
    {"doc": lambda x: x.page_content}
    | ChatPromptTemplate.from_template("Summarize the following document:\n\n{doc}")
    | ChatOpenAI(model="gpt-3.5-turbo",max_retries=0)
    | StrOutputParser()
)
summaries = chain.batch(docs, {"max_concurrency": 5})
 


#Now we create the storage space for all these things 
from langchain.storage import InMemoryByteStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.retrievers.multi_vector import MultiVectorRetriever
# The vectorstore to use to index the child chunks initialisg a vectorspace to store the summary embeddings
vectorstore = Chroma(collection_name="summaries",
                     embedding_function=OpenAIEmbeddings())
# The storage layer for the parent documents we store the actual emebedding sof the parent document in the memoryBYstore
store = InMemoryByteStore()
id_key = "doc_id"
# The retriever inbuilt which will find the summary and get the releveant original doc 
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    byte_store=store,
    id_key=id_key,
)
doc_ids = [str(uuid.uuid4()) for _ in docs]#create a list of unique id's 
summary_docs = [
    Document(page_content=s, metadata={id_key: doc_ids[i]})#here from the normal docs wth page content we are creating anew object metadata about the content with content and id as attributes
    for i, s in enumerate(summaries)
]
# Add the created spaces to the onejct created previously
retriever.vectorstore.add_documents(summary_docs)
retriever.docstore.mset(list(zip(doc_ids, docs)))

#Now we are set to create the main chain where we will use the muti queried question and multi represntation indexing

from langchain_core.runnables import RunnableLambda,RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI

#1 first we need to define a func to generate teh queries for the question 
def generate_multiple_queries(question:str):
    queries=generate_queries.invoke(question)
#2 we have to create a list of docs for each query
def retrieve_unique_docs(queries: list[str]):
    all_docs = []
    seen = set()
    for q in queries:
        docs = retriever.get_relevant_documents(q)
        for doc in docs:
            if doc.metadata[id_key] not in seen:
                all_docs.append(doc)
                seen.add(doc.metadata[id_key])
    return all_docs
#3 we need to generate a prompt to work on the collected docs and give us an effective answer
# 3. 🧩 Prompt template to answer based on retrieved docs
qa_prompt = ChatPromptTemplate.from_template("""
You are a friendly AI tutor talking to a child. Use the provided context to answer their question in a simple, encouraging way.
Speak like a caring teacher helping a young learner.

Question: {question}

Context:
{context}

Answer in 2–3 child-friendly sentences.
""")

#No we are ready to build the chain
# here in the chain the inout of each is obtained from the output of prev by using lambda and we should also constuct the present part's output so that it is compatible with teh next part's input
final_rag_chain=(
    RunnableLambda(lambda input:generate_multiple_queries(input["question"])) 
    | RunnableLambda(lambda list_of_queries:{"docs":retrieve_unique_docs(list_of_queries),"question":list_of_queries[0]})
    | RunnableLambda(lambda dict:{"question":dict["question"],
                               "context":"\n\n".join(doc.pagecontent for doc in dict["docs"])
                                  })
    | qa_prompt
    | OpenAI(model="gpt-3.5-turbo-instruct",temperature=0.5)
    | StrOutputParser
)

final_rag_chain.invoke({"question":"What is a Noun"})

