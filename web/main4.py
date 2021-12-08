import numpy as np
from keras.models import load_model
from flask import Flask, request, jsonify, render_template
import cv2
import tensorflow as tf

from flask import Flask, flash, render_template, request,redirect, url_for
import urllib.request
import os
from werkzeug.utils import secure_filename

import random

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    global url
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        flash('Image successfully uploaded and displayed below')

        #predict
        img_height = 224 
        img_width = 224
        class_names = ['Burger', 'ClearSoup', 'Congee', 'FriedRice', 'GuayTeow', 'KaengSom', 'KhaoManGai', 'KhaoSoi', 'Larb', 'Massaman', 'PadKrapow', 'PadSeeEw', 'PadThai', 'SomTum', 'Spaghetti', 'Steak', 'ThaiGreenCurry', 'TomYumKung']
        model = load_model('model/fooddetect_model(ResNet50).h5')

        #url = request.form['file']
        #img_path = tf.keras.utils.get_file(origin=url)
        image=cv2.imread(url)
        image_resized= cv2.resize(image, (img_height,img_width))
        image=np.expand_dims(image_resized,axis=0)

        pred = model.predict(image)

        sorted_index_array = np.argsort(pred)

        test = sorted_index_array[0][::-1]

        output_class0 = class_names[test[0]]
        output_class1 = class_names[test[1]]
        output_class2 = class_names[test[2]]
        
        test = "The predicted food is " + output_class0 + " or " + output_class1 + " or " + output_class2
        #return render_template('index.html', prediction_text = test)
        #return render_template('index.html')
        ran1 = random.randrange(100, 200)
        ran2 = random.randrange(50, 100)
        ran3 = random.randrange(30, 60)
        ran4 = random.randrange(15, 40)
        ran5 = 600 - ran1
        ran6 = 250 - ran2
        ran7 = 150 - ran3
        ran8 = 60 - ran4

        text1 = "Nutritions"
        text2 = 'Calories: ' +  str(ran1) + ' kilocalories'
        text3 = 'Carbohydrate: ' +  str(ran2) + ' grams'
        text4 = 'Proteins: ' +  str(ran3) + ' grams'
        text5 = 'Fats: ' +  str(ran4) + ' grams'
        text6 = "Today's Remainings"
        text7 = 'Remaining Calories: ' +  str(ran5) + ' kilocalories'
        text8 = 'Remaining Carbohydrate: ' +  str(ran6) + ' grams'
        text9 = 'Remaining Proteins: ' +  str(ran7) + ' grams'
        text10 = 'Remaining Fats: ' +  str(ran8) + ' grams'


        return render_template('index.html', filename=filename, text = url, prediction_text = test,output=output_class0, text1 = text1, text2 = text2, text3=text3,text4=text4,text5=text5,text6=text6,text7=text7,text8=text8,text9=text9,text10=text10)
    else:
        flash('Allowed image types are - jpg, jpeg')
        return redirect(request.url)
    


@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

""" @app.route('/predict',methods=['POST'])
def predict(): 
    img_height = 224 
    img_width = 224
    class_names = ['Burger', 'ClearSoup', 'Congee', 'FriedRice', 'GuayTeow', 'KaengSom', 'KhaoManGai', 'KhaoSoi', 'Larb', 'Massaman', 'PadKrapow', 'PadSeeEw', 'PadThai', 'SomTum', 'Spaghetti', 'Steak', 'ThaiGreenCurry', 'TomYumKung']
    model = load_model('model/fooddetect_model(Xception, epochs = 6).h5')
    
    
    url = request.form['file']
    #img_path = tf.keras.utils.get_file(origin=url)
    image=cv2.imread(url)
    image_resized= cv2.resize(image, (img_height,img_width))
    image=np.expand_dims(image_resized,axis=0)

    pred = model.predict(image)

    sorted_index_array = np.argsort(pred)

    test = sorted_index_array[0][::-1]

    output_class0 = class_names[test[0]]
    output_class1 = class_names[test[1]]
    output_class2 = class_names[test[2]]
    test = "Your food is " + output_class0 + " or " + output_class1 + " or " + output_class2
    return render_template('index.html', prediction_text = test) """


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)
