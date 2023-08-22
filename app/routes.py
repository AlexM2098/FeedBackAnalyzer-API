from flask import request, jsonify
from app.models.classifier import classify_feedback

def setup_routes(app):
    @app.route('/predict', methods=['POST'])
    def predict_feedback():
        data = request.get_json()
        feedback = data.get('feedback', '')
        category = classify_feedback(feedback)
        return jsonify({'category': category})
