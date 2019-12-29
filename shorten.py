import requests

# User Interface for Program
print("URL Shortener")
print("#############")
link = input("Enter URL to shorten : ")


# Setting Parameters and Sending POST request from the rel.ink API
url = 'https://rel.ink/api/links/'
data = {"url": link}
response = requests.post(url, data = data)

# Validating Response and Printing the Shorten URL
if response:
	id = response.json()["hashid"]
	print("Shorten URL : https://rel.ink/" + id)
else:
	print("Please Enter a valid URL")