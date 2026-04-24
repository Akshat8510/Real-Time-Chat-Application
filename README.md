# Real-Time Chat Application with Llama 3.3 AI 💬🤖

A high-performance, real-time chat application built with **Django Channels** and integrated with **Groq's Llama 3.3 70B** model for instant AI responses.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-010101?style=for-the-badge&logo=socketdotio&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)

## 🚀 Features

- **Real-Time Messaging**: Instant communication using WebSockets (ASGI).
- **AI Integration**: Chat with **Llama 3.3** by starting your message with `/ai`.
- **Dynamic Rooms**: Create or join any chat room by simply entering a name.
- **Fast Inference**: Powered by **Groq**, providing AI responses in milliseconds.
- **Asynchronous Architecture**: Built on Django Channels for handling multiple concurrent connections.

## 🛠️ Tech Stack

- **Backend**: Django 5.x, Django Channels (ASGI).
- **AI Engine**: Groq Cloud SDK (Llama-3.3-70b-versatile).
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla).
- **Server**: Daphne (ASGI Server).
- **Environment Management**: Python-Decouple (for API security).

## 📋 Prerequisites

- Python 3.10+
- Groq API Key ([Get it here](https://console.groq.com/))
- Redis (Optional: Required for production scaling)

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Akshat8510/Real-Time-Chat-Application.git
   cd Real-Time-Chat-Application
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DEBUG=True
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/chat/` to start chatting!

## 🤖 Using the AI

To interact with the AI assistant:
1. Enter any chat room (e.g., "lobby").
2. Type your message starting with `/ai`.
3. Example: `/ai explain quantum physics in one sentence`.
4. The AI will respond in real-time to everyone in the room.


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---
**Developed by [Akshat](https://github.com/Akshat8510)**
