#!/usr/bin/python3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#toy datasets
from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer

#preprocessing
from sklearn import preprocessing 
#models
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR, SVC

#evaluation
from sklearn.metrics import f1_score, precision_score, recall_score, mean_squared_error

# y = np.arange(1,10,2)
# x = np.arange(1, 6)

# x_prime = np.arange(1.0,5.01, 0.01)
# y_prime = (18111/2) * np.power(x_prime, 4) - 90555* np.power(x_prime, 3) \
# 		+ (633885/2)*np.power(x_prime, 2) - 452773 *x_prime + 217331

# linear = 2*x_prime + 1
# plt.plot(x, y, 'bo', color='red')
# plt.plot(x_prime, linear, color='red')
# plt.plot(x_prime, y_prime, color='blue')
# plt.show()

def regression(model='linear'):
	regression_model = LinearRegression() if model == "linear"\
					 else SVR()

	#load data
	x, y = load_boston(return_X_y = True)
	train_size = int(0.7 * x.shape[0])

	print(train_size)
	x_train = x[:train_size]
	x_test = x[train_size:]
	y_train = y[:train_size]
	y_test = y[train_size:]
	print("Training shapes: X: {} Y:{}".format(x_train.shape, y_train.shape))
	print("Test shapes: X: {} Y:{}".format(x_test.shape, y_test.shape))
	#transform
	transformer = preprocessing.StandardScaler()
	transformer = transformer.fit(x_train)
	x_train_transformed = transformer.transform(x_train)
	x_test_transformed = transformer.transform(x_test)
	#train data
	regression_model.fit(x_train_transformed, y_train)
	#test data
	y_hat = regression_model.predict(x_test_transformed)

	#plot test data:
	x_test_indices = np.arange(len(x_test))
	print(x_test_indices)
	plt.plot(x_test_indices, y_test, color='red')
	plt.plot(x_test_indices, y_hat, color='blue')
	plt.show()
	#evaluate
	regression_evaluation(y_test, y_hat)

def classification_evaluation(y_test, y_hat):
	pred = precision_score(y_test, y_hat)
	recall = recall_score(y_test, y_hat)
	f1 = f1_score(y_test, y_hat)
	print("Evaluation Result: \n")
	print("P = {}\n R = {}\n F1={}".format(pred, recall, f1))

def regression_evaluation(y_test, y_hat):
	print("Evaluation Result:\n")
	print("mse ={}".format(mean_squared_error(y_test, y_hat)))

#
#regression()
#
regression('svr')