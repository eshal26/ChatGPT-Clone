from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://eshal26:eshal123@chatgpt.mfxtdjf.mongodb.net/ChatGPT"
mongo = PyMongo(app)

@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template('index.html', myChats = myChats)

@app.route('/api', methods=['GET','POST'])
def qa():
    if request.method == 'POST':
        print(request.json)
        question = request.json.get('question')
        chat = mongo.db.chats.find_one({'question': question})
        print(chat)
        if chat:
            data = {'question':question,'answer': f"{chat.get('answer')}"}
            return jsonify(data)
        else:
            data = {'result': f"{question}"}
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
            mongo.db.chats.insert_one({'question': question, 'answer': response})


        data = {'result': f"{question}"}
        return jsonify(data)
    data = {'result': 'success'}
    return jsonify(data)

app.run(debug=True)