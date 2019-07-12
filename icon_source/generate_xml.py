import os
import csv

appfilter = open("../app/src/main/res/xml/appfilter.xml", "w")
appfilter.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
appfilter.write("<resources>\n")
with open("components.csv", newline="") as csvfile:
	reader = csv.reader(csvfile, delimiter=",", quotechar="\"")
	for row in reader:
		appfilter.write("<item component=\"ComponentInfo{" + row[0] + "}\" drawable=\"" + row[1] + "\"/>\n")
		
appfilter.write("</resources>")		
appfilter.close()

drawable = open("../app/src/main/res/xml/drawable.xml", "w")
drawable.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
drawable.write("<resources>\n")
drawable.write("<category title=\"Icons\"/>\n")

dir = "../app/src/main/res/drawable-nodpi/"
for i in os.listdir(dir):
        if not i in ("ic_splash_screen.png"):
                drawable.write("<item drawable=\"" + os.path.splitext(i)[0] + "\"/>\n")

drawable.write("</resources>")        
drawable.close()
