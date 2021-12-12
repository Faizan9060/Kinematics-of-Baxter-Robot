import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

data = pd.read_csv(r'/dataset/train.csv')
x = data.iloc[:,7:10].values
y = data.iloc[:,0:7].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.5,random_state = 1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test) 

ann = Sequential()


ann.add(Dense(units=3,activation='relu'))
ann.add(Dense(units=4,activation='relu'))
ann.add(Dense(units=5,activation='relu'))
ann.add(Dense(units=6,activation='relu'))

# ann.add(Dense(units=6,activation='relu'))
# ann.add(Dense(units=32,activation='relu'))
# ann.add(Dense(units=32,activation='relu'))

ann.add(Dense(units=7,activation='softmax'))  #sigmoid activation function


ann.compile(optimizer = 'rmsprop',loss = 'categorical_crossentropy',metrics = ["accuracy"])

ann.fit(x_train,y_train,batch_size = 30,epochs = 80)

_, accuracy = ann.evaluate(x, y, verbose=0)
print(accuracy)


#predicting test results

print(ann.predict(sc.transform([[0.5,-.6,.2]])))
y_pred = ann.predict(x_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))


#confusion matrix
from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)
print(cm)
print(accuracy_score(y_test,y_pred))
