from numpy import exp,array,random,dot

class NeuralNetwork():
	def __init__(self):
		random.seed(1)
		self.synaptic_weights=2*random.random((3,1))-1

	def sigmoid(self,x): #activation function ,convet it to probability 
		return 1/(1+exp(-x))

	def __sigmoid_derivative(self,x):#to caluate derivative of sigmoid or slope
		return x*(1-x)	

	def train(self,training_input,training_output,num_iterations):
		for iteration in range(num_iterations):
			output=self.predict(training_input) #passing the traing set through the network
			error=training_output - output #findng error b/w predicted and actul output
			##back propagation##
			adjustment=dot(training_input.T,error*self.__sigmoid_derivative(output))
			self.synaptic_weights+=adjustment
			####################
	
	def predict(self,inputs):
		return self.sigmoid(dot(inputs,self.synaptic_weights))	#getting the dot product of weight and inputs
			



if __name__ == '__main__':
	nn=NeuralNetwork()
	print nn.synaptic_weights
	training_input=array([[0,0,0],[1,1,1],[1,0,1],[0,1,1]])
	training_output=array([[1,0,0,0]]).T
	nn.train(training_input,training_output,100000)
	print "new weight"
	print nn.synaptic_weights
	print "predicting"
	print nn.predict(array([0,0,1]))
	