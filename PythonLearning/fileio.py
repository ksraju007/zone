#Writing a file
with open('test.txt','w') as f:
	f.write('Line 1\nLine 2\nLine 3\n')
	f.close()

#Reading a file, line by line
with open('test.txt','r') as f:
	for line in f:
		print line,
	f.close()
	
