# Part-3:
# Functions & Classes

SoupReplacer(...):
bs4/filter.py, around line 335, class SoupReplacer(ElementFilter)

BeautifulSoup(...):
bs4/__init__.py, around line 133, class BeautifulSoup(Tag)

handle_starttag(...):
bs4/__init__.py, around line 1040, def handle_starttag()

handle_endtag(...):
bs4/__init__.py, around line 1080, def handle_endtag()



# M3 Summary
Expanded `SoupReplacer` to support functional transformers (`name_xformer`, `attrs_xformer`, `xformer`) alongside the legacy positional arguments. Updated BeautifulSoup's parsing lifecycle (`handle_starttag` and `handle_endtag`) to execute transformers on the fly during tree construction. Wrote 6 unit tests under `bs4/tests/` and implemented Milestone 3 Task 7 under `apps/m3/task7.py`.