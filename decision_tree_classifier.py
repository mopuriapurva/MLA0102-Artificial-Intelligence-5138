import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X_train, y_train)
tree_rules = export_text(clf, feature_names=list(X.columns))
print("Decision Tree Structure:\n")
print(tree_rules)
print("\nPredictions for new instances:")
new_instances = X_test.head()
predictions = clf.predict(new_instances)
for i, instance in enumerate(new_instances.values):
    print(f"Instance {instance} -> Predicted class: {predictions[i]}")
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy on Test Data: {accuracy:.2f}")
