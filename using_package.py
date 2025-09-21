# Now that we've built a package, we can use it in other files. 

# here is an example of using our package in a "get diagnosis message script"

from lr_package import lr_model, mse, r2 # we used to have to import these from seperate files, but now we can import them from one package 
def get_diagnosis_message(bmi, age):
    """
    This function takes in a bmi and age and returns a diagnosis message
    """

    # make a prediction
    prediction = lr_model.predict([[bmi, age]])

    # get the diagnosis message
    diagnosis_message = f"\n\n Dear client. Based on your bmi of {bmi} and age of {age}, your diagnosis is a diabetes progression of {prediction}. This prediction is based on a linear regression model with a mse of {mse} and r2 of {r2}"
    return diagnosis_message

# test the function
print(get_diagnosis_message(25, 45))