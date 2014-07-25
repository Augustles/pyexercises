
f = open('xx.txt','w')
for i in range(1, 10):
  for j in range(1, i + 1):
      if i != j:
        print i,'*',j,'=',i*j
		
f.write("i,'*',j,'=',i*j")