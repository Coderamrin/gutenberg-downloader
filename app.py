import requests
import os
import urllib.request
from lxml import html
 
 
# check if folder exist if not create a folder
def createFolder (folderName) :
    isExist = os.path.exists(folderName)

    if not isExist:
        os.mkdir(folderName)

def removeSpecialCharFromStr(str):
    remove_characters = ["/", "/", ":", "<", ">", "|", "\""]
    for character in remove_characters:
        str = str.replace(character, "")
    return str

# scrape single book 
def downloadSingleBook(link):
    resp = requests.get(url=link)
    tree = html.fromstring(html=resp
                           .content)

    bookInfo = tree.xpath("//h1/text()")[0]
    url = tree.xpath("//table[@class='files']/tr[@class='even'][2]/@about")[0]

    validString = removeSpecialCharFromStr(bookInfo
    )
    fileName = "{}.epub".format(validString)
    resp = requests.get(url=url)
    open(fileName, 'wb').write(resp.content)

# from the author page get single book link
# open that link
# download the book from single book page

def downloadAuthorsList(url):
    resp = requests.get(url=url)
    tree = html.fromstring(html=resp
                           .content)
    authorInfo = tree.xpath("//h1/text()")[0]  
    allBooksUrl = tree.xpath("//li[@class='booklink']/a/@href")

    for bookUrl in allBooksUrl:
        formattedBookUrl = "https://www.gutenberg.org{}".format(bookUrl)
        weburl = urllib.request.urlopen(formattedBookUrl)
        
        booksTree = html.fromstring(html=weburl.read())

        bookInfo = booksTree.xpath(
            "//h1/text()")[0]
        validStr = removeSpecialCharFromStr(bookInfo) 
        downloadLink = booksTree.xpath("//table[@class='files']/tr[3]/@about")[0]

        formattedBookName = "{}.epub".format(validStr)   
 
        createFolder(authorInfo) 
        folderName = authorInfo
        completeFileName = os.path.join(folderName, formattedBookName) 

        book = requests.get(url=downloadLink)
        open(completeFileName, 'wb').write(book.content) 


# downloadAuthorsList("")
downloadSingleBook("https://www.gutenberg.org/ebooks/66465")

# ask if single book or author list then call the funcions accordingly 
