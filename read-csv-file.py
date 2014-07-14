import csv

arquivo = csv.reader(open('files/search_terms.csv'), delimiter=';')
count = 0
for [term] in arquivo:
	print'%s' % term
	count +=1

print "%s lines" % count
