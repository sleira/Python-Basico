import requests
from lxml import etree

r = requests.get('https://es.wikipedia.org/wiki/Sharon')
print(r.url)
print(r.text)

html = etree.HTML(r.text)
resultado = etree.tostring(html)
print(resultado)

pelc = html.xpath('//a[@title]/text()')
nomPelc = html.xpath('//div[@class="mw-parser-output"]//table//tbody//td//text()')
footer = html.xpath('//div[@class="action-list"]//p/text()')

print(pelc)
print(nomPelc)
print(footer)

