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
#print meanMatrix;
n,m = data.shape;
for i in range(n):
	for j in range(m):
		data[i][j] -= meanMatrix[i];
		
		
# Get the transpose of data 
transpose = np.transpose(data);


# Get dot product of data and its transpose to get covariance matrix times n-1
covMatrix = np.cov(data);
print "covMatrix";
print covMatrix;

#Get eigen values and eigen vectors 
eigenValues,eigenVectors = LA.eigh(covMatrix);
print "eigenVectors";
print eigenVectors;
print "eigenvalues"
print eigenValues;


# Sort Eigen values in decreasing order
idx = eigenValues.argsort()[::-1]   
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]
print "Eigen values: Sorted"
print eigenValues;
print "Eigen vectors: Sorted"
print eigenVectors;


#Compute the transformed matrix 
# Matrix of principal components is transpose of matrix of eigen vectors ie (eig1 eig2 eig3)
P = np.transpose(eigenVectors);
print "Principal Components";
print P;

# Transform Y = PX to get new data
y = np.dot(P, data);
print "Y";

# Take transpose for convenience in viewing data
y = np.transpose(y);
np.savetxt("output.npy",y);
#print y;

