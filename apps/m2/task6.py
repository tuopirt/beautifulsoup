import os
import sys

# Use the modified bs4 package from this Milestone-2 repository when this
# file is run directly (for example: python apps/m2/task6.py input.html).
MILESTONE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if MILESTONE_ROOT not in sys.path:
    sys.path.insert(0, MILESTONE_ROOT)

from bs4 import BeautifulSoup, SoupReplacer

def main():
    if len(sys.argv) < 2:
        print("Usage: python task6.py <path_to_html_xml_file>")
        return

    file_path = sys.argv[1]
    parser = "xml" if file_path.lower().endswith(".xml") else "html.parser"

    b_to_blockquote = SoupReplacer("b", "blockquote")

    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), parser, replacer=b_to_blockquote)

    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output = f"{file_name}_task6_output.html"
    
    with open(output, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    main()
