from sklearn import linear_model
import pandas

dataset = pandas.read_csv("coinmarketcap_dataset.csv")

target = dataset.iloc[:,1].values
# target = dataset.iloc[:,1].values
print(target)

data = dataset.iloc[:,8:10].values
print(data)

machine = linear_model.LogisticRegression()

machine.fit(data, target)

new_data = [
	[20201110182620, ],
 	[1,-0.55,0.55,1.3,-0.011,1],
 	[2,-0.53,0.9,0.36,-0.0123,0],
 	[2.3,-0.23,0.33,0.32,-0.019,1],
 	[10,-0.23,0.33,0.32,-0.019,1],
 ]

# results = machine.predict(new_data)

# print(results)