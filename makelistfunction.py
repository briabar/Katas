import bleach
'''Write a function in Python that takes a list of strings and returns a
single string that is an HTML unordered list (<ul>...</ul>) of those strings.
You should include a brief explanation of your code. Then, what would you have
to consider if the original list was provided by user input?'''

def MakeList(list_of_strings):
	answer_array = []
	answer = ''
	for string in list_of_strings:
		answer_array.append('<ul>')
		answer_array.append(bleach.clean(string))
		answer_array.append('/ul>')
		answer_array.append(' ')
	answer = answer.join(answer_array)
	return answer


print MakeList(["foot",'pizza','gym bag'])
'''The reason I've built this function using only array appends and joins
because I wanted to limit the number of objects held in memory.  Using a
concatenation function would generate a new string object each time an
assignment occurs.  While this is fine for a smaller operation, supposing we
had millions of lines of items in our array list_of_string this would
drastically and needlessly increase the time of said operation.
	If the string data was provided by user input we would need to pass it
through a good sanitization library, like bleach.
'''
