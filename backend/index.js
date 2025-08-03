const express=require('express')
const router=require('./router')
const app=express()
app.use(express.json)
PORT=5000
app.use('./api/ask',router)
app.listen(PORT,()=>{
    console.log(`server is listenin to the port : ${PORT}`)
})