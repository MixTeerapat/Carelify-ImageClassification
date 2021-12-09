# Carelify-ImageClassification
These are the files for training ImageClassification using pre-trained model and fine tuning from Keras, and after running all the codes from Xception.ipynb, you would receive:
1. fine tuned model (.h5) 
2. Accuracy and Loss graphs (both before and after fine tuning) 
3. Statistics, Matrix, and Heatmap

The Xception.ipynb is just only the template for training Xception pre-trained model. You could change the pre-trained model based on your preferrence including VGG16, ResNet50, MobileNetV2. More specific information will be provided on the Keras website.

After receiving the .h5 model from the code, we can connect and utilize it (for predicting images) locally with the Flask (Micro Web Framework) by running main4.py in the 'web' directory.

To run the code, you must change the path that belongs to your dataset path or other path in directory on your computer. It would probably not exactly like the path provided in the code. Moreover, preprocess_input and model import code might also be different depends on the seleted model.

Hope you enjoy !!

