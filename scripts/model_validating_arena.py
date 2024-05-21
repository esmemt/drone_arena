#! /usr/bin/env python

# Import libraries
import csv
import keras
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from pandas import read_csv
from keras.utils import plot_model
from tensorflow.keras.models import load_model
from matplotlib.ticker import FuncFormatter


plt.rcParams.update({'font.size': 24})
plt.rcParams['font.family'] = ['Nimbus Roman']
#plt.rcParams['font.NimbusRoman-Regular'] = ['Nimbus Roman']

# Load neural network model
model = load_model('trainingDA_nueva_mod_400epoch_030_2.h5')

# Summarize model
model.summary()
# tf.keras.utils.plot_model(model, to_file='trainingTP1-2-9-10-14-15OBS1-2-3.png', show_shapes=True, show_layer_names=True)

# Prepare and load data
dataframe = read_csv("trainingDA_nueva_mod.csv", delim_whitespace=False, header=None)
dataset = dataframe.values

# Split into input (X) and output (Y) variables
X = dataset[:, 0:94]
Y = dataset[:, 94:96]

# Graph linear and angular velocity training data
x_x = range(len(X))
plt.title("Linear and angular velocity training data")
plt.plot(x_x, Y[:,0], 'g', label="human-driver linear velocity", linewidth=3.0)
plt.plot(x_x, Y[:,1], 'r', label="human-driver angular velocity", linewidth=3.0)
plt.ylabel('linear velocity (m/s), angular velocity (rad/s)')
plt.xlabel('timesteps')

# Adding comma for thousands in x-axis labels
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
plt.gca().xaxis.set_major_formatter(formatter)

plt.legend()
plt.show()

# Convert input and output to numpy arrays of float type
XN = np.array(X, dtype = float)
YN = np.array(Y, dtype = float)

# Reshape the arrays into LSTM format (samples, timesteps, features)
XN = np.reshape(XN, (len(XN), 1, 94))
print("x:", XN.shape, "y:", YN.shape)

# Evaluate the model
score = model.evaluate(XN, YN, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

# Make predictions
ypred = model.predict(XN)
# print(ypred)

# Graph LSTM multi-output prediction
x_ax = range(len(XN))
plt.title("LSTM multi-output prediction")
plt.plot(x_ax, YN[:,0], 'g', label="human-driver linear velocity", linewidth=2.0)
plt.plot(x_ax, ypred[:,0], 'r', label="LSTM predicted linear velocity", linewidth=2.0, linestyle='--')
plt.ylabel('linear velocity (m/s)')
plt.xlabel('timesteps')

# Adding comma for thousands in x-axis labels
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
plt.gca().xaxis.set_major_formatter(formatter)


plt.legend()
plt.show()

plt.title("LSTM multi-output prediction")
plt.plot(x_ax, YN[:,1], 'b', label="human-driver angular velocity", linewidth=2.0)
plt.plot(x_ax, ypred[:,1], 'm', label="LSTM predicted angular velocity", linewidth=2.0, linestyle='--')
plt.ylabel('angular velocity (rad/s)')
plt.xlabel('timesteps')

# Adding comma for thousands in x-axis labels
formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
plt.gca().xaxis.set_major_formatter(formatter)

plt.legend()
plt.show()
