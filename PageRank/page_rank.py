import numpy as np
N=int(input("Enter The No. Of Pages => "))
print("Enter 1 Page i having a link to Page j......")
links=[]
d=0.85
for i in range(0,N):
	L=[]
	for j in range(0,N):
		L.append(int(input("Page "+str(i+1)+" To Page "+str(j+1)+" => ")))
		links.append(L)

outboundL = np.zeros((N,),dtype=int)
for i in range(0,N):
	for j in range(0,N):
		if(links[i][j]==1):
			outboundL[i]+=1

M=np.zeros((N,N))
for i in range(0,N):
	for j in range(0,N):
		if(links[j][i]==1):
			M[i][j]=1/outboundL[j]

col=np.ones((N,1))

r=np.full((N,1),1/N)
