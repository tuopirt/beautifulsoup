from bs4 import BeautifulSoup
from bs4.tests import SoupTest


class TestBeautifulSoupIter(SoupTest):

    def test_iter_nested_tags_and_text(self):
        html = "<div><p>Hello</p><span>World</span></div>"
        soup = BeautifulSoup(html, "html.parser")
        nodes = list(soup)
        tag_names = [getattr(node, "name", None) for node in nodes]
        texts = [str(node) for node in nodes]
        assert "div" in tag_names
        assert "p" in tag_names
        assert "span" in tag_names
        assert "Hello" in texts
        assert "World" in texts

    def test_iter_empty_document(self):
        soup = BeautifulSoup("", "html.parser")
        assert list(soup) == []

    def test_iter_single_tag(self):
        soup = BeautifulSoup("<hr/>", "html.parser")
        hrs = [node for node in soup if getattr(node, "name", None) == "hr"]
        assert len(hrs) == 1

    def test_iter_xml_document(self):
        xml = "<root><item id='a'>One</item><item id='b'>Two</item></root>"
        soup = BeautifulSoup(xml, "xml")
        items = [node for node in soup if getattr(node, "name", None) == "item"]
        assert len(items) == 2

    def test_iter_yields_one_at_a_time(self):
        soup = BeautifulSoup("<div><p>First</p><p>Second</p></div>", "html.parser")
        iterator = iter(soup)
        first_node = next(iterator)
        assert first_node is not None
        assert not isinstance(iterator, list)