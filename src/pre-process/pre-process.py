import cv2 as cv
import numpy as np
import os
import sys
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio as im
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
#from own_modules.ImageData.ImageDataset_v2 import *
#from own_modules.KerasCallbacks import custom_keras_callbacks

print(cv.__version__)
print(tf.config.list_physical_devices('GPU'))