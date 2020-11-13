from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd

links = ['https://www.expedia.com/Las-Vegas-Hotels-Wynn-Las-Vegas.h1184243.Hotel-Information', 
'https://www.expedia.com/Las-Vegas-Hotels-Mandalay-Bay-Resort-And-Casino.h203613.Hotel-Information']

hotel_name = []
source_name = ['expedia']*20
for link in links:
	page_url = link
	uClient = uReq(page_url)
	page_soup = soup(uClient.read(), "html.parser")
	uClient.close()
	#hotel = page_soup.find_all("div", {"class": "expandable-content description"})
	hotel = 'hotel'
	print(hotel)
	text = []
	
	containers = page_soup.findAll("p", {"class":"Review-comment-bodyText"})
	#print(containers)
	for container in containers:
		#container = container.text.strip().replace("<span> class=\"c-review__body\">", "")
		print(container)
		text.append(container)
		hotel_name.append(hotel)

print(text)
final = pd.DataFrame(list(zip(hotel_name, source_name, text)), columns=['Hotel', 'Source', 'Text'])
final.to_csv('reviews.csv', mode='a', index=False)
	#f.write(hotel + ", " + Source + ", " + text)