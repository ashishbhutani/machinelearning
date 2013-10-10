
import numpy as np
import random

def cal_avg_iter():
	total_iterations = 0
	total_error_point = 0
	error_point = 0
	total_prob_error = 0.0
	total_res = 0.0
	for count in range(1000):
		#print "#run: ",count
		l_x1= random.uniform(-1.0,1.0)
		l_y1= random.uniform(-1.0,1.0)
		l_x2= random.uniform(-1.0,1.0)
		l_y2= random.uniform(-1.0,1.0)
		slope   =  (l_y2-l_y1)/(l_x2-l_x1)
		y_icept =  (l_y2-slope*l_x2)
		#print "line cood: ",l_x1," ",l_y1," ",l_x2," ",l_y2," slope: ",slope," y_icept: ",y_icept
		n = 10
		#(x1, x2) are the co-ordinates, NOT (x,y)
		#y is the output/label i.e. -1/1
		x1 = []
		for i in range(n):
			x1.append(random.uniform(-1.0,1.0))
		x2 = []
		for i in range(n):
			x2.append(random.uniform(-1.0,1.0))	
		outputs = []
		for i in range(n):
			#print "random x1: ",x1[i]," random x2: ",x2[i]
			func_val = slope*x1[i]+y_icept
			#print "func_val: ",func_val
			if (x2[i] > func_val):
				outputs.append(1)
			else:
				outputs.append(-1)
			#print "output found: ",outputs[i]	
		w0 = w1 = w2 = 0
		iterations = 0
		done = False
		while not done:
			iterations += 1
			total_iterations += 1
			#print "PLA #iteration: ",iterations
			#print "#Total iteration: ",total_iterations
			error_found = False
			misclassifieds = []
			error_point = 0
			for i in range(n):
				weight = w0+w1*x1[i]+w2*x2[i]
				#print "weight: ",weight
				sign = 1
				if (weight<0):
					sign = -1
				#print "sign found: ",sign," and corresponding outputs was: ",outputs[i]	
				if (sign != outputs[i]):
					misclassifieds.append(i)
					#print "doesnt match"
					error_found = True
					error_point += 1
			prob_error = error_point/(n*1.0)
			#print "error_point: ", error_point
			#print "prob_error: ",prob_error
			total_prob_error += prob_error
			if error_found:		
				rmp_idx = random.randint(0,len(misclassifieds)-1)
				total_error_point += 1
				rmp = misclassifieds[rmp_idx]
				#print "rmp = ",rmp
				weight = w0+w1*x1[rmp]+w2*x2[rmp]
				sign = 1
				if weight>=0:
					sign = -1		
				w0 += 1*(outputs[rmp])
				w1 += x1[rmp]*(outputs[rmp])
				w2 += x2[rmp]*(outputs[rmp])
				#print "new weights: ",w0," ",w1," ",w2
			else:
				#print "converged in this iteration"
				done = True
		#############################
		# Code for mean probability #
		#############################	
		L = 100000
		tmp1= []
		for i in range(L):
			tmp1.append(random.uniform(-1.0,1.0))
		tmp2 = []
		for i in range(L):
			tmp2.append(random.uniform(-1.0,1.0))	
		tmps = []
		for i in range(L):
			func_val = slope*tmp1[i]+y_icept
			if (tmp2[i] > func_val):
				tmps.append(1)
			else:
				tmps.append(-1)
		wrong = 0
		for i in range(L):
			weight = w0+w1*tmp1[i]+w2*tmp2[i]			
			sign = 1
			if (weight <=0):
				sign = -1
			if (sign != tmps[i]):
				wrong += 1
				
		res = wrong/(L * 1.0)
		#print "res: ",res
		total_res += res				
	
	print "#Total iteration: ",total_iterations
	total_res = total_res/(1000*1.0)
	print "total_res: ", total_res
	#per = total_error_point/(n*1000*1.0)
	#print "total_error_pont: ",total_error_point
	#print "per: ",per
	#print "total_prob_error: ",total_prob_error
	
	
if __name__ == "__main__":
	cal_avg_iter()
    			
