# importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset

dataset = pd.read_csv('../Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# splitting the dataset into the Training set and Testing set
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# fitting simple linear regression to the Training set
from sklearn.linear_model import LinearRegression

model = LinearRegression()
# train model
model.fit(x_train, y_train)

# prediction the Test set result

y_prediction = model.predict(x_test)

accuracy = model.score(x_test, y_test)

print("accuracy =", accuracy)


# visualizing the Training set result

plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, model.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
