from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the AI embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Read the knowledge base
with open("data/mentor_knowledge.txt", "r", encoding="utf-8") as file:
    knowledge = file.read()


# Split knowledge into separate lines
documents = [
    line.strip()
    for line in knowledge.splitlines()
    if line.strip()
]


# Convert knowledge into embeddings
document_embeddings = model.encode(documents)


# Ask a question
question = input("Ask your project mentor: ")


# Convert question into an embedding
question_embedding = model.encode([question])


# Calculate similarity
similarities = cosine_similarity(
    question_embedding,
    document_embeddings
)[0]


# Get the best results
best_indices = similarities.argsort()[-5:][::-1]


print("\nMost relevant information:\n")

for index in best_indices:
    print("-", documents[index])