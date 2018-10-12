'''
Created on Oct 12, 2018

@author: David Ngo
'''
import tensorflow as tf
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b
init = tf.global_variables_initializer() #initialize all variables
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(linear_model, {x: [1,2,3,4]})) #evaluate for several values of x
    
# to visualize the 