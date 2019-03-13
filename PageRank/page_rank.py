import numpy as np

#Take matrix size as input
n=int(input("Enter Total No, Pages ->"))
print("Enter 1 If Page i Has Link To Page j")
#initialise nxn matrix 
mat=np.zeros((n,n))

#input each row at a time,with each element separated by a space
for i in range(n):
   mat[i]=input("For Page "+str(i)+" To Others => ").split(" ")
print(mat)  

#outbound Calucalation
