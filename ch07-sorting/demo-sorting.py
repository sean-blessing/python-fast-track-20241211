fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon",
 "Kiwi", "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG",
 "pear", "banana", "Tamarind", "persimmon", "elderberry" , "peach",
 "BLUEberry", "lychee", "grape"]

print(f'fruit: {fruit}')
fruit.sort()
print(f'sorted fruit: {fruit}')
fruit = sorted(fruit)
print(f'sorted fruit: {fruit}')

def ignore_case(item):
    return item.lower()

sorted_fruit = sorted(fruit, key=ignore_case)
print(f'sorted again: {sorted_fruit}')

books= [
 "A Study in Scarlet",
 "The Sign of the Four",
 "The Hound of the Baskervilles",
 "The Valley of Fear",
 "The Adventures of Sherlock Holmes",
 "The Memoirs of Sherlock Holmes",
 "The Return of Sherlock Holmes",
 "His Last Bow",
 "The Case-Book of Sherlock Holmes"
 ]

def print_books(books):
    for book in books:
        print(book)
    print('--------------')

print_books(books)
books = sorted(books)
print_books(books)

# article is an ignored word: a, an, the
def strip_article(title):
    title = title.lower()
    for article in 'a ', 'an ', 'the ':
        if title.startswith(article):
            title = title.removeprefix(article)
            break
    return title

print('\nSorted Books:')
for book in sorted(books, key=strip_article):
    print(book)