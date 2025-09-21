from .data_preprocessing import X_test, y_test  # RELATIVE IMPORT within lr_package
from .model import lr_model  # RELATIVE IMPORT within lr_package

# same code as before. For testing the model
y_pred = lr_model.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"mean_squared_error {mse}")

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(f"r2_score {r2}")
