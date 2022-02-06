# quizlet-parser

A simple python script to extract useful information from a Quizlet link.

### To run:
1. ```pip install -r requirements.txt```
2. Execute [```main.py```](quizlet_parser/main.py)

### Requirements:
- ```beautifulsoup4```
- ```requests_html```

### Usage:
```>>> from quizlet_parser import Flashcards
>>> cards = Flashcards("https://quizlet.com/143490264/programming-python-flash-cards/")
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
