from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target # X is 'age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'
                                   # y is diabetes progression

print(diabetes.feature_names) # see the X features
print(diabetes.DESCR) # see the dataset description

print(X.shape)
print(y.shape)


# Lets pretend we are only interested in the 'bmi' and 'age' features
X = X[:, [0, 2]] # age and bmi are the 3rd and 1st feature names in the X features. The colon at the beginning means we keep all the samples the same
features = diabetes.feature_names[2] + " " + diabetes.feature_names[0] # sanity check to see if we are selecting the correct feature
print(features)

print(X.shape)
print(y.shape)
# great! Now we can see 442 X samples with 1 feature, pairing up to 442 diabetes progression values
# now we can split into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

