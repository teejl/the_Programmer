# Thomas Lockwood
# 4/10/2018
# Learning from Data by Yaser


'''
Purpose: The purpose of this assignment is to create the PLA algorithm.
The main input should be a csv file. (I will generate one if need be).
The out put should be the algorithm weights printed to a csv file.
'''

#Import Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Hello World")

def generate_data(N=1000, outpath=False, outdelimiter = ',',inpath=False, indelimiter = ','):
#input: N - number of rows
#output: z - (N, 3) matrix with classified points
    if inpath:
        z = np.genfromtxt(inpath, delimiter=indelimiter)
    else:
        # generate a 2-D random array
        x = np.random.randint(0, 100, size=(N,2)) #print(x)
        #x = x/100
        
        # generate the solution set
        f = lambda x1, x2: x1*4 - x2*2 - 1 < 0 #=> w1 = 4, w2 = -2, w0 = -1 (b > 2a - 1/2)
        y = np.fromiter((f(a,b) for a,b in x), x.dtype, count=len(x))     #print(np.count_nonzero(y))
        #print(y)
        z = np.column_stack(np.append(np.column_stack(x),np.column_stack(y), axis=0))     #print (z, z.shape)

        # save as filepath if user selects
        if outpath:
            np.savetxt(outpath, z, '%5.2f', delimiter=outdelimiter)
	

    return (z)

def plot_data(z=generate_data(), w = np.array([[1],[4],[-2]]), solution=False):
#input: 3-d array [x1, x2, y] for the 3 column vectors
#output: scatter plot
	w0 = w[0][0]
	w1 = w[1][0]
	w2 = w[2][0]
	x1 = np.column_stack(z)[0]
	x2 = np.column_stack(z)[1]
	y = np.column_stack(z)[2]
	ys = np.where(y==1, True, False)
	no = np.where(y==1, False, True)
	yc = np.where(y==1, 'R', 'G')
	#print(ys)
	#print(y.shape, ys.shape, yc.shape)

    # plot the scatterplot
	plt.scatter(x1[ys], x2[ys], marker = 'o', color = yc[ys])
	plt.scatter(x1[no], x2[no], marker = '+', color = yc[no])

    # plot line
	if solution:
		l = np.linspace(0, (100-(w2/w0))*(w2/-w1))
		plt.plot(l,(-w1/w2)*l+(w0/w2))

    # plot solution with points
	plt.show()

def PLA(z=generate_data() , ulimit=1000, mapitt=50):
#input: array for the 3 column vectors
#output: weight array


	# Add the row of 1'
	x0 = np.ones(shape = (z.shape[0], 1))
	X = np.append(x0, z[:,:-1], axis=1) # X Matrix
	Y = np.array([z[:,-1]]).T # Actual Solution set
	Y = np.where(Y==0, -1, 1)
	
	# Shortcut; start with least squares coefficients
	w = np.dot(np.linalg.pinv(X),Y)
	
	#print(z.shape)
	#print(X.shape, Y.shape, w.shape)
	
	# 	Start loop here
	for i in range(ulimit):
		h = np.dot(X,w) #Find h 
		hx = np.where(h<0, -1, 1) #Find h(x) with weights
		Err = Y * hx
		ErrCount = np.unique((Err==1), return_counts=True)[1]
		
		#print(w)
		#print(np.linalg.pinv(X).shape)
		#print(Y.shape)
		#print(np.dot(
		
		if np.any(Err==-1):
			# Plot every 10 iterations
			if i%(mapitt) == 0:
				print("The following solution has an accuracy of " + str(ErrCount[1]/X.shape[0]*100) + "%")
				plot_data(z=z, w=w, solution = True)
				
			Err_Arr = (Err==-1).reshape(X.shape[0])
			delta = np.array([(Y[Err_Arr][0]*X[Err_Arr][0])]).T
			w = w + delta
				
		#print(w)
		#print(w, np.array([(Y[Err_Arr][0]*X[Err_Arr][0])]).T)
		#print(Err.shape, X.shape, (Err==-1).reshape(X.shape[0]).shape)
		#print(Y[Err==-1][0], X[(Err == -1), :])
		
		#Plot Results when finished
		else:
			print("The following solution has an accuracy of " + str(100) + "%")
			plot_data(z=z, w=w, solution = True)
			print(i, w)
			return(w)
			
	# Plot and sign off
	print("The following solution has an accuracy of " + str(ErrCount[1]/X.shape[0]*100) + "%")
	plot_data(z=z, w=w, solution = True)
	print(w)
	return(w)


#plot_data(generate_data(100), 0, -1, 1, solution=True)   
#generate_data(N=1000,outpath="Generated_Data.csv")
PLA(z=generate_data(inpath="Generated_Data.csv"))
