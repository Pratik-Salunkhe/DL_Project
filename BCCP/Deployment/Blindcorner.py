from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import os
import numpy as np
import cv2
from collections import Counter
import pygame
import base64

app = Flask(__name__)

pygame.mixer.init()

# Specify the siren audio path
siren_audio_path = r"C:\Users\Admin\Desktop\DL_Project\Deployment\audio\YRL6BSM-siren.mp3"
siren_sound = pygame.mixer.Sound(siren_audio_path)

def predict_class_for_image(raw_img, model_folder_path, top_5_model_names, class_labels):
    raw_img = cv2.resize(raw_img, (100, 100))
    raw_img = np.array(raw_img)  # convert image to array
    raw_img = np.expand_dims(raw_img, axis=0)
    raw_img = raw_img / 255

    # Load each model
    models = []

    for i in top_5_model_names:
        model_path = os.path.join(model_folder_path, i)
        model = load_model(model_path)

        probability = model.predict(raw_img)
        classes = probability.argmax(axis=1)
        models.append(classes[0])  # Append the class value, not the array

    # Find the most frequent class
    most_frequent_class = Counter(models).most_common(1)[0][0]

    predicted_class = class_labels[most_frequent_class]

    return most_frequent_class, predicted_class, models

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        if file:
            # Read the image from file
            image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)

            # Define your variables
            model_folder_path = r"C:\Users\Admin\Desktop\DL_Project\Deployment"
            top_model_names1 = ['finalmodel94_47.h5', 'finalmodel1.h5', 'finalmodel94_04.h5', 'finalmodel89.h5',
                                   'finalmodel92.h5','train-5.h5','train-63.h5','train-62.h5','train-6.h5']
            
            class_labels = ['The vehicle Is Ahead Please Be Alert Drive Slow Sharp Turn A Head', 
                            'The Road Is Empty But Drive Slow Sharp Turn A Head']

            # Make predictions
            most_frequent_class, predicted_class, models = predict_class_for_image(image, model_folder_path, top_model_names1, class_labels)

            # Play the siren sound if predicted class is 'The vehicle Is Ahead Please Be Alert Drive Slow Sharp Turn A Head'
            if predicted_class == 'The vehicle Is Ahead Please Be Alert Drive Slow Sharp Turn A Head':
                siren_sound.play()

            return render_template('index.html', image_path="data:image/png;base64," + base64.b64encode(cv2.imencode('.png', image)[1]).decode('utf-8'),
                                   
                                   predicted_class=predicted_class)
        #models=models,
                        #           most_frequent_class=most_frequent_class,

    return render_template('index.html', image_path=None)

   
if __name__ == '__main__':
    app.run(debug=True)
