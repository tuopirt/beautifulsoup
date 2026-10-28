import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("Usage: python apps/m2/task2.py <path_to_html_xml_file>")
        return

    file_path = sys.argv[1]
    parser = "xml" if file_path.lower().endswith(".xml") else "html.parser"

    only_links = SoupStrainer('a')

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), parser, parse_only=only_links)

    for link in soup.find_all('a'):
        print(link.get('href'))

if __name__ == "__main__":
    main()