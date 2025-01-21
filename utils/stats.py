import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score

def f1(y_true, y_pred):
    y_true = np.argmax(y_true, axis=1)
    y_pred = np.argmax(y_pred, axis=1)
    return f1_score(y_true, y_pred, average='weighted')

def precision(y_true, y_pred):
    y_true = np.argmax(y_true, axis=1)
    y_pred = np.argmax(y_pred, axis=1)
    return precision_score(y_true, y_pred, average='weighted', zero_division=0)

def recall(y_true, y_pred):
    y_true = np.argmax(y_true, axis=1)
    y_pred = np.argmax(y_pred, axis=1)
    return recall_score(y_true, y_pred, average='weighted')