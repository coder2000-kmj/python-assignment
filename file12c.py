data = data2 = "" 
with open('f1.txt') as fp: 
	data = fp.read() 
with open('f2.txt') as fp: 
	data2 = fp.read() 
data += "\n"
data += data2 

with open ('f3.txt', 'w') as fp: 
	fp.write(data) 
