# A = U S V^t
import numpy as np;
from numpy import linalg as LA
import math

# Read data from csv
csv = "testData2"
data = np.genfromtxt(csv,delimiter = ',');
print data;

# Take the transpose of data 
# Data is assumed to be in form 
# columns = attributes
# rows = trials
# so take transpose 
transpose = np.transpose(data);
aat = np.dot(data,transpose);
ata = np.dot(transpose,data);

#Get eigen values and eigen vectors of AAt
eigenValues1,eigenVectors1 = LA.eigh(aat);
print "eigenVectors of AAt";
print eigenVectors1;
print "eigenvalues of AAt"
print eigenValues1;
#Get eigen values and eigen vectors  of AtA
eigenValues2,eigenVectors2 = LA.eigh(ata);
print "eigenVectors of AtA";
print eigenVectors2;
print "eigenvalues of AtA"
print eigenValues2;



# Sort Eigen values in decreasing order
idx = eigenValues1.argsort()[::-1]   
eigenValues1 = eigenValues1[idx]
eigenVectors1 = eigenVectors1[:,idx]
print "Eigen values of aat: Sorted"
print eigenValues1;
print "Eigen vectors of aat: Sorted"
print eigenVectors1;

# Sort Eigen values in decreasing order
idx = eigenValues2.argsort()[::-1]   
eigenValues2 = eigenValues2[idx]
eigenVectors2 = eigenVectors2[:,idx]
print "Eigen values of ata: Sorted"
print eigenValues2;
print "Eigen vectors of ata: Sorted" 
print eigenVectors2;

#u in the equation 

u = eigenVectors1;

# v ^ t in the equation 
vtranspose = np.transpose(eigenVectors2);

# Create the S diagonal Matrix 
n,m = data.shape;
S = np.zeros([n,m]);
length = eigenValues1.size;
for i in range(0,length):
	if eigenValues1[i] < 0:
		S[i][i] = 0
	else:
		S[i][i] = math.sqrt(eigenValues1[i]);
	

print "u"
print u
print "S"
print S
print "vtranspose"
print vtranspose;

result = np.dot(u, S);
result = np.dot(result, vtranspose);
print "result "
print result 
	







