from bs4 import BeautifulSoup, SoupReplacer
from bs4.tests import SoupTest

class TestSoupReplacerMultiple(SoupTest):

    def test_multiple_replacements(self):
        html = "<div><b>One</b> and <b>Two</b></div>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)

        assert len(soup.find_all("b")) == 0
        assert len(soup.find_all("blockquote")) == 2