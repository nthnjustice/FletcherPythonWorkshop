import urllib.request

url = 'http://data.worldbank.org/indicator/NY.GDP.MKTP.CD'

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)
