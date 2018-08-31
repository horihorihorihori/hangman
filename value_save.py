import pprint
cats = [{'name':'Zon','desc':'chuby'},{'name':'hobby','desc':'flu'}]
pprint.pformat(cats)

file_obj = open('myCats.py','w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')

file_obj.close()
