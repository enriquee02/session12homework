import requests
import string

def get_unique_words(book_url):
    book = requests.get(book_url)
    text = book.text.lower()  # Convert to lowercase to avoid case variations

    # Define punctuation to remove
    punctuation_remove = ",.!?:;"
    punctuation_space = "'\()[]=-+_"

    for character in punctuation_remove:
        text = text.replace(character, "")
    for character in punctuation_space:
        text = text.replace(character, "")

    words = text.split()
    unique_words = set(words)  # Using a set to count unique words only

    return len(unique_words)


# URLs of two books from Project Gutenberg
book1_url = 'https://www.gutenberg.org/cache/epub/166/pg166-images.html'  # Example: Dracula by Bram Stoker
book2_url = 'https://www.gutenberg.org/cache/epub/37106/pg37106-images.html'  # Example: Frankenstein by Mary Shelley

# Get unique word counts for both books
unique_words_book1 = get_unique_words(book1_url)
unique_words_book2 = get_unique_words(book2_url)

# Print results
print(f"Book 1 Unique Words: {unique_words_book1}")
print(f"Book 2 Unique Words: {unique_words_book2}")

if unique_words_book1 > unique_words_book2:
    print("Book 1's author used more unique words.")
elif unique_words_book2 > unique_words_book1:
    print("Book 2's author used more unique words.")
else:
    print("Both authors used the same number of unique words.")