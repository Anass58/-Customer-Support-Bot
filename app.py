from flask import Flask, render_template, request, jsonify
import openai

# إعداد التطبيق
app = Flask(__name__)

# إدخال مفتاح API الخاص بـ OpenAI
openai.api_key = 'YOUR_API_KEY'

# قوالب الأوامر لتحسين المحادثة
PROMPTS = {
    "product_info": "Provide detailed information about a product.",
    "order_status": "Check the status of a customer's order.",
    "return_policy": "Explain the store's return policy.",
    "human_support": "Connect the user to a human support agent."
}

# دالة لمعالجة الطلبات عبر ChatGPT
def ask_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = ask_gpt(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
