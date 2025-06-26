# stats.py

def count_words(book: str) -> int:
    '''takes the text from the book as a string and returns the total word count
    '''
    words = book.split()
    return len(words)

def count_characters(book: str):
    '''Takes the text from the book as a string,
    returns the number of times each character,
    (including symbols and spaces), appears in the string.
    The count is case-insensitive.
    '''
    frequency_dict: dict[str, int] = {}
    for c in book:
        c = c.lower()
        frequency_dict[c] = frequency_dict.get(c, 0) + 1
        
    return frequency_dict
    
def sort_by_frequency(freq_dict: dict[str, int]) -> list[dict[str, int]]:
    '''each dictionary has two key-value pairs:
    e.g. {"char": "b", "num": 4868}
    the list is sorted from greatest to least by count
    '''
    result = [{"char": k, "num": v} for k, v in freq_dict.items()]
    result.sort(reverse=True, key=lambda d: d["num"])
    return result