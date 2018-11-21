import sys
import urllib.request

if len(sys.argv) != 3:
	print("py skriptinimi.py sisendfail.txt valjundfail.txt")
	sys.exit()
	
sisendFail = open(str(sys.argv[1]), "r")
valjundFail = open(str(sys.argv[2]), "w")
failiRead = sisendFail.readlines()

for rida in failiRead:
	if rida != "\n":
		try:
			reaSisu = rida.strip("\n").split(",")
			aadress = reaSisu[0]
			tekstMidaotsida = reaSisu[1]
			f = urllib.request.urlopen(aadress)
			vastus = str(f.read())		
			valjundFail.write(aadress + "," + tekstMidaotsida + ",")
			if tekstMidaotsida in vastus:
				valjundFail.write("JAH\n")
			else:
				valjundFail.write("EI\n")
		except Exception as e:
			valjundFail.write(aadress + "," + tekstMidaotsida + "," + "EI\n")
			sisendFail.close()
			valjundFail.close()
			sys.exit()
			
print("KÕIK ON TIMM")				
sisendFail.close()
valjundFail.close()
