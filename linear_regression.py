from sklearn import linear_model
import pandas

dataset = pandas.read_csv("coinrank_dataset.csv")

target = dataset.iloc[:,3].values
# print(target)

data = dataset.iloc[:,[5]].values
# print(data)

machine = linear_model.LinearRegression()

machine.fit(data, target)

new_data = [
	[289994],
 	[279994],
 	[269994],
 	[269994]
 ]

results = machine.predict(new_data)

print(results)