from urllib.request import urlopen


url = 'http://alura-site-scraping.herokuapp.com/index.php'
response = urlopen(url)
html = response.read()
html

html = html.decode('utf-8')
def trata_html(input):
    return " ".join(input.split()).replace('> <', '><')

html = trata_html(html)
html