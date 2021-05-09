#w:write file if exists or not exists
#x:means write if the file does not exists
#r:read the file if exists
#a:means append if the file exists
#b:means binary file
#t: text fille

content = "This string goes inside of the file"
fileobj = open("file.txt",'wt')
fileobj.write(content)
fileobj.close()



#again open
fileobj = open("file.txt", 'at')
text = "\nThis is another string which going to append"
fileobj.write(text)
fileobj.close()
