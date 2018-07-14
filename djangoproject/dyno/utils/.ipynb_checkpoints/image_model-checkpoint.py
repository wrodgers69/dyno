
import os
import keras
import keras.layers
from keras.models import *
from keras.utils import *
from PIL import Image
import numpy as np
from keras.preprocessing.image import *
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


def predict(img):
    
    model = load_model('/Users/leerodgers/Google Drive/codingprojects/dyno/trained_models/dyno_model_CNN_1')
    img = image.load_img(img, target_size=(256, 256,1), grayscale = True)
    #display(img)
    i_array = image.img_to_array(img)
    x = np.expand_dims(i_array, axis=0)
    
    prediction = model.predict_classes(x)
    pp = model.predict_proba(x)
    
    if prediction == 1:
        return str('Prediction = Good with %s probability' % pp)
    else:
        return print('Bad')

