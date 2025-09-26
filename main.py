def main():
	output = get_book_text("books/frankenstein.txt")

	#import function to count words and characters from stat.py file
	from stats import get_num_words
	from stats import get_char

	num_words = get_num_words(output)
	num_char = get_char(output)
	print(f'Found {num_words} total words')
	print(num_char)

# create function to obtain book text
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents


main()

