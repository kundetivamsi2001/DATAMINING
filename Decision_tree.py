#step:0 importing all required libraries
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
#step:1 Load dataset
iris=load_iris()
#step:2 Divide dependent and independent(target variable) variables
X,y=iris.data,iris.target
#step:3 split train data and test data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)
#step 4:create an object for Decision tree
Dtree=tree.DecisionTreeClassifier()
#step 5: fit the data
Dtree=Dtree.fit(X_train,y_train)
y_pred=Dtree.predict(X_test)
#step 6:predict the test data during model
print("pred_val,"","","",act_val")
for i in range(len(X_test)):
    print(y_pred[i],y_test[i])
#step 7:finding the accuracy of the model
print("Accuracy of model is:",metrics.accuracy_score(y_test,y_pred))
#printing of text representation
r=export_text(Dtree,feature_names=iris["feature_names"])
print(r)
#printing of graph /tree representation
fig = plt.figure(figsize=(10,5))
tr= tree.plot_tree(Dtree, 
                   feature_names=iris.feature_names,  
                   class_names=iris.target_names,
                   filled=True)
fig.show()
      
