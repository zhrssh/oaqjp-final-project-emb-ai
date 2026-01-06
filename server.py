from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    if "textToAnalyze" not in request.args:
        return jsonify(error_message="Missing 'textToAnalyze' query"), 400

    # Call function
    text_to_analyse = request.args["textToAnalyze"]
    response = emotion_detector(text_to_analyse)

    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."


if __name__ == "__main__":
    app.run(port=5000, debug=True)
