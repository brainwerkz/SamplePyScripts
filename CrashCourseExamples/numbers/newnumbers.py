#!/usr/local/bin/python3

squares = []
for value in range(1,100):
	#square = value**3
	squares.append(value**3)
	
print(squares)
#print('The length of the list is:\n\t')
#print len(squares)

#print min(squares)

#print max(squares)

#print sum(squares)

squares = [value for value in range(1,100)]
print(squares)

print min(squares)

print max(squares)

print sum(squares)


odd_numbers = list(range(1,50,2))
print(odd_numbers)
