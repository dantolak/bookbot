def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters=get_num_characters(text)
    # print(f"{num_words} words found in the document")
    # print(f"{num_characters} words found in the document")
    get_report(book_path, num_words, num_characters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_characters(text):
    lowered_string = text.lower()
    chars={}
    for character in lowered_string:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    
    return chars

def get_report(book_path, words, characters):
    print (f"--- Begin report of {book_path} ---")
    print (f"{words} words found in document")
    sorted_dict = dict(sorted(characters.items(),key=lambda item: item[1], reverse=True))
    for char in sorted_dict:
        if char.isalpha():
            print (f"The {char} character was found {sorted_dict[char]} times")
    print ("--- End report ---")


main()