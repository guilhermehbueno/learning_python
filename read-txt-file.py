arquivo = open("files/musica.txt")
print arquivo

print "#Printing full file"
fullFileContent = arquivo.read()
print fullFileContent

print "\n#Printing first line"
arquivo = open("files/musica.txt", "r")
firstLine = arquivo.readline()
print firstLine

print "\n#Printing line by line"
arquivo = open("files/musica.txt", "r")
for line in arquivo:
	print line
arquivo.close()

