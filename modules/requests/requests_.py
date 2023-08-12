import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response, end="\n\n")
print(response.status_code, end="\n\n")
print(response.headers, end="\n\n")
print(response.text)  # content
