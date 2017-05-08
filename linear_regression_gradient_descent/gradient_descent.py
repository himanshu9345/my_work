import pandas as pd
from numpy import *
def compute_error(c,m,data):
	totalerror=0
	for i in range(0,len(data)):
		x = data[i,0]
		y = data[i,1]
		totalerror += (y - (m * x + c)) ** 2
	return totalerror/float(len(data))
def step_gradient(c,m,data,lr):
	c_gradient=0
	m_gradient=0
	N=float(len(data))
	for i in range(0,len(data)):
		x=data[i,0]
		y=data[i,1]
		c_gradient+= -(2/N)* (y-((m*x)+c)) #finding the gradient of c
		m_gradient+= -(2/N)* x * (y-((m*x)+c))#finding the gradient of m
	new_c=c - (lr * c_gradient)  #updting the values of c and m
	new_m=m - (lr * m_gradient)
	return [new_c,new_m]

def gradient_descent_runner(data,value_c,value_m,lr,num_iterations):
	c = value_c
	m = value_m
	for i in range(num_iterations):
		c,m = step_gradient(c,m,array(data),lr)	
	return [c,m]	
def main():
	data=pd.read_csv('data.csv',sep=",",header=None)
	#print data
	lr=0.0001
	value_m=0
	value_c=0
	num_iterations=1000
	[c,m]=gradient_descent_runner(data,value_c,value_m,lr,num_iterations)
	print c
	print m
if __name__ == '__main__':
	main()