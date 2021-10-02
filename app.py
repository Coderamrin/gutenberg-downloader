import requests
from lxml import html 

# variables
link = "https://www.gutenberg.org/ebooks/61085"


resp = requests.get(url=link) 
tree = html.fromstring(html=resp
.content)  
 
titleAndAuthor = tree.xpath("//h1/text()")[0]
url = tree.xpath("//table[@class='files']/tr[@class='even'][2]/@about")[0]  

bookName = "{}.epub".format(titleAndAuthor) 

resp = requests.get(url=url) 
open(bookName, 'wb').write(resp.content)  
