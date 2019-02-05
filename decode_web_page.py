import requests
import bs4

strLink = 'https://www.nytimes.com'

response = requests.get( strLink )
html = response.text

soup = bs4.BeautifulSoup( html, 'html.parser' )

strContent = soup.find( id="site-content")

for div in strContent.find('div') :
	if None != div:
		print(div.get_text())