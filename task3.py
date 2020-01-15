# list_ = input('Enter a list of elements: ').split('')
# shift = int(input('Enter positive or negative number: '))
# print(list(list_[-shift:] + list_[:-shift]))

cipher = input("Enter a list of integer with space: ").split()
move = int(input("Enter a step: "))

for i in range(len(cipher)):
	cipher[i] = int(cipher[i])
print(cipher)

if move > 0:
	for i in range(move):
		n = cipher.pop(0)
		cipher.append(n)
else:
	for i in range(abs(move)):
		n = cipher.pop()
		cipher.insert(0, n)
print (cipher)