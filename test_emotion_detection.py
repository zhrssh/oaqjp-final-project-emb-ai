"""
Testing emotion detection
"""
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happened"
        response = emotion_detector(text)
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        text = "I am really mad about this"
        response = emotion_detector(text)
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        text = "I feel disgusted just hearing about this"
        response = emotion_detector(text)
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_sadness(self):
        text = "I am so sad about this"
        response = emotion_detector(text)
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        text = "I am really afraid that this will happen"
        response = emotion_detector(text)
        self.assertEqual(response["dominant_emotion"], "fear")
