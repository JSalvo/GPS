from datetime import datetime

tempo1 = "2017-03-15T19:40:52.000Z"

tempo2 = "2017-03-15T18:57:07.000Z"


tempo2obj  = datetime.strptime(tempo1, "%Y-%m-%dT%H:%M:%S.%fZ")
tempo1obj  = datetime.strptime(tempo2, "%Y-%m-%dT%H:%M:%S.%fZ")

print tempo1obj
print tempo2obj 

print (tempo2obj - tempo1obj).total_seconds()

dislivelloOutput = open("filedislivello.csv", "w")

fileToOpen = open("./risulato.txt", "r")

linee = fileToOpen.readlines()

for i in range(1, len(linee)):
	r1 = linee[i-1].split(",")
	r1[0] = float(r1[0])
	r1[1] = datetime.strptime(r1[1], "%Y-%m-%dT%H:%M:%S.%fZ\n")

	r2 = linee[i].split(",")
	r2[0] = float(r2[0])
	r2[1] = datetime.strptime(r2[1], "%Y-%m-%dT%H:%M:%S.%fZ\n")


	dislivello = r2[0] - r1[0]
	deltat = (r2[1] - r1[1]).total_seconds()*1.0


	minutoprima = int(r1[1].strftime('%M')) + int(r1[1].strftime('%H'))*60
	minutoadesso = int(r2[1].strftime('%M')) + int(r2[1].strftime('%H'))*60

	if (minutoadesso / 5 > minutoprima / 5):
		dislivelloOutput.write(r2[1].strftime('%H:%M:%S'))
	dislivelloOutput.write(',')	
	dislivelloOutput.write(str(int((dislivello / deltat)*3600)))
	dislivelloOutput.write("\n")

