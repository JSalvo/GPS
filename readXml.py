import sys
import xml.etree.ElementTree as ET
tree = ET.parse('risalita.gpx')
root = tree.getroot()


fileoutput = open("./risulato.txt", "w")

print root.tag

for child in root:
	print child.tag
	if child.tag == "{http://www.topografix.com/GPX/1/1}trk":
		trk = child		
		for trkchild in trk:
			print trkchild
			if trkchild.tag == "{http://www.topografix.com/GPX/1/1}trkseg":
				trkseg = trkchild
				for trksegchild in trkseg:
					if trksegchild.tag == "{http://www.topografix.com/GPX/1/1}trkpt":
						trkpt = trksegchild
						for trkptchild in trkpt:
							if trkptchild.tag == "{http://www.topografix.com/GPX/1/1}ele":
								fileoutput.write(trkptchild.text)
								fileoutput.write(",")

							if trkptchild.tag == "{http://www.topografix.com/GPX/1/1}time":
								fileoutput.write(trkptchild.text)
								fileoutput.write("\n")

fileoutput.close()
								
