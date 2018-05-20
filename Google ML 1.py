from sklearn import tree 
features = [[140, 1], [130, 1], [150, 0], [170, 0]] # First key is the weight in grams, the second key is the texture. 0 for bumpy and 1 for smooth.
labels = [0, 0, 1, 1] # 0 for apples and 1 for oranges
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
weight = int(input("Vad väger frukten: "))
texture = input("Smooth eller bumpy? ")
if texture == "smooth":
    texture = 1
else:
    texture = 0
result = clf.predict([[weight, texture]])
if result == [1]:
    print("Datorn tror att det är en apelsin")
else:
    print("Datorn tror att det är ett äpple")