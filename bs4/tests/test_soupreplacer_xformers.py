from bs4 import BeautifulSoup, SoupReplacer
from bs4.tests import SoupTest

class TestSoupReplacerXformers(SoupTest):

    def test_name_xformer_conditional(self):
        html = "<div><b>Bold</b><i>Italic</i></div>"
        replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        assert soup.find("b") is None
        assert soup.find("blockquote") is not None

    def test_name_xformer_uppercase(self):
        html = "<p>Hello</p>"
        replacer = SoupReplacer(name_xformer=lambda tag: tag.name.upper())
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        assert soup.find("P") is not None

    def test_attrs_xformer_add_attribute(self):
        html = "<div>Content</div>"
        def add_attr(tag):
            attrs = dict(tag.attrs)
            attrs["class"] = "highlighted"
            return attrs
        replacer = SoupReplacer(attrs_xformer=add_attr)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        div = soup.find("div")
        assert div["class"] == "highlighted"

    def test_attrs_xformer_remove_attribute(self):
        html = '<div class="old-class" id="main">Test</div>'
        def remove_class(tag):
            attrs = dict(tag.attrs)
            attrs.pop("class", None)
            return attrs
        replacer = SoupReplacer(attrs_xformer=remove_class)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        div = soup.find("div")
        assert "class" not in div.attrs
        assert div["id"] == "main"

    def test_side_effect_xformer(self):
        html = '<p class="remove-me">Paragraph</p>'
        def remove_class_attr(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]
        replacer = SoupReplacer(xformer=remove_class_attr)
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        p = soup.find("p")
        assert "class" not in p.attrs
        assert p.string == "Paragraph"

    def test_combined_xformers(self):
        html = "<b>Text</b>"
        replacer = SoupReplacer(
            name_xformer=lambda tag: "strong" if tag.name == "b" else tag.name,
            attrs_xformer=lambda tag: {"role": "bold-text"}
        )
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        strong = soup.find("strong")
        assert strong is not None
        assert strong["role"] == "bold-text"