import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession


class Flashcards(dict):
    def __init__(self, url: str):
        super(Flashcards, self).__init__()

        session = HTMLSession()
        soup = BeautifulSoup(session.get(url).content, features='html.parser')

        title = soup.find('h1', {'class': 'UIHeading UIHeading--one'})
        self.title = title.text if title is not None else title

        author = soup.find('span', {'class': 'UserLink-username'})
        self.author = author.text if author is not None else author

        description = soup.find('div', {'class': 'SetPageHeader-description'})
        self.description = description.text if description is not None else description

        results = soup.findAll('span', {'class': re.compile('TermText notranslate')})
        for i, result in enumerate(results):
            if i % 2 == 0:
                self[self._parse_tag_text(result)] = self._parse_tag_text(results[i + 1])

    @staticmethod
    def _parse_tag_text(tag) -> str:
        result = ''
        for item in tag.contents:
            if isinstance(item, str):
                result += item
            elif len(result) and result[-1] != '\n':
                result += '\n'
        return result
