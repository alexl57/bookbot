import sys
from stats import ( count_words, 
                   count_characters,
                   sort_by_frequency,
)

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        return f.read()

def main(path):
    text = get_book_text(path)
    num_of_words = count_words(text)
    counts_of_characters = count_characters(text)
    character_frequencies = sort_by_frequency(counts_of_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in character_frequencies:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

main(path)