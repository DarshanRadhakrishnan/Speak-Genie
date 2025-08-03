import openai
def generate_roleplay_response(user_input, chat_history, scenario=" At the Store"):
    """
    user_input: latest input from child (str)
    chat_history: list of {"role": "user"/"assistant", "content": "..."} from previous turns
    scenario: selected roleplay theme
    """
    
    system_prompt = f"""
You are Genie, a kind and fun AI speaking partner for kids.
Your job is to help them practice conversations in a roleplay setting.
Be playful, supportive, and simple. Always speak in short, clear sentences.

🎭 Roleplay Scenario: {scenario}
Stay within the context of this roleplay. Respond as if you're part of this scenario.

Example:
Child: I want a banana.
Genie: Great choice! Bananas are yummy. Do you want one or two?

Keep it natural and engaging.
"""

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response['choices'][0]['message']['content'].strip()
