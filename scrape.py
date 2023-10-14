import requests
from random import randint

# url1 = "https://www.gutenberg.org/cache/epub/1/pg1.txt"
# booknum =str(randint(1,69000))
# url = "https://www.gutenberg.org/cache/epub/"+booknum+"/pg"+booknum+".txt"
# print(url)
# print("reqesting the book... ")
# r = requests.get(url,allow_redirects=True)
# print(r.status_code)


def main():
    i = int(input('how many books do you want to install?'))
    for _ in range(i):
        downloadBook()

def generateUrl():
   booknum =str(randint(1,69000))
   url = "https://www.gutenberg.org/cache/epub/"+booknum+"/pg"+booknum+".txt" 
   return booknum,url

def downloadBook():
    bookInfo = generateUrl()
    url = bookInfo[1]
    booknum = bookInfo[0]
    print(url)
    print("requesting")
    r = requests.get(url,allow_redirects=True)

    if r.status_code == 200:
        book_content = r.text
        title = extractTitle(book_content)+".txt"
        with open(title, "wb") as file:
            file.write(r.content)
            print("successfully downloaded")
    elif r.status_code ==404:
        print("book doesnt exist, retrying")
        downloadBook()

def extractTitle(book_content):
    # This function should extract the title from the book's content
    # For example, you can search for a line that contains "Title:" and extract the title
    # Modify this part based on the format of the title in the book's content.
    title_line = None
    for line in book_content.splitlines():
        if "Title:" in line:
            title_line = line
            print (title_line)
            break
    
    if title_line:
        return title_line.replace("Title:", "").strip()
    else:
        return "Unknown Title"

if __name__ == "__main__":
    main()