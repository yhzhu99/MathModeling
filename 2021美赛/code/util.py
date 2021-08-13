from numpy import arange
from numpy import absolute
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from matplotlib import pyplot

# evaluate a model


def evaluate_model(X, y, model):
    # define model evaluation method
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
    # evaluate model
    scores = cross_val_score(
        model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
    # force scores to be positive
    return absolute(scores)

# plot the dataset and the model's line of best fit


def plot_best_fit(X, y, model):
    # fut the model on all data
    model.fit(X, y)
    # plot the dataset
    pyplot.scatter(X, y, s=100, c='blue')
    # plot the line of best fit
    xaxis = arange(X.min(), X.max(), 0.01)
    yaxis = model.predict(xaxis.reshape((len(xaxis), 1)))
    pyplot.xlabel('Hyphal extension rate (%)', fontsize=14)
    pyplot.ylabel('Decomposition rate (mm/day)', fontsize=14)
    ty = type(model).__name__
    if ty == 'LinearRegression':
        pyplot.plot(xaxis, yaxis, color='green', label=ty)
    elif ty == 'HuberRegressor':
        pyplot.plot(xaxis, yaxis, color='red', label=ty)
    elif ty == 'TheilSenRegressor':
        pyplot.plot(xaxis, yaxis, color='skyblue', label=ty)
    # show the plot
    pyplot.title('Comparison of Regression Methods')
    # pyplot.show()
