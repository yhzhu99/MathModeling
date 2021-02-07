# theilsen regression on a dataset with outliers
from data_loader import load_data
from util import *
from numpy import mean
from numpy import std
from numpy import array
from sklearn.linear_model import TheilSenRegressor

# load dataset
X, y = load_data(10)
# add outliers
X.append(50)
y.append(1)
X = array(X).reshape((len(X), 1))
y = array(y)
# define the model
model = TheilSenRegressor()
# evaluate model
results = evaluate_model(X, y, model)
print('(Theil Sen) Mean MAE: %.3f (%.3f)' % (mean(results), std(results)))
# plot the line of best fit
plot_best_fit(X, y, model)
