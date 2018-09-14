import tensorflow as tf 
a=tf.placeholder("float")
b=tf.placeholder("float")
x=tf.constant(2.0)
c=tf.multiply(a,b)
with tf.Session() as sess:
	for i in range(11):
		feed_dict={a:i,b:x}
		print(sess.run(c,feed_dict))
