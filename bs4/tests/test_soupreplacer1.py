from bs4 import BeautifulSoup, SoupReplacer
from bs4.tests import SoupTest

class TestSoupReplacerSingle(SoupTest):

    def test_single_replacement(self):
        html = "<p>Hello <b>world</b>!</p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)

        assert soup.find("b") is None
        assert soup.find("blockquote") is not None
        assert soup.find("blockquote").string == "world"