 
### 1. `app.py` – Main Application Code
```python
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form["message"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        bot_reply = response.choices[0].message.content
        return render_template("index.html", user_message=user_message, bot_reply=bot_reply)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```
