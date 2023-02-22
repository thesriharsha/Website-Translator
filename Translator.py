import os
from bs4 import BeautifulSoup
from googletrans import Translator

path = "Classcentral"
count=0

# Collecting all the files with extensions .html 
# and.htm and saving the names in a html_files

html_files=[]
for x in os.listdir(path) :
    if x.endswith(".html") or x.endswith('.htm'):
        html_files.append(x)

#Creating googletrans object
translator = Translator()


# For each file in html_files, 
# the text gets extracted and Translated into Hindi using
# the translator object and finally gets Replaced

for html_file in html_files:
    
    count+=1
    #Displays the number of file that is being processed
    print(count)
    with open("Classcentral/"+html_file,"r",encoding="utf-8") as index:
        html=index.read()

    soup= BeautifulSoup(html,"html.parser")
    tags = ['script','style','img']

    for tag in soup.find_all():
        if tag.name not in tags:
            try:
                old_text= tag.text.strip()
                tag.string.replace_with(translator.translate(old_text,dest="hi").text)
                
            except:
                pass
    

    with open(html_file,"wb") as f_output:
        f_output.write(soup.prettify("utf-8")) 