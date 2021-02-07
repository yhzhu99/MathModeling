# huber regression on a dataset with outliers
from random import random
from random import randint
from random import seed
from numpy import arange
from numpy import mean
from numpy import std
from numpy import absolute
from numpy import array
from sklearn.datasets import make_regression
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from matplotlib import pyplot

decomp=[]
extent=[]

with open('./data/decomposition_rate_temp.txt','r') as de:
    for line in de:
        x=line.split()
        decomp.append(float(x[-4])) # 10 degree
        decomp.append(float(x[-3])) # 16 degree
        decomp.append(float(x[-2])) # 22 degree
with open('./data/extension_rate_temp.txt','r') as ex:
    for line in ex:
        x=line.split()
        extent.append(float(x[-3])) # 10 degree
        extent.append(float(x[-2])) # 16 degree
        extent.append(float(x[-1])) # 22 degree

decomp_10=[decomp[i] for i in range(0,34*3,3)]
decomp_16=[decomp[i] for i in range(1,34*3,3)]
decomp_22=[decomp[i] for i in range(2,34*3,3)]
extent_10=[extent[i] for i in range(0,34*3,3)]
extent_16=[extent[i] for i in range(1,34*3,3)]
extent_22=[extent[i] for i in range(2,34*3,3)]

# evaluate a model
def evaluate_model(X, y, model):
	# define model evaluation method
	cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
	# evaluate model
	scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
	# force scores to be positive
	return absolute(scores)
 
# plot the dataset and the model's line of best fit
def plot_best_fit(X, y, model):
	# fut the model on all data
	model.fit(X, y)
	# plot the dataset
	pyplot.scatter(X, y)
	# plot the line of best fit
	xaxis = arange(X.min(), X.max(), 0.01)
	yaxis = model.predict(xaxis.reshape((len(xaxis), 1)))
	pyplot.plot(xaxis, yaxis, color='r')
	# show the plot
	pyplot.title(type(model).__name__)
	pyplot.show()
 
# load dataset
X = array(extent_16).reshape((34,1))
y = array(decomp_16)
# define the model
model = HuberRegressor()
# evaluate model
results = evaluate_model(X, y, model)
print('Mean MAE: %.3f (%.3f)' % (mean(results), std(results)))
# plot the line of best fit
plot_best_fit(X, y, model)