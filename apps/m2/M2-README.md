# Part-2:
# Functions
BeautifulSoup(...):
bs4/__init__.py, around line 133, class BeautifulSoup(Tag)

SoupStrainer(...):
bs4/filter.py, around line 313, class SoupStrainer(ElementFilter)

.find(...):
bs4/element.py, around line 2684, def find()

.find_all(...):
bs4/element.py, around line 2715, def find_all()

.find_parent(...):
bs4/element.py, around line 992, def find_parent()

.get(...):
bs4/element.py, around line 2160, def get()

.prettify(...):
bs4/element.py, around line 2601, def prettify()

.clear(...):
bs4/element.py, around line 2093, def clear(self, decompose: bool = False) -> None


# (additionals I am finding for myself so I can understand the tool better)

## Arguments:
parse_only:
bs4/__init__.py, around line 182

## Attributes:
.name:
bs4/element.py, around line 1740

.attrs:
bs4/element.py, around line 1743

.sourceline:
bs4/element.py, around line 1744

.sourcepos:
bs4/element.py, around line 1745



# Part 3
Added SoupReplacer(og_tag, alt_tag) to replace matching tags during parsing. Updated BeautifulSoup to accept the optional replacer argument and 2 tests.