import numpy as np
from sklearn.linear_model import LinearRegression
from lr_package.data_preprocessing import X_train, y_train  

np.random.seed(12) # this is to make the results reproducible
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

print(f"lr_model.coef_ {lr_model.coef_}")
print(f"lr_model.intercept_ {lr_model.intercept_}")
