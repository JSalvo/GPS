import math

def degreesMinutesSecondsToDegree(d, m, s):
	return d + m/60.0 + s/3600.0

def degreesMinutesSecondsToRadians(d, m, s):
	return degreesToRadians(degreesMinutesSecondsToDegree(d, m, s))

def degreesToRadians(d):
	tmp = d % 360
	return (2*math.pi*d) / 360.0

def gpsToVector(d1, p1, s1, d2, p2, s2):
	a1 = degreesMinutesSecondsToRadians(d1, p1, s1)
	a2 = degreesMinutesSecondsToRadians(d2, p2, s2)

	r1 = 6371000
	r2 = math.cos(a1) * r1

	z = math.sin(a1) * r1
	y = math.sin(a2) * r2
	x = math.cos(a2) * r2

	return [x, y, z]

def vectorDifference(v1, v2):
	result = [0, 0, 0]
	for i in range(0, len(v1)):
		result[i] = v1[i] - v2[i]

	return result

def dotProduct(v1, v2):
	result = 0 
	for i in range(0, len(v1)):
		result += v1[i] * v2[i] 

	return result

def vectorLength(v):
	return(math.sqrt(dotProduct(v, v)))


def distance(v1, v2):
	return(vectorLength(vectorDifference(v1, v2)))

v1 = gpsToVector(45, 57, 30.91, 10, 18, 36.61)
v2 = gpsToVector(45, 57, 31.47, 10, 18, 41.45)
v3 = gpsToVector(45, 57, 29.48, 10, 18, 42.10)
v4 = gpsToVector(45, 57, 28.98, 10, 18, 37.11)

print(v1)
print(v2)
print(v3)
print(v4)

print(distance(v1, v2))
print(distance(v2, v3))
print(distance(v3, v4))
print(distance(v4, v1))



from xml.etree import ElementTree as ET


xml = """
<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE xgdresponse SYSTEM 'xgdresponse.dtd'>
<xgdresponse version='1.0'>
  <transid>2771709</transid>
  <errorcode>0</errorcode>
  <response>
    <result>
      <element>666</element>
      <errorcode>0</errorcode>
      <value>SOMETHING IMPORTANT!</value>
	<value>Qualcosa di importante 2!</value>
    </result>
  </response>
</xgdresponse>
""".strip()


value = ET.fromstring(xml).find('response/result/value')
print value.text
if value != None:
	print 'Found value:', value.text

value = ET.fromstring(xml).find('response/result/value')
print value.text
if value != None:
	print 'Found value:', value.text
