text = """María tenía un perrito su pelo era blanco como la nieve y dondequiera que fuera María, el perrito seguramente iría detraz de Maria"""

def leer_xml(aLine):
	print( "Se encontro: ", aLine)

def parse_text(theText, aPattern, function):
	for line in theText.split('\n'):
		if aPattern in line:
			function(line)

parse_text(text,'Maria',leer_xml)
