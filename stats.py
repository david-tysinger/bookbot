#create function to count words
def get_num_words(book):
	words = book.split()
	return len(words)

#create function to count characters
def get_char(book):
    char = {}
    for c in book:
        lower_case = c.lower()
        if lower_case in char:
            char[lower_case] += 1
        else:
            char[lower_case] = 1
    return char 

	