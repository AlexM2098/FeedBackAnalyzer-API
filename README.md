# FeedbackAnalyzer

FeedbackAnalyzer is a Flask-based API that classifies customer feedback into various categories such as "compliment," "complaint," "suggestion," and "query" using a Naive Bayes classifier.

## Project Structure

```
FeedbackAnalyzer/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models/
│ │ ├── init.py
│ │ ├── classifier.py
│ │ └── data/
│ │ ├── model.pkl
│ │ └── vectorizer.pkl
│ │
│ └── utils/
│ ├── init.py
│ └── preprocess.py
│
├── config.py
├── run.py
└── requirements.txt
```

## Setup and Installation

1. **Python Environment**: Ensure Python is installed on your system.
2. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd FeedbackAnalyzer

1. Install Required Libraries:
    pip install -r requirements.txt

## Running the API
1. Start the Flask server:
 ```bash
    python run.py
```

2. The server should start and be accessible at http://127.0.0.1:5000/

## Using the API

To classify feedback, make a POST request to the /predict endpoint with the feedback text:
```
{
    "feedback": "Your feedback text here"
} 
```
The response will contain the predicted category for the feedback.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.