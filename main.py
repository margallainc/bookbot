import sys
from stats import word_count, char_count, sort_on, sort_chars, get_book_text
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

 
def main():
    book_text = get_book_text(book_path)
    count = word_count(book_text)
    character_count = char_count(book_text)
    sorted_characters = sort_chars(character_count)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ===============")

main()
