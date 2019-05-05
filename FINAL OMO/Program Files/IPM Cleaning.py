loc = "Archives Rm 146"
year = "2018"
#months = ['10', '12']
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

m = """
Bees, Honey	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Beetle, Cabinet	0	0	0	0	0	0	0	0	1	0	0	0	0	0
Beetle, Carpet 	0	0	0	0	0	0	0	0	1	0	0	0	1	0
Beetle, Cigarette 	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Beetle, Drugstore	0	0	0	0	0	0	0	1	0	0	0	5	0	0
Beetle, Furniture	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Beetle, Ground	0	1	1	0	0	0	1	0	0	0	0	0	0	0
Beetle, Hide	0	0	0	0	0	0	0	0	0	0	1	0	0	0
Beetle, Minute Brown Scavenger	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Beetle, Odd	0	0	1	0	0	2	0	0	0	0	0	0	0	0
Beetle, Powder post	0	1	0	0	0	0	0	0	0	0	0	0	1	0
Beetle, Spider	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Beetle, Unid.	0	1	1	0	0	0	2	1	0	0	2	0	2	0
Book Louse	1	0	0	3	1	1	0	0	0	0	0	1	0	0
Centipede	0	1	1	0	0	0	0	0	0	0	0	0	2	0
Cockroach, American	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Cockroach, German	0	0	0	0	0	2	0	0	0	0	1	0	0	0
Cockroach, Oriental	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Cricket	0	0	0	0	0	1	5	2	1	1	1	1	5	1
Moth, Clothes	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Silverfish	0	0	0	0	0	1	0	0	0	0	0	0	0	0
Spider	2	2	0	1	2	5	3	1	5	4	3	7	4	0
Spider- Black Widow	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Spider- Brown Recluse	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Spring Tail	14	11	13	19	9	6	4	1	1	10	1	2	1	0
Termite	0	0	0	0	0	0	0	0	0	0	0	0	0	0
Wasp, Yellow Jacket	0	0	0	0	0	0	0	0	0	0	0	0	0	0
	6	12	28	4	5	14	12	5	2	11	6	13	27	0"""

mat =  [l.split('\t') for l in m.split('\n') if len(l) > 0]

mt = list(map(list, zip(*mat)))
labels = list(mt)[0]
mt.pop(0)

for i, l in enumerate(list(mt)):
	month = months[i]
	print ("\n".join(["	".join([loc, label, year, month, count]) for label, count in zip(labels, l)]))
	# print '\n'.join("\t".join(zip(labels, l)))
