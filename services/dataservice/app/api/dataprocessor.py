# Importing the libraries
import pandas as pd
import numpy as np

# Importing the Boston Housing dataset
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

def prepare_datasets():
    # Loading the Boston Housing dataset
    boston = load_boston()

    # Initializing the dataframe
    data = pd.DataFrame(boston.data)

    # Adding the feature names to the dataframe
    data.columns = boston.feature_names

    # Adding target variable to dataframe
    data['PRICE'] = boston.target

    # Split the data into train and test with 80 train / 20 test
    train, test = train_test_split(data, test_size=0.2, random_state=1)
    train, val = train_test_split(train, test_size=0.2, random_state=1)

    # Normalize the training and test data
    norm_train_X = np.array(norm(train, train))
    norm_test_X = np.array(norm(test, train))
    norm_val_X = np.array(norm(val, train))

    train_Y = format_output(train)
    test_Y = format_output(test)
    val_Y = format_output(val)

    return norm_train_X, norm_test_X, norm_val_X, train_Y, test_Y, val_Y

# Helper functions
def norm(x, train):
    # Get PRICE and PTRATIO as the 2 outputs and format them as np arrays
    # PTRATIO - pupil-teacher ratio by town
    train_stats = train.describe()
    train_stats.pop('PRICE')
    train_stats.pop('PTRATIO')
    train_stats = train_stats.transpose()

    return (x - train_stats['mean']) / train_stats['std']

def format_output(data):
    y1 = data.pop('PRICE')
    y1 = np.array(y1)
    y2 = data.pop('PTRATIO')
    y2 = np.array(y2)
    return y1, y2