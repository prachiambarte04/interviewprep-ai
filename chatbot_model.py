# chatbot_model.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Load Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read dataset
with open(
    r"D:\nlp_projects\basic_nlp_mini_project\questions",
    "r",
    encoding="utf-8"
) as f:
    questions = f.read().splitlines()

with open(
    r"D:\nlp_projects\basic_nlp_mini_project\answers",
    "r",
    encoding="utf-8"
) as f:
    answers = f.read().splitlines()

# Embedding file
embedding_file = "embeddings.pkl"

# Create or load embeddings
if os.path.exists(embedding_file):
    with open(embedding_file, "rb") as f:
        question_embeddings = pickle.load(f)
    print("Embeddings loaded from pickle.")
else:
    question_embeddings = model.encode(questions)

    with open(embedding_file, "wb") as f:
        pickle.dump(question_embeddings, f)

    print("Embeddings created and saved.")

# Chat function
def get_answer(user_input):

    user_embedding = model.encode([user_input])

    similarity = cosine_similarity(
        user_embedding,
        question_embeddings
    )

    index = similarity.argmax()
    score = similarity.max()

    # Confidence handling
    if score < 0.40:
        return "I am not sure. Please ask differently."

    elif score < 0.60:
        return f"I think this may help:\n\n{answers[index]}"

    else:
        return answers[index]