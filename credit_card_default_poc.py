import numpy as np
import pandas as pd

try:
    __IPYTHON__
except NameError:
    print ("Not running in IPython, this check won't matter unless we use matplotlib to show graphs")

# Assumes UCI_Credit_Card.csv is present in the same directory as this script
df = pd.read_csv("UCI_Credit_Card.csv")

# frac determines the split ratio, random_state is a specified seed we can give to have static sample data. Remove to randomise each time
train = df.sample(frac=0.6, random_state=200)
test = df.drop(train.index)

model1 = run_model(train, test)
model2 = run_model(train, test)

def run_model(train, test):
    # Run a model here with the training and test datasets
    model = "model function here"
    return model

def run_model2(train, test):
    # Run another model here
    model = "model function here"
    return model
