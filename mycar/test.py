import tensorflow as tf

print("GPUs Available: ", tf.config.list_physical_devices('GPU'))

with tf.device('/GPU:0'):
	a=tf.random.normal([1000, 1000])

print("Done")
