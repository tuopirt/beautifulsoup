import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("Usage: python apps/m2/task3.py <path_to_html_xml_file>")
        return

    file_path = sys.argv[1]
    parser = "xml" if file_path.lower().endswith(".xml") else "html.parser"

    # Parse all tags (True)
    only_tags = SoupStrainer(True)

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), parser, parse_only=only_tags)

    for tag in soup.find_all(True):
        print(f"<{tag.name}>")

if __name__ == "__main__":
    main()