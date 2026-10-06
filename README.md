🤖 AI Hackathon & Project Mentor Chatbot

An AI-powered chatbot designed to help students and hackathon participants with project ideas, technology selection, development guidance, and hackathon preparation.

The chatbot uses a local knowledge base and semantic search to understand user questions and provide relevant project-related guidance.

🌟 Features
💡 Project Idea Suggestions – Suggests innovative ideas based on the user's interests.
🧠 AI-Powered Q&A – Answers questions related to hackathons and project development.
🛠️ Technology Guidance – Helps select suitable technologies and tools for a project.
📋 Project Planning – Provides guidance on planning and structuring projects.
🔍 Semantic Search – Finds relevant information from the project's local knowledge base.
📚 Hackathon Guidance – Helps users understand problem statements, features, implementation, and presentation.
💻 Simple Web Interface – Built using Streamlit for easy interaction.
🎯 Problem Statement

Students participating in hackathons often struggle with:

Choosing a suitable project idea
Understanding problem statements
Selecting the right technology stack
Planning project features
Knowing how to start development
Preparing their project for presentation

This chatbot acts as a virtual project mentor that provides quick and relevant guidance throughout the project development process.

💡 Proposed Solution

The AI Hackathon & Project Mentor Chatbot provides a conversational interface where users can ask questions about their projects.

The system searches a local knowledge base using semantic similarity and returns the most relevant information to the user's query.

Example

User:

Suggest an AI project for a healthcare hackathon.

Chatbot:

Suggests suitable project ideas along with possible features, technologies, and implementation directions.

🏗️ System Architecture
              ┌──────────────────────┐
              │        User          │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Streamlit UI       │
              │       app.py         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   User Query         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Semantic Search    │
              │ semantic_search.py   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Mentor Knowledge Base│
              │ mentor_knowledge.txt │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Relevant Information │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   AI Mentor Response │
              └──────────────────────┘
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Sentence Transformers	Semantic understanding/search
NumPy	Numerical operations
Pandas	Data processing
Python-dotenv	Environment configuration
Git & GitHub	Version control and project hosting
📁 Project Structure
AI-HACKATHON-PROJECT-MENTOR-CHATBOT/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── mentor_knowledge.txt
│
├── app.py
├── semantic_search.py
├── .gitignore
└── README.md
⚙️ How to Run the Project Locally
1. Clone the repository
git clone https://github.com/pranathilaxmi/AI-HACKATHON-PROJECT-MENTOR-CHATBOT.git
2. Move into the project directory
cd AI-HACKATHON-PROJECT-MENTOR-CHATBOT
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1
5. Install required packages
pip install streamlit pandas numpy requests python-dotenv sentence-transformers transformers torch
6. Run the application
streamlit run app.py

The chatbot will open in your browser.

💬 Example Questions

Users can ask questions such as:

Suggest a project idea for an AI hackathon.

What technology should I use for my project?

How can I make my project unique?

How should I plan my hackathon project?

What features can I add to my project?

How can I present my project effectively?

What AI technologies can I use?
🔍 How Semantic Search Works

The chatbot uses semantic search to find information related to the user's question.

User Question
      ↓
Convert Query into Embedding
      ↓
Compare with Knowledge Base
      ↓
Find Most Relevant Content
      ↓
Generate Relevant Response

Unlike simple keyword matching, semantic search focuses on the meaning of the query, allowing the chatbot to identify related information even when the exact words are different.

🚀 Future Enhancements
🤖 Integration with advanced Large Language Models
📄 PDF/document-based project guidance
🧑‍💻 Personalized project recommendations
🏆 Hackathon problem-statement analyzer
📊 Project evaluation and scoring
💬 Conversation history
🌐 Deployment as a public web application
🔐 User authentication
📱 Mobile-friendly interface
🎯 Applications

The chatbot can be useful for:

College students
Hackathon participants
Beginner developers
Project teams
Engineering students
Startup idea exploration
Academic mini-project planning
👩‍💻 Author

Kunta Pranathi Laxmi

B.Tech – CSE (Data Science)

Malla Reddy Engineering College for Women

📜 License

This project is developed for educational and training purposes.
