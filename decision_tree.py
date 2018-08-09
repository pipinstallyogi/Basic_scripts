from sklearn import tree

#[height, weight, shoe size]

A = [[181, 80, 44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]

B = ['male','female','female','female','male','male','male','female','male','female','male']


# clf store our decisiontree classifier,
clf = tree.DecisionTreeClassifier()

# fit() method trains the decision tree on our dataset
clf= clf.fit(A,B)

#predict() method will help predicting the given input based on training set
prediction = clf.predict([[157,50,36]])

print prediction

