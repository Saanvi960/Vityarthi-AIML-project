from sklearn.linear_model import LinearRegression
import numpy as np

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70, 80, 85])

model = LinearRegression()
model.fit(hours, marks)

h = float(input("Enter study hours: "))

predicted = model.predict([[h]])

print("Predicted Marks:", int(predicted[0]))