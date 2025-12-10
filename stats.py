def word_count(book_text):
    return len(book_text.split())

def char_count(book_str):
    character_count = {}
    for char in book_str:
        char = char.lower()
        if char in character_count:
            character_count[char] +=1 
        else:
            character_count[char] = 1 
    return character_count

def sort_on(item):
    return item["num"]


def sort_chars(char_dict):
    sorted_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read() 