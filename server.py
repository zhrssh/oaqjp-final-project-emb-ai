"""
Server for running emotion detection
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Main route of the server app
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Emotion detector route
    """
    if "textToAnalyze" not in request.args:
        return jsonify(error_message="Missing 'textToAnalyze' query"), 400

    # Call function
    text_to_analyse = request.args["textToAnalyze"]
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    message = (
        f"For the given statement, "
        f"the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']} "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return message


if __name__ == "__main__":
    app.run(port=5000, debug=True)
