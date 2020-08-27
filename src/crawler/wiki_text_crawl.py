from os.path import exists
import requests
from bs4 import BeautifulSoup


def get_content(title):
    filename = f"{title}.html"
    if exists(filename):
        text = open(filename).read()
        return text
    url = f"https://vi.wikipedia.org/wiki/{title}"

    page = requests.get(url)
    text = page.content.decode("utf-8")
    f = open(filename, "w")
    f.write(text)
    return text


title = "Hồ_Hoàn_Kiếm"
text = get_content(title)
soup = BeautifulSoup(text, "html.parser")
parser_output = soup.find("div", class_="mw-parser-output")
paragraphs = parser_output.find_all("p")

# parse article
filename = f"{title}.txt"
with open(filename, "w") as f:
    f.write("")

f = open(filename, "a")

for p in paragraphs:
    for child in p.children:
        pass
        # child

    f.write(p.text)
    f.write("\n")

f.close()

print("Done")
