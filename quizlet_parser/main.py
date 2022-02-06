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
        card_data = soup.findAll('span', {'class': re.compile('TermText notranslate')})
        self.flashcards = {}
        for i, result in enumerate(card_data):
            if i % 2 == 0:
                self.flashcards[result.text] = card_data[i + 1].text

    def __getitem__(self, item: str) -> str:
        return self.flashcards[item]

    def __len__(self):
        return len(self.flashcards)
