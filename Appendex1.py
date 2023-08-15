
# Problem statement
# Classify a X-Ray image as being normal or Abnormal.
# Import libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Define path
import pathlib
data_dir = "data/train/" # Datasets path
data_dir = pathlib.Path(data_dir)
data_dir
# Define classes
normal = list(data_dir.glob('NORMAL/*'))
Abnormal = list(data_dir.glob('Abnormal/*'))

print("Length of normal: ", len(normal))
print("Length of Abnormal: ", len(tb))
# Print random images
import matplotlib.image as img
import PIL.Image as Image

fig, ax = plt.subplots(ncols= 2, nrows = 1, figsize=(20,5))
fig.suptitle('Category')

rand_normal = np.random.randint(-1,len(normal))
print(rand_normal)

Abnormal = np.random.randint(-1, len(tb))
print(Abnormal)

normal_image = img.imread(normal[rand_normal])
abnormal = img.imread(tb[Abnormal])
ax[0].set_title('normal')
ax[1].set_title('abnormal')
ax[0].imshow(normal_image)
ax[1].imshow(abnormal)

# contains the images path

df_images = {
    'normal' : normal,
    'abnormal' : abnormal
}

# contains numerical labels for the categories
df_labels = {
    'abnormal' : 0,
    'abnormal' : 1
}
# Get shape of image
import cv2
img = cv2.imread(str(df_images['abnormal'][abnormal])) # Converting it into numerical arrays
img.shape
# Define X and y
X, y = [], [] # X = images, y = labels
for label, images in df_images.items():
    for image in images:
        img = cv2.imread(str(image))
        resized_img = cv2.resize(img, (224, 224)) # Resizing the images to be able to pass on MobileNetv2 model
        X.append(resized_img) 
        y.append(df_labels[label])
print(len(X), len(y))
# Convert X and y to numpy arrays
X = np.array(X)
y = np.array(y)
# Split X and y into training, validation, and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test_val, y_train, y_test_val = train_test_split(X, y, train_size = 0.8, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(X_test_val, y_test_val, random_state=42)
X_train.shape, X_val.shape, X_test.shape, y_train.shape, y_val.shape, y_test.shape

# Tensorflow
import tensorflow as tf 
from tensorflow import keras 
import tensorflow_hub as hub
from keras.utils.np_utils import to_categorical
from tensorflow.keras.applications import VGG19
from tensorflow.keras.applications import MobileNetV2, DenseNet169
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Input, Lambda, Dense, Flatten
from glob import glob
from keras.models import Model
print(tf.__version__)

# Normalise data
normalizer = tf.keras.layers.Rescaling(scale=1/255)
# Define input shape to pretrained models
input_shape = (224, 224, 3)
input_layer = keras.Input(shape = (224, 224, 3))

# Set up pretrained models
input_shape = (224, 224, 3)

vgg = VGG19(weights='imagenet', include_top=False, input_shape=input_shape)
for layer in vgg.layers:
    layer.trainable = False

# Define model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
folders = glob('data/train/*')
x = Flatten()(vgg.output)

prediction = Dense(len(folders), activation='softmax')(x)
# create a model object
model = Model(inputs=vgg.input, outputs=prediction)
# view the structure of the model
model.summary()

model.compile(
  optimizer="adam",
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['acc'])

from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Model

# Train the model
early_stopping = EarlyStopping(monitor='val_loss', mode='min', patience=25, verbose=1)
mc = ModelCheckpoint ('best_model.h5', monitor='val_loss', mode='min', save_best_only=True)
history = model.fit(X_train, y_train, epochs=17, validation_data=(X_val, y_val), callbacks=[early_stopping, mc])


# Plot accuracy and loss graphs
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy') 
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

model.save("model.h5")

# Make predictions
y_pred = model.predict(X_test, batch_size=64, verbose=1)
y_pred_bool = np.argmax(y_pred, axis=1)
y_pred_bool


from sklearn.metrics import accuracy_score

total_right = accuracy_score(y_test, y_pred_bool, normalize=False)
print(total_right)
accuracy = (total_right / len(y_test))
print(accuracy)


model.evaluate(X_test,y_test)
from sklearn.metrics import classification_report
# Classification Report
print(classification_report(y_test, y_pred_bool))
from mlxtend.plotting import plot_confusion_matrix

from sklearn.metrics import confusion_matrix
# plot_confusion_matrix 
cm= confusion_matrix(y_test, y_pred_bool)
plot_confusion_matrix(cm, figsize=(5,5))

# plot train and test acc
epochs= range(1, len(history.history["acc"])+1)
plt.plot(epochs, history.history["acc"], color="purple")
plt.plot(epochs, history.history["val_acc"], color="pink")
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.title("Accuracy plot")
plt.legend(["train_acc", "val_acc"])
plt.show()

# plot train and test losses
plt.plot(epochs, history.history["loss"], color="purple")
plt.plot(epochs, history.history["val_loss"], color="pink")
plt.xlabel("epochs")
plt.ylabel("loss")
plt.title("Loss plot")
plt.legend(["train_loss", "val_loss"])
plt.show()
df = pd.DataFrame({'actual': y_test, 'predicted': y_pred_bool})
df


#testing , predicting image
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import keras.utils as image

model=load_model('PN1.h5')
img=image.load_img('C:/Users/pc/Desktop/Pneumonia/data/val/PNEUMONIA/person1946_bacteria_4875.jpeg',target_size=(224,224,-1))

import numpy as np
x=image.img_to_array(img)
x=np.expand_dims(x, axis=0)
img_data=preprocess_input(x)
classes=model.predict(img_data)
result=int(classes[0][0])

if result > 0.5:
    print("Result is Normal")
    
else:
    print("Person is Affected ")