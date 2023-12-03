import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Salary_Data.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=model.score(x_test,y_test)
print("accuracy =",accuracy)
plt.scatter(x_train,y_train,color ='red')
plt.plot(x_train,model.predict(x_train),color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()