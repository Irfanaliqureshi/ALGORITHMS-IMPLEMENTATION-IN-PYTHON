def TowerOfHanoi(n , beg, end, aux):
	if n==1:
		print ("Move disk 1 from BEG",beg,"to END",end)
		return
	TowerOfHanoi(n-1, beg, aux, end)
	print ("Move disk",n,"from BEG",beg,"to END",end)
	TowerOfHanoi(n-1, aux, end, beg)
		
# input to run code
#NOTE: Be careful while changing the value of n becuase it can hang our system because of recurisve Algorithm
n = 4
TowerOfHanoi(n,'A','B','C') 
# A, C, B are the name of rods
