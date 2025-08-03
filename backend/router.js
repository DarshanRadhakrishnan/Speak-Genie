const express = require('express');
const axios = require('axios');
const router = express.Router();

router.post('/ask', async (req, res) => {
    try {
        const { language, ageGroup } = req.body;
        const response = await axios.post('http://localhost:8000/ask', {
            language,
            age_group: ageGroup
        });
        res.json(response.data);
    } catch (err) {
        console.error("Error calling Python API:", err.message);
        res.status(500).json({ error: "Python service unavailable" });
    }
});

router.post('/ask_role',async(req,res)=>{
    try{
        const{language ,ageGroup,chatHistory,scenario}=req.body;
        const resp=await axios.post("http://localhost:8000/ask" ,{
            language,
            ageGroup,
            chatHistory,
            scenario
        });
        res.json(resp.data);
    }catch(err){
        console.error("Error calling teh python api",err.message);
        res.status(500).json({ error: "Python service unavailable" })
    }
})

module.exports = router;
