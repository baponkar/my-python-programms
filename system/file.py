#creating a file

myfile = open('test_file.txt', 'wt')

content = " This is the content of the file.\nThis is a second line.\n"

myfile.write(content)

myfile.close()
