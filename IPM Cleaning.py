loc = "RBML"
year = "2017"
#months = ['10', '12']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

m = """
Beetle, Cigarette 																															
Beetle, Drugstore																															
Beetle, Furniture																															
Beetle, Ground																															
Beetle, Hide																															
Beetle, Odd								1														1									
Beetle, Powder post																															
Beetle, Spider																															
Beetle, Unid.																															
Book Louse	4		2	5	1									1					2	3	1								1		1
Centipede																					1	10									
Cockroach, American																															
Cockroach, German																															
Cockroach, Oriental																															
Cricket																															
Moth, Clothes																															
Silverfish														1																	
Spider																							1								
Spider- Black Widow																															
Spider- Brown Recluse																															
Spring Tail																															
Termite																															
Wasp, Yellow Jacket																															
Other																																																																							
"""

mat =  [l.split('\t') for l in m.split('\n') if len(l) > 0]

mt = list(map(list, zip(*mat)))
labels = list(mt)[0]
mt.pop(0)

for i, l in enumerate(list(mt)):
	month = months[i]
	print ("\n".join(["	".join([loc, label, year, month, count]) for label, count in zip(labels, l)]))
	# print '\n'.join("\t".join(zip(labels, l)))
