import streamlit as st
import ollama
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="AI Project Mentor",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# LOAD AI EMBEDDING MODEL
# ============================================================

@st.cache_resource
def load_embedding_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


embedding_model = load_embedding_model()


# ============================================================
# LOAD KNOWLEDGE BASE
# ============================================================

@st.cache_data
def load_knowledge():

    try:
        with open(
            "data/mentor_knowledge.txt",
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        documents = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        return documents

    except FileNotFoundError:

        return [
            "A good hackathon project should solve a real-world problem.",
            "A project should have a clear problem statement and target users.",
            "Technology should be selected according to project requirements.",
            "A project roadmap includes problem analysis, design, development, testing, and deployment.",
            "A good PPT should explain the problem, proposed solution, technology, architecture, results, and future scope.",
            "Viva questions can cover the problem statement, technology selection, architecture, implementation, challenges, and future scope.",
            "Hackathon projects should be innovative, useful, feasible, and easy to demonstrate."
        ]


documents = load_knowledge()


# ============================================================
# CREATE EMBEDDINGS
# ============================================================

@st.cache_data
def create_document_embeddings(documents):

    embeddings = embedding_model.encode(
        documents,
        convert_to_numpy=True
    )

    return embeddings


document_embeddings = create_document_embeddings(documents)


# ============================================================
# SEMANTIC SEARCH
# ============================================================

def search_knowledge(question):

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    similarity_scores = cosine_similarity(
        question_embedding,
        document_embeddings
    )[0]

    top_indices = similarity_scores.argsort()[::-1][:5]

    results = []

    for index in top_indices:
        results.append(documents[index])

    return results


# ============================================================
# TITLE
# ============================================================

st.title("🤖 AI Project Mentor")

st.write(
    "Your AI-powered mentor for hackathons and project development."
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🎯 Mentor Mode")

    mentor_mode = st.selectbox(
        "Choose a mode",
        [
            "Project Ideas",
            "Problem Analysis",
            "Technology Selection",
            "Project Roadmap",
            "PPT & Documentation",
            "Viva Preparation"
        ]
    )

    st.divider()

    st.header("📋 My Project")

    project_name = st.text_input(
        "Project Name",
        placeholder="Example: AI Crop Disease Detector"
    )

    project_domain = st.text_input(
        "Project Domain",
        placeholder="Example: Agriculture"
    )

    problem_statement = st.text_area(
        "Problem Statement",
        placeholder="Describe the problem your project solves"
    )


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ============================================================
# USER QUESTION
# ============================================================

user_question = st.chat_input(
    "Ask your project mentor..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if user_question:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_question)


    # --------------------------------------------------------
    # SEARCH KNOWLEDGE BASE
    # --------------------------------------------------------

    relevant_information = search_knowledge(
        user_question
    )

    context = "\n".join(
        relevant_information
    )


    # --------------------------------------------------------
    # PROJECT INFORMATION
    # --------------------------------------------------------

    if project_name:
        project_info = f"""
Project Name: {project_name}
Project Domain: {project_domain}
Problem Statement: {problem_statement}
"""
    else:
        project_info = """
The student has not provided project information yet.
"""


    # --------------------------------------------------------
    # AI PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are an AI mentor for a student participating in a hackathon.

Mentor Mode:
{mentor_mode}

Student Project:
{project_info}

Relevant knowledge:
{context}

Student Question:
{user_question}

Instructions:

- Give a clear and useful answer.
- Use simple language.
- Give practical steps when possible.
- Personalize the answer according to the student's project.
- If recommending technology, explain why.
- If giving a roadmap, provide numbered steps.
- If discussing a PPT, provide slide-by-slide guidance.
- If discussing viva, provide possible questions and answers.
- Do not make up information.
"""


    # --------------------------------------------------------
    # GET RESPONSE FROM OLLAMA
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("🤖 AI Mentor is thinking..."):

            try:

                response = ollama.chat(
                    model="llama3.2:3b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                answer = response["message"]["content"]

                st.write(answer)

                # Save assistant message
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as error:

                st.error(
                    "Could not connect to Ollama."
                )

                st.info(
                    "Make sure Ollama is running and "
                    "llama3.2:3b is installed."
                )

                st.code(
                    "ollama run llama3.2:3b"
                )

                st.caption(
                    f"Error: {error}"
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

