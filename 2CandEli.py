import csv
a=[]

print("The Given Training Data Set is :")

with open('ws.csv','r') as csvf:
	reader=csv.reader(csvf)
	for row in reader:
		a.append(row)
		print(row)
num_attr=len(a[0])-1

print("\nInitial value of Hypothesis is :")
s=['0']*num_attr
g=['?']*num_attr
print("The Most Specific Hypothesis is ",s)
print("The Most Generic Hypothesis is ",g)

for j in range(0,num_attr):
	s[j]=a[0][j]

print("\nThe Candidate Elimination Algorithm Hypothesis Version Space is")
temp=[]

for i in range(0,len(a)):
	if a[i][num_attr]=='Yes':
		for j in range(0,num_attr):
			if(a[i][j]!=s[j]):
				s[j]='?'

		for j in range(0,num_attr):
			for k in range(1,len(temp)):
				if temp[k][j]!='?' and temp[k][j]!=s[j]:
					del temp[k]
		print("For Training Example Number ",i+1," Specific Hypothesis is :",s)
		if len(temp)==0:
			print("For Training Example Number ",i+1," Generic Hypothesis is :",g)
		else:
			print("For Training Example Number ",i+1," the Generic Hypothesis is :",temp)


	if a[i][num_attr]=='No':
		for j in range(0,num_attr):
			if a[i][j]!=s[j] and s[j]!='?':
				g[j]=s[j]
				temp.append(g)
				g=['?']*num_attr
		print("For Training Example Number ",i+1," Specific Hypothesis is :",s)
		print("For Training Example Number ",i+1," Generic Hypothesis is :",temp)

print("Most Specific Hypothesis is :",s)
print("Most Generic Hypothesis is :",temp)
s.append(temp)
print("The Hypotheses is :",s)
