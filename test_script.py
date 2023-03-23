import requests,sys,re

import urllib
website = sys.argv[1]
subfile=open("subdoms","w")
dirfile = open("dirs",'w')
with open("subdomains_dictionary.bat",'r') as subdomains:
    for line in subdomains:
        line = re.sub("\s+","",line)
        sub = f"https://{line}.{website}"
        try:
                response = urllib.request.urlopen(sub)
        except urllib.error.URLError:
                continue
        if response.code == 200:
            subfile.write(sub+"\n")
with open("dirs_dictionary.bat",'r') as dictionaries:
      for line in dictionaries:
            line = re.sub("\s+","",line)
            directory = f"https://{website}/{line}"
            try:
                response = urllib.request.urlopen(directory)
            except urllib.error.URLError:
                    continue
            if response.code == 200:
                dirfile.write(directory+"\n")
response = requests.get(website)
html = response.text
files=open("files","w")
pattern = 'href="[^\s]*"'
links =re.findall(pattern,html)
for link in links:
    l = link.split("/") 
    if re.match(".*\.[^c]*[^o]*[^m]*",l[-1]):
        files.write(link + "\n")
   

