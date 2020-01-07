import requests 

print(requests.__version__)

var =requests.get("https://raw.githubusercontent.com/Vanessa0122/404Lab1/master/script.py")

print(var.content)
