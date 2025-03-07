# 🛍️ Customer Support Chatbot

A **Customer Support Chatbot** built using **Flask** and **OpenAI** to enhance user experience and provide instant responses to common inquiries. This chatbot seamlessly integrates into e-commerce websites, offering automated assistance while allowing users to escalate to human support if needed.

## 🚀 Features

- **Interactive Chat Interface**: Engages users in real-time conversations.
- **Custom Prompts**: Handles specific customer queries (e.g., product details, order status, return policies).
- **OpenAI Integration**: Utilizes GPT-4 for intelligent and context-aware responses.
- **User Data Collection**: Captures user name and email for personalized support.
- **Fallback to Human Support**: Provides an option for users to connect with a human representative.
- **Easy Website Integration**: Displays as a floating chat bubble on the site.

---

## 📋 Requirements

Ensure you have the following dependencies installed:

- Python 3.8+
- Flask
- OpenAI API Key

Install required packages via:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Installation and Setup

1. **Clone the Repository**

```bash
git clone https://github.com/YourUsername/customer-support-bot.git
cd customer-support-bot
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Environment**

Set up your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

5. **Run the Application**

```bash
python app.py
```

Access the chatbot at: `http://localhost:5000`

---

## 📊 Project Structure

```
customer-support-bot/
├── app.py               # Main Flask Application
├── static/
│   └── style.css       # Chatbot Styling
├── templates/
│   └── index.html     # User Interface
├── requirements.txt   # Project Dependencies
└── README.md          # Project Documentation
```

---

## 💬 Usage Instructions

1. **User Flow**:
    - Users initiate the conversation via the chatbot bubble.
    - The chatbot greets the user and requests their **name** and **email**.
    - Provides predefined options:
      - Ask about specific products
      - Check order status
      - Inquire about return policies
      - Connect to human support

2. **Customization**:
   Modify the chatbot's behavior by updating the **system prompt** in `app.py`.

```python
{"role": "system", "content": "You are a helpful customer support assistant."}
```

---

## 🔗 Deployment

To deploy the chatbot on a production server:

1. Use **Gunicorn** for handling requests efficiently:

```bash
pip install gunicorn
```

2. Run with Gunicorn:

```bash
gunicorn app:app
```

3. Consider using **Docker** for containerized deployment.

---

## 📌 Future Improvements

- Multi-language support
- Session tracking for better personalization
- Webhook integration for live order updates

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to modify and use it in your projects.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to enhance this project, please open a pull request.

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a pull request.

---

## 📧 Contact

For inquiries or support, reach out via:

- GitHub: [Anass58](https://github.com/Anass58)
- Email: a55.44.as47@gmail.com

