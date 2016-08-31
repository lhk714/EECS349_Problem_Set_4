import csv, random
c = csv.writer(open('prob_ec.csv', 'wb'))
header = []
for i in range(2):
	header.append('X' + str(i+1))
header.append('Y')
c.writerow(header)
for i in range(1000):
	row = []
	row.append(random.randint(0,1))
	row.append(random.randint(0,1))
	if row[0] == row[1]:
		row.append(0)
	else: 
		row.append(1)
	c.writerow(row)