#save_path = "/Users/mali/Documents/MNIST/mnist_demo/CNN_mnsit"

#import modules
import sys
import tensorflow as tf
from PIL import Image, ImageFilter

def predictint(imvalue):


    # Define the model (same as when creating the model file)
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    def weight_variable(shape):
      initial = tf.truncated_normal(shape, stddev=0.1)
      return tf.Variable(initial)

    def bias_variable(shape):
      initial = tf.constant(0.1, shape=shape)
      return tf.Variable(initial)

    def conv2d(x, W):
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(x):
      return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    x_image = tf.reshape(x, [-1,28,28,1])
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    init_op = tf.initialize_all_variables()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, "/Users/mali/Documents/MNIST/mnist_demo/CNN_mnsit/cnn_model.ckpt")
        print ("Model restored.")

        prediction=tf.argmax(y_conv,1)
        return prediction.eval(feed_dict={x: [imvalue],keep_prob: 1.0}, session=sess)


def getdata(argv):
    test_image = Image.open(argv)
    data = list(test_image.getdata())
    return data
global pNum


def main(argv):
    """
    Main function.
    """
    print argv
    #  global pNum
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    imvalue = getdata(argv)
    print imvalue
    predint = predictint(imvalue)
    #print (predint[0]) #first value in list

    #return predint

    pNum = predint[0]
    anwerlist = ['anw0.png','anw1.png','anw2.png','anw3.png','anw4.png','anw5.png','anw6.png','anw7.png','anw8.png','anw9.png']
    anw = Image.open(anwerlist[pNum])
    anw.show()
    return predint
#if __name__ == "__main__":
#    #main(sys.argv[1])
#    main()


'''
def getdata(argv):
    test_image = Image.open(argv)
    data = list(test_image.getdata())
    return data
def main(argv):
    """
    Main function.
    """
    pSum = len(sys.argv) - 1
    pic = sys.argv[ -pSum: ]

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(len(pic)):
        print(pic[i])
        imvalue = getdata(pic[i])
        predint = predictint(imvalue)
        print (predint[0]) #first value in list
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if __name__ == "__main__":
    main(sys.argv)
'''
