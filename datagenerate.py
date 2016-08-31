import csv, random
c = csv.writer(open('prob4.csv', 'wb'))
header = []
for i in range(30):
	header.append('X' + str(i+1))
header.append('Y')
c.writerow(header)
for i in range(1000):
	row = []
	row.append(random.uniform(1,10)) #the first attribute is a random float number and ranges from 1 to 10
	row.append(random.uniform(0,1)) #the second attribute is a random float number and ranges from 0 to 1
	row.append(random.uniform(10,12)) #the third attribute is a random float number and ranges from 10 to 12
	for j in range(27):
		pred_val = random.randint(0,1)
		row.append(pred_val)
	if (row[0] < 5 and row[6] == 0) or (row[9] == 1 and row[8] == 0 and row[1]==0) or (row[7]==1 and row[5]==1) or (row [11]==0 and row[20]==0 and row[16]==1):
		row.append(1)
	else:
		row.append(0)
	c.writerow(row)
# this algorithom has 30 attributes (from X1 to X30), 3 of them are numeric (X1-X3) and the others are nominal, Y is label. The output follow the rules: if 
# (row[0] < 5 and row[6] == 0) or (row[9] == 1 and row[8] == 0 and row[1]==0) or (row[7]==1 and row[5]==1) or (row [11]==0 and row[20]==0 and row[16]==1) then Y is 1;
# otherwise Y is 0. These rules can be recognized by J48 (decsion treee) easily which has accuracy about 99%. IBk (nearestneighbour) perform bad on this data set (accuracy around 65%).