import shelve

shelf_file = shelve.open('mydata')
cats = ['Zon','Pika','simon']
shelf_file['cats'] = cats
shelf_file.close()
