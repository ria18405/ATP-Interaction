from sklearn import svm

def find_patterns(n,p):
	"""
		divides training set protien sequence p string into patterns of length n
		output = 2 matrices = X and Y for train.data
	"""
	X=[]
	sequences=[]
	Y=[]

	half_n=(n-1)//2
	for i in range(len(p)-(n)+1):
		seq=p[i:i+n]
		sequences.append(seq)
		seq_dict=[]
		for j in range(n):
			dict={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0,'X':0}
			
			if (seq[j] in dict ):
				dict[seq[j]]=1 
			elif (chr(ord(seq[j])-32) in dict):
				dict[chr(ord(seq[j])-32)]=1
			seq_dict.extend(list(dict.values()))

		X.append(seq_dict)
	
	"""
	Small alphabet indicates ATP interacting residues
	ATP interacting = +1
	Non ATP interacting = -1

	"""
		if (ord(p[i:i+n][half_n]) >=97):
			Y.append(1)
		else:
			Y.append(-1)

	return X,Y

def find_patterns_test(n,p):
	"""
		divides protien sequence p string into patterns of length n
		output = 1 matrix = X for test.data
	"""
	X=[]
	sequences=[]

	half_n=(n-1)//2
	for i in range(len(p)-(n)+1):
		seq=p[i:i+n]
		sequences.append(seq)
		seq_dict=[]
		for j in range(n):
			dict={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0,'X':0}
			if (seq[j] in dict):
				dict[seq[j]]=1 
			seq_dict.extend(list(dict.values()))

		X.append(seq_dict)
		
	return X


#-------------TRAINING------------------
X_train=[]
Y_train=[]
file=open('train.data','r')
data=file.readlines()
n=7			#n=pattern length
for i in range(1,len(data)):
	
	"""
	Addition of 'XXX..XX' at the beginning and end of protien sequences
	(n-1)/2 number of X are added in both directions
	Output : s->train-protien_sequence
	"""
	s=''
	count_x_insert=(n-1)//2
	s+='X'*count_x_insert
	s+=data[i][8:-1]
	s+='X'*count_x_insert		


	X,Y=find_patterns(n,s)
	X_train.extend(X)
	Y_train.extend(Y)


"""
[Optional]now apply five fold verification: append 4 outputs to X and 
leave 1 for testing purpose.
"""

clf = svm.SVC(gamma ='scale')
clf.fit(X_train, Y_train)

#-------------------TESTING-----------

file=open('test1.txt','r')
data=file.readlines()

"""
Addition of 'XXX..XX' at the beginning and end of protien sequences
(n-1)/2 number of X are added in both directions
Output : s-test-protien_sequence
"""

s=''	
count_x_insert=(n-1)//2
s+='X'*count_x_insert
for i in range(1,len(data)):
	s+=data[i][6]

s+='X'*count_x_insert		


X_test=find_patterns_test(n,s)

#making predictions
out=clf.predict(X_test)



"""
Writing predictions output in a file output.txt
with the respective Protien IDs
"""
ofile = open("output.txt","w")
s="ID,Lable\n"
ofile.write(s)
ind=0
file_test = open("test1.txt","r")
data = file_test.readlines()
data = data[1:]

for line in data:
	s = list(line.split(","))
	l = s[0]+","+str(out[ind])+'\n'

	ofile.write(l)
	ind=ind+1
