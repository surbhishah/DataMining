import numpy as np;
from numpy import linalg as LA


# Read data from csv
csv = "iris/iris.data"
data = np.genfromtxt(csv,delimiter = ',');
#print data;


# Take the transpose of data 
# Data is assumed to be in form 
# columns = attributes
# rows = trials
# so take transpose 
data = np.transpose(data);


# Delete the last row of the data, it consists of class
n,m = data.shape;
data = np.delete(data, n-1,0);


# Transform the data to get zero mean 
meanMatrix = np.mean(data,axis=1);
print meanMatrix;
n,m = data.shape;
for i in range(n):
	for j in range(m):
		data[i][j] -= meanMatrix[i];


# Transform by dividing by standard deviation
data /= data.std(axis=0);
		
		
# Get the transpose of data 
transpose = np.transpose(data);


# Get dot product of data and its transpose to get covariance matrix times n-1
dotProduct = np.dot(data,transpose);


# Get Eigen Values and Eigen vectors
eigenValues,eigenVectors = LA.eigh(dotProduct);


# Sort Eigen values in decreasing order
idx = eigenValues.argsort()[::-1]   
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print "Eigen values:"
print eigenValues;
print "Eigen vectors:"
print eigenVectors;


# Matrix of principal components is transpose of matrix of eigen vectors
P = np.transpose(eigenVectors);
print "P";
print P;

# Transform Y = PX to get new data
y = np.dot(P, data);
print "Y";

# Take transpose for convenience in viewing data
y = np.transpose(y);
print y;




