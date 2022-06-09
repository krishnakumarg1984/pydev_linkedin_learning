# HTML Parser Module
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr:", attr)

    def handle_endtag(self, tag):
        print("End tag: ", tag)

    def handle_comment(self, data):
        print("Comment: ", data)

    def handle_data(self, data):
        print("Data: ", data)


parser = MyHTMLParser()
parser.feed(
    "<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>"
)
print()

# user_input = input("Put in HTML Code")
# parser.feed(user_input)
# print()

# htmlFile = open("sampleHTML.html", "r")
s = ""
with open("sampleHTML.html", "r", encoding="utf-8") as htmlFile:
    for line in htmlFile:
        s += line
parser.feed(s)
