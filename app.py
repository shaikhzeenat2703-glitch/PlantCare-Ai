import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import json

from solutions import solutions
from translations import translations
from chatbot import get_chatbot_response


app = Flask(__name__)


# ==========================================
# MODEL
# ==========================================

MODEL_PATH = "model/plant_disease_model_efficientnet.keras"

model = tf.keras.models.load_model(MODEL_PATH)


# ==========================================
# CLASS NAMES
# ==========================================

with open("model/class_names.json", "r") as file:
    class_names = json.load(file)


# ==========================================
# CONFIDENCE THRESHOLD
# ==========================================

CONFIDENCE_THRESHOLD = 90.0


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    lang = request.args.get("lang", "en")

    if lang not in translations:
        lang = "en"

    t = translations[lang]

    return render_template(
        "index.html",
        lang=lang,
        t=t
    )


# ==========================================
# PREDICT DISEASE
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    lang = request.args.get("lang", "en")

    if lang not in translations:
        lang = "en"

    t = translations[lang]


    # ------------------------------------------
    # CHECK IMAGE
    # ------------------------------------------

    if "image" not in request.files:
        return "No image uploaded."


    file = request.files["image"]


    if file.filename == "":
        return "Please select an image."


    # ------------------------------------------
    # OPEN IMAGE
    # ------------------------------------------

    try:

        image = Image.open(file).convert("RGB")

    except Exception:

        return "Invalid image file."


    # ------------------------------------------
    # RESIZE IMAGE
    # ------------------------------------------

    image = image.resize((224, 224))


    # ------------------------------------------
    # CONVERT TO NUMPY
    # ------------------------------------------

    image_array = np.array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )


    # ------------------------------------------
    # MODEL PREDICTION
    # ------------------------------------------

    prediction = model.predict(
        image_array,
        verbose=0
    )


    predicted_index = np.argmax(
        prediction
    )


    disease_name = class_names[
        predicted_index
    ]


    confidence = float(
        prediction[0][predicted_index] * 100
    )


    # ==========================================
    # UNKNOWN / UNSUPPORTED IMAGE CHECK
    # ==========================================

    if confidence < CONFIDENCE_THRESHOLD:

        if lang == "hi":

            disease_display = (
                "असमर्थित या अस्पष्ट पौधे की फोटो"
            )

            solution_display = (
                "कृपया Tomato, Potato या Pepper "
                "के पत्ते की साफ और स्पष्ट फोटो अपलोड करें।"
            )

        elif lang == "mr":

            disease_display = (
                "असमर्थित किंवा अस्पष्ट वनस्पतीचा फोटो"
            )

            solution_display = (
                "कृपया Tomato, Potato किंवा Pepper "
                "च्या पानाचा स्वच्छ आणि स्पष्ट फोटो अपलोड करा."
            )

        else:

            disease_display = (
                "Unsupported or Unclear Plant Image"
            )

            solution_display = (
                "Please upload a clear image of a "
                "Tomato, Potato, or Pepper leaf."
            )


        return render_template(
            "result.html",
            lang=lang,
            t=t,
            disease=disease_display,
            confidence=round(confidence, 2),
            solution=solution_display,
            is_unknown=True
        )


    # ==========================================
    # NORMAL DISEASE RESULT
    # ==========================================

    translated_disease = t["diseases"].get(
        disease_name,
        disease_name
    )


    solution = t["solutions"].get(
        disease_name,
        solutions.get(
            disease_name,
            "No specific solution available."
        )
    )


    return render_template(
        "result.html",
        lang=lang,
        t=t,
        disease=translated_disease,
        confidence=round(confidence, 2),
        solution=solution,
        is_unknown=False
    )


# ==========================================
# CHATBOT
# ==========================================

@app.route("/chat", methods=["POST"])
def chat():

    message = request.form.get(
        "message",
        ""
    )


    language = request.form.get(
        "lang",
        "en"
    )


    response = get_chatbot_response(
        message,
        language
    )


    return response


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)