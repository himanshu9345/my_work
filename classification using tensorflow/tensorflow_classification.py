import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import tensorflow as tf
#https://jalammar.github.io/visual-interactive-guide-basics-neural-networks/
##load the data
#dataset has different attributes of the houses that are sold

data=pd.read_csv('data1.csv')
#now we will classify the house whether the house buy is good or bad on the
#basis of two attributes area and bothroom (you can take any two attributes which you feel it relevent)
#we will eliminate the unwanted coloums 
data=data.drop(["index","price","sq_price"],axis=1)
#get first 10 row of the dataset
data=data[0:10]
#let's assign random class to 10 row(good/bad) 1=good 2=bad
data.loc[:,("y1")]=[1,0,0,1,0,1,0,1,1,0]
#added another column for bad class y2 will be negation of y1
data .loc[:,("y2")]=data["y1"]==0 #outputs true/false
data.loc[:,("y2")]=data["y2"].astype(int) #conveting true/false to 1/0
#since we have to feed this data to tensorflow we have to convert it to Martix
input_x=data.loc[:,['area','bathrooms']].as_matrix()
input_y=data.loc[:,['y1','y2']].as_matrix()
#some parameters for training process 
lr=0.00001
no_epochs=2000
display_step=50
n_samples=input_y.size
#tenserflow variables
x=tf.placeholder(tf.float32,[None,2])
w=tf.Variable(tf.zeros([2,2]))
b=tf.Variable(tf.zeros([2]))
#
y_values=tf.add(tf.matmul(x,w),b)

y=tf.nn.softmax(y_values)#activation function

y_=tf.placeholder(tf.float32,[None,2])

error=tf.reduce_sum(tf.pow(y_-y,2))/(2*n_samples)

optimizer= tf.train.GradientDescentOptimizer(lr).minimize(error)#optimizer to optimize the cost
#initialising all tf variable
init =tf.initialize_all_variables()
sess=tf.Session()
sess.run(init)

for i in range(no_epochs):
	sess.run(optimizer,feed_dict={x:input_x,y_:input_y})


	if (i)%display_step==0:
		cc=sess.run(error,feed_dict={x:input_x,y_:input_y})
		print "training step:",'%d' %(i),"cost=","{:.9f}".format(cc)

print "Optimization finished"

training_cost=sess.run(error,feed_dict={x:input_x,y_:input_y})

print "Training cost=", training_cost, "W=", sess.run(w), "b=", sess.run(b), '\n'		
#prediction is less accurate we can add more hidden layers to imporve it.
print sess.run(y, feed_dict={x: input_x })
#		y1			y2
# [[ 0.87931693  0.12068304]
#  [ 0.81913888  0.18086113]
#  [ 0.9059546   0.09404533]
#  [ 0.79193395  0.20806599]
#  [ 0.94435722  0.0556428 ]
#  [ 0.86692518  0.13307482]
#  [ 0.80973089  0.19026911]
#  [ 0.79369158  0.20630841]
#  [ 0.7863369   0.2136631 ]
#  [ 0.80384922  0.19615081]]
#it classify all the houseas good buy