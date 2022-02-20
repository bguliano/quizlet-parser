# quizlet-parser

A simple python script to extract useful information from a Quizlet link.

### To run:
1. ```pip install -r requirements.txt```
2. Execute [```main.py```](quizlet_parser/main.py)

### Requirements:
- [```beautifulsoup4```](https://pypi.org/project/beautifulsoup4/)
- [```requests-html```](https://pypi.org/project/requests-html/)

### Usage:
```
>>> from quizlet_parser import Flashcards
>>> cards = Flashcards("https://quizlet.com/667086814/python-builtins-flash-cards/")
>>> cards.author
'bguliano'
>>> cards.title
'Python builtins'
>>> cards.description
'Sample description'
>>> len(cards)
5
>>> cards.flashcards
{'abs()': 'Returns the absolute value of a number', 'bool()': 'Converts a value to a boolean', 'dir()': 'Returns a list of attributes for an object', 'len()': 'Returns the length of a object', 'type()': 'Return the type of an object'}
>>> cards['bool()']
'Converts a value to a boolean'
```

### Example:
This code takes a search term and searches google for 5 Quizlet pages that best match the search term. Then, it prints out term-definition pairs that best match the original search term. Requires the [```googlesearch-python```](https://pypi.org/project/googlesearch-python/) PyPI package.
```
from difflib import SequenceMatcher
from googlesearch import search
from quizlet_parser.main import Flashcards


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


if __name__ == '__main__':
    search_term = input('Search term: ').strip()
    google_search_term = 'site:quizlet.com ' + search_term
    urls = search(google_search_term, 4)  # search returns 1 more URL than specified, so passing in 4 returns 5 URLs
    matches = {}

    for url in urls:
        cards = Flashcards(url)
        for term, definition in cards.flashcards.items():
            if similarity(term, search_term) >= 0.5:
                matches[term] = definition

    print()
    for key, value in matches.items():
        print(f'{key}:\n{value}\n')
```
