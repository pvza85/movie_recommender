import xml.etree.ElementTree as ET

def convert_to_text(in_file):
	"""
	a function that gets subtitle xml file and extract it's text
	and save it to a file with same name but '.txt' extension
	"""

	# read xml file
	tree = ET.parse(in_file)
    root = tree.getroot()

    file_name = in_file.split('.')[0] #extract file name without .xml

    text = ''
    for parag in root.iter('s'):  # read each paragraph
        for word in parag.iter('w'): # read each word
            text += word.text
        text += '\n'
        
    try:
        f = open(file_name + '.txt', 'w')
        f.write(text.encode('utf8'))   # to avoid encoding error
    except Exception as e:
        print 'there is an error in file: ', in_file
        print e
    else:
        f.close()
