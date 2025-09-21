
"""
We are now inside a package called lr_package. This package contains all of the linear regression code you explored earlier
Only now instead of importanting from each file directly, we can import from the package. 

This is a good practice because it makes the code more organized and easier to maintain.

We can also use the __init__.py file to define what gets imported when someone does "from lr_package import *"


"""

print("LR Package loaded!")

from .data_preprocessing import X_train, y_train
from .model import lr_model

# Import the evaluation module to run it and get the metrics
from . import eval

# Now we can access the metrics that were calculated in these files
mse = eval.mse
r2 = eval.r2
model = model.lr_model
print("mse r2 and model can now be accessed from lr_package!")

# this allows us to import the data_preprocessing, model, and eval modules from the ml_package package rather than importing them all seperately