import solr
import csv

instance = solr.Solr("http://localhost:8984/solr/search")
termsFile = csv.reader(open('files/search_terms.csv'), delimiter=";")
responseFile = open('files/results.txt', 'w')

result =[]
count =0
for [term] in termsFile:
	response = instance.select(term, facet='true', facet_field='departmentId', fq='')
	result.append("%s %s\n" % (len(response.facet_counts['facet_fields']['departmentId']), term))
	count += 1
	if count > 100:
		break


responseFile.writelines(result)
responseFile.close()