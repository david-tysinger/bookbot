def main():
	filepath = "books/frankenstein.txt"
	output = get_book_text(filepath)

	#import function to count words and characters from stat.py file
	from stats import get_num_words
	from stats import get_char
	from stats import sort_on

	num_words = get_num_words(output)
	num_char = get_char(output)
	sorted_list = sort_on(num_char)

	print("============ BOOKBOT ============")
	print(f'Analyzing book found at {filepath}...')
	print("----------- Word Count ----------")
	print(f'Found {num_words} total words')
	print("--------- Character Count -------")

	for i in sorted_list:
		if not i["char"].isalpha():
			continue
		print(f"{i['char']}: {i['num']}")

	print("============= END ===============")

# create function to obtain book text
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents


main()

