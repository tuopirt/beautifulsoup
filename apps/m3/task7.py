import os
import sys
from bs4 import BeautifulSoup, SoupReplacer

def main():
    if len(sys.argv) < 2:
        print("Usage: python task7.py <path_to_html_xml_file>")
        return

    file_path = sys.argv[1]
    parser = "xml" if file_path.lower().endswith(".xml") else "html.parser"

    replacer = SoupReplacer(
        attrs_xformer=lambda tag: {**tag.attrs, "class": "test"} if tag.name == "p" else tag.attrs
    )

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), parser, replacer=replacer)

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output = f"{file_name}_task7_output.html"
    
    with open(output, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"Successfully processed {file_path} using SoupReplacer -> saved to {output}")

if __name__ == "__main__":
    main()