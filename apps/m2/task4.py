import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("Usage: python apps/m2/task4.py <path_to_html_xml_file>")
        return

    file_path = sys.argv[1]
    parser = "xml" if file_path.lower().endswith(".xml") else "html.parser"

    # Only parse tags that have an id attribute
    only_with_ids = SoupStrainer(id=True)

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), parser, parse_only=only_with_ids)

    for tag in soup.find_all(id=True):
        print(f"Tag: <{tag.name}> | ID: {tag.get('id')}")

if __name__ == "__main__":
    main()