'''
Created on Oct 12, 2018

@author: David Ngo
'''
#import tensorflow
import tensorflow as tf
#create constant a and b
a = tf.constant(12)
b = tf.constant(5)
x = tf.add(a,b)
with tf.Session() as sess:
    print(sess.run(x))
    
#write 