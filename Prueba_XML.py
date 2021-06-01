import xml.etree.ElementTree as Et

xml_tree = Et.parse('products.xml')
products = xml_tree.getroot()
print(products.tag)
for product in products:
	print(' ',product.tag, ' name=',product.get('name'))
for product_item in product:
	print(' ',product_item.tag, '=',product_item.text)

print('----------')
for code in products.iter('code'):
	print(code.text)

print('construct xml file')
users = Et.Element('users')
for i in range(1, 5):
	user = Et.SubElement(users, 'user')
	user.set('name', "User " + str(i))
	user_item = Et.SubElement(user, 'age')
	user_item.text = str(i * 3)
	user_item2 = Et.SubElement(user, 'id')
	user_item2.text = "1203" + str(i)
	print('write into xml file')
