boolarray = np.isclose(eigenValues1, eigenValues2, 1e-05, 1e-08);
j =0
for i in range(0, boolarray.size):
	if boolarray[i] == true:
		commonEigenValues[j] = eigenValues[i]
		j = j+1; 	

