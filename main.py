def main():

    book_path = "books/frankenstein.txt"

    book_text = f_file_contents(book_path)

    num_words = count_words(book_text)
    print(f"Number of words in book: {num_words}")

    character_count = count_characters(book_text)
    print(f"Characters in book: {character_count}")

    print_report(book_path, num_words, character_count)

def f_file_contents(path):
    #Opening the file and reading it
    with open(path) as f:
        file_contents =f.read()

        return file_contents


def count_words(book_text):
    words = book_text.split()
    word_count = len(words)

    return word_count

def count_characters(book_text):
    character_stats = {}


    for c in book_text:
        lower_character = c.lower()
        if lower_character in character_stats:
            character_stats[lower_character] += 1
        else: character_stats[lower_character] = 1



    return character_stats


def print_report(book_path, word_count, character_dictionary):

    print(f"--- Begin report of {book_path}---")
    print(f"{word_count} words found in the document")

    for char in character_dictionary:
        print(f"The {char} character was found {character_dictionary[char]} times")

    print(f"--- End report ---")

    return None



main()