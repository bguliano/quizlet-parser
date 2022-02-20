import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Flashcards:
    def __init__(self, url: str):
        session = HTMLSession()
        soup = BeautifulSoup(session.get(url).content, features='html.parser')
        self.title = soup.find('h1', {'class': 'UIHeading UIHeading--one'}).text
        self.author = soup.find('span', {'class': 'UserLink-username'}).text
        description = soup.find('div', {'class': 'SetPageHeader-description'})
        self.description = description.text if description is not None else description
        results = soup.findAll('span', {'class': re.compile('TermText notranslate')})
        self.flashcards = {}
        for i, result in enumerate(results):
            if i % 2 == 0:
                self.flashcards[self.parse_tag_text(result)] = self.parse_tag_text(results[i + 1])

    @staticmethod
    def parse_tag_text(tag) -> str:
        result = ''
        print(tag.contents)
        for item in tag.contents:
            if isinstance(item, str):
                result += item
            elif len(result) and result[-1] != '\n':
                result += '\n'
        return result

    def __getitem__(self, item: str) -> str:
        return self.flashcards[item]

    def __len__(self):
        return len(self.flashcards)
