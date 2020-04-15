from sklearn import svm

def find_patterns(n,p):
	"""
		divides protien sequence p string into patterns of length n
		output = 2 matrices = X and Y for train.data
		and only X for test.data
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
		# print(seq)
		# print(seq_dict)
		X.append(seq_dict)
	

		if (ord(p[i:i+n][half_n]) >=97):
			Y.append(1)
		else:
			Y.append(-1)
	# print(X)
	# print(Y)
	return X,Y
	# print(sequences)
	for p in sequences:
		if (len(p)!=7):
			print("error",p)
def find_patterns_test(n,p):
	"""
		divides protien sequence p string into patterns of length n
		output = 2 matrices = X and Y for train.data
		and only X for test.data
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
		# print(seq)
		# print(seq_dict)
		X.append(seq_dict)
		
	return X
	# print(sequences)
X_train=[]
Y_train=[]
file=open('train.data','r')
data=file.readlines()
n=7
for i in range(1,len(data)):
	s=''
	count_x_insert=(n-1)//2
	s+='X'*count_x_insert
	s+=data[i][8:-1]
	s+='X'*count_x_insert
	# print(s)
	X,Y=find_patterns(n,s)
	X_train.extend(X)
	Y_train.extend(Y)




# print(X_train)
# print(Y_train)

# print(len(X_train),len(Y_train))

"""
now apply five fold verification: append 4 outputs to X and 
leave 1 for testing purpose.
"""

clf = svm.SVC(gamma ='scale')
clf.fit(X_train, Y_train)


# print(X)
# print(Y)
# print(len(X),len(Y))


file=open('test1.txt','r')
data=file.readlines()
s=''	
count_x_insert=(n-1)//2
s+='X'*count_x_insert
for i in range(1,len(data)):
	s+=data[i][6]

s+='X'*count_x_insert

X_test=find_patterns_test(n,s)
# print(X)
# print(len(X))
# print(s)			#s=test_protien_seq
out=clf.predict(X_test)
print(out)


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
	# if (out[ind]==1):
	# 	print("1 found")
	ofile.write(l)
	ind=ind+1
