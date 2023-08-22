import pickle
from app.utils.preprocess import preprocess_text

# Load trained model and vectorizer
with open('app/models/data/model.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('app/models/data/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def classify_feedback(feedback):
    processed_feedback = preprocess_text(feedback)
    feedback_vec = vectorizer.transform([processed_feedback])
    category = clf.predict(feedback_vec)[0]
    return category
