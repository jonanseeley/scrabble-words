from bs4 import BeautifulSoup as bs
from unidecode import unidecode
import json
from string import ascii_lowercase as lowercase

def parse_page(letter):
    with open(f"pages/{letter}.htm") as f:
        soup = bs(f, features="html.parser")

    word_lists = soup.find_all(attrs={"class": "wres_ul"})
    words = []
    for i in range(len(word_lists)):
        words.extend([thing.contents[0] for thing in word_lists[i].find_all("a")])
    print(f"There are {len(words)} words that begin with {letter}")
    return words

words = []
for letter in lowercase:
    words.extend(parse_page(letter))

words.sort()
with open("wordlist.txt", "w") as f:
    for word in words:
        f.write(word + "\n")
'''
buttons = document.getElementsByClassName("sbl_load_all")
for (let button of buttons){
    button.click()
}
'''
