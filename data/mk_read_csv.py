#csv:comma separeted value

import csv

data = [ ['American','Hi'],['English','Hello'],['Bengali','Namaskar'],['Indian','Namaste'],['Arabian','Salam'],
        ['French','Bonjour']]
#Making a csv file from a list
fileobj = open('gret.csv','wt')

csvout = csv.writer(fileobj)
csvout.writerows(data)


fileobj.close()


#making a list from a csv file
csvobj = open('gret.csv','rt')
cin = csv.reader(csvobj)
cout = [ row for row in cin]
print(cout)
csvobj.close()


#making dictionary from csv file
csvobj = open('gret.csv', 'rt')
cin = csv.DictReader(csvobj,fieldnames = ['Citezen','Greet style'])
cout = [row for row in cin]
print(cout)
csvobj.close()



