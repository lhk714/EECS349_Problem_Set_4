import csv, random
c = csv.writer(open('prob_test.csv', 'wb'))
header = []
for i in range(30):
	header.append('X' + str(i+1))
header.append('Y')
c.writerow(header)

X ={}
for i in range(30):
	x = [d for d in range(1000)]
	random.shuffle(x)
	X[i] = x

for i in range(1000):
	row = []
	for j in range(30):
		row.append(X[j][i])
	if X[j][i] % 2 ==0:
		row.append(0)
	else:
		row.append(1)

	c.writerow(row)