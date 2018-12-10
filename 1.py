import csv

a=[]

print("The Given Training Data Set is :")

with open('ws.csv','r') as csvf: # with open will open as well as close the file, csvf is the holder or pointer
	reader=csv.reader(csvf)
	for row in reader:
		a.append(row) # all the entries of the excel sheet are stored here
		print(row)

num_attr=len(a[0])-1 #length of each entry in excel file(number of values in each row)

print("Initial value of Hypothesis is :")
hypo=['0']*num_attr	#Initial hypothesis which is all null
print(hypo)

for j in range(0,num_attr): # hypo need to be calculated, initially it is first entry in excel file,(summer is hypo[0] and so on)
	hypo[j]=a[0][j]

print("Maximally Specific Hypothesis:")

for i in range(0,len(a)): #range includes 0 and excludes len(a)
	if a[i][num_attr]=='Yes': #Modify th hypo only for those that have positive response
		for j in range(0,num_attr):
			if a[i][j]!=hypo[j]: #if different, then update with a question mark
				hypo[j]='?'
	print("For Training Example Number ",i," Hypothesis is :",hypo)

print("Most Specific Hypothesis is :",hypo)
