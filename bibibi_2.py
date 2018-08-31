import shelve

shelf_file = shelve.open('mydata')
print(type(shelf_file))

print(shelf_file['cats'])

shelf_file.close()
