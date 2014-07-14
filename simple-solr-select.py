import solr

s = solr.Solr("http://localhost:8984/solr/search")
response = s.select("name_s:tv",facet='true', facet_field='departmentId', fq='isVisible:true')

print len(response.facet_counts['facet_fields']['departmentId'])