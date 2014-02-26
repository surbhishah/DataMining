import sys
import numpy as np
from numpy import linalg as LA
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.mlab import PCA
# Iris data csv file 
csv = "iris/iris.data";
# Numpy array of iris data
data = np.genfromtxt(csv, delimiter = ',');
n,m = data.shape;
# Deleting last column which is not a number ..It represents the class
data = np.delete(data,m-1 ,1);

# Transpose of data
#data = np.transpose(data)
"""mean = data.mean(axis=0);
data = data - mean;

print data
#data /= data.std(data, axis=1)
#print mean

	

"""




res = PCA(data)
print "weights of input vectors" , res.Y
#print "Variances" , res.fracs;



"""
a = np.matrix('1 2 1; 6 -1 0; -1 -2 -1');
print "A"
print a
mean  = a.mean(axis=1);
print "mean";
print mean;
b = a- mean ;
print "b";
print b;
#meanzero = a - mean[:, np.newaxis]
#print meanzero




b = np.transpose(a);
print "B"
print b;
print "A.B"
c = np.dot(a,b);
print c;
w,v = LA.eigh(c);
print "Eigen values:"
print w
print "Eigen vectors:"
print v
"""
