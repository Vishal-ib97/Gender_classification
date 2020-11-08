# -*- coding: utf-8 -*-
"""predict

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/142wxul6dUnlj2idnBxqxRco00zdKD-xS
"""

#Evaluation on test data

import keras
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)
m = load_model('/content/drive/My Drive/pictures2/final_model.h5')
test_gen = data_generator.flow_from_directory('/content/drive/My Drive/pictures2/test2', 
                                              target_size=(224, 224), class_mode = 'categorical', 
                                              batch_size = 1, shuffle = False)
loss, accu, auc = m.evaluate(test_gen, verbose = 1)


pred = m.predict(test_gen)
y_pred = np.argmax(pred, axis=1)
conf = confusion_matrix(test_gen.classes, y_pred)

target_names = ['male', 'female']
rep = classification_report(test_gen.classes, y_pred, target_names=target_names)
print(rep)