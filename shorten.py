import requests

# User Interface for Program
print("URL Shortener")
print("#############")
link = input("Enter URL to shorten : ")


# Setting Parameters and Sending POST request from the rel.ink API
url = 'https://rel.ink/api/links/'
data = {"url": link}
response = requests.post(url, data = data)

