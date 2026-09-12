# Final Project - Flask Emotion Detector

A lightweight Flask web application that analyzes text and identifies its underlying emotional tone. The application evaluates five core emotions—**anger, disgust, fear, joy, and sadness**—and reports the emotion with the highest confidence score.

> **Note:** The project uses the IBM Watson NLP service provided through the IBM Skills Network environment. The emotion API may only be accessible from the course/cloud environment where it is provided.

## Features

- **Real-time emotion analysis** — Submit text and receive emotion confidence scores.
- **Multi-emotion detection** — Evaluates five emotional dimensions.
- **Dominant emotion detection** — Identifies the strongest emotion in the input.
- **Simple web interface** — Enter text and view the result directly in the browser.
- **REST endpoint** — Analyze text programmatically through `/emotionDetector`.
- **Input handling** — Returns a clear response for empty or invalid input.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, JavaScript, Bootstrap
- **NLP:** IBM Watson NLP / Skills Network Emotion Prediction service

## Project Structure

```text
flask-emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py    # Emotion detection logic
├── static/
│   └── mywebscript.js           # Frontend interaction
├── templates/
│   └── index.html               # Web interface
├── server.py                    # Flask application entry point
├── test_emotion_detection.py    # Unit tests
├── requirements.txt             # Python dependencies
├── LICENSE
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd flask-emotion-detector
```

### 2. Create a virtual environment

Recommended for keeping project dependencies isolated:

```bash
python -m venv venv
```

Activate it with:

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Start the application

```bash
python server.py
```

The Flask application will run on:

```text
http://localhost:5000
```

### Web Interface

1. Open `http://localhost:5000` in your browser.
2. Enter the text you want to analyze.
3. Click **Run Sentiment Analysis**.
4. The application displays the confidence scores and dominant emotion.

### API Endpoint

The application exposes the `/emotionDetector` endpoint.

Example:

```bash
curl "http://localhost:5000/emotionDetector?textToAnalyze=I%20am%20so%20happy%20today"
```

Example response:

```text
For the given statement, the system response is 'anger': 0.01, 'disgust': 0.02,
'fear': 0.01, 'joy': 0.95, 'sadness': 0.01. The dominant emotion is joy.
```

## Running Tests

Run the included unit tests with:

```bash
python -m unittest test_emotion_detection
```

The tests cover the five supported emotions:

| Emotion | Example meaning |
|---------|------------------|
| Anger | Frustration, irritation, or hostility |
| Disgust | Revulsion or strong disapproval |
| Fear | Anxiety, worry, or apprehension |
| Joy | Happiness, contentment, or excitement |
| Sadness | Sorrow, grief, or disappointment |

## Important Note

This repository is based on a Flask emotion-detection project developed using IBM Watson NLP and the IBM Skills Network learning environment. The external emotion prediction service is required for the detector to return live results.

## License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for details.

## Acknowledgments

- IBM Developer Skills Network for the learning environment and project guidance.
- IBM Watson NLP for the emotion detection capabilities.
