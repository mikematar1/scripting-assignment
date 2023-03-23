import requests,sys,re
website = sys.argv[1]
response = requests.get(website)
html = response.text
print(html)
pattern = 'href="[^\s]*"'
func = lambda x : x[6:-1]
links =re.findall(pattern,html)
print(links)
# for x in links:
#     print(x)
links = map(func,links)
links = list(set(links))
# print(links)
# for x in links:
#     print(x)
directory=open("dirs","w") 
sub=open("subdoms","w")
files=open("files","w")
for link in links:
    l = link.split("/")
    print(link)
    if re.search("^https?:\/\/(?:[^\/]+\.)*com(\/)?$",link):
        sub.write(link + "\n")
    elif re.match(".*\.[^c]*[^o]*[^m]*",l[-1]):
        files.write(link + "\n")
    else:
        directory.write(link+"\n")
