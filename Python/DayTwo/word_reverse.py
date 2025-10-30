s ="abcdefd"

def reverse_until_d(s):
	index = s.find('d')
	if index == -1:
		return [s]
    	else:
        	first = s[:index + 1][::-1]  
        	second = s[index + 1:]       
        return [first, second]
print(reverse_until_d(s))



	
def find_largest(data):
    largest = data[0][0]

    for group in data:
        for number in group:
            if number > largest:
                largest = number

    return [largest]  



