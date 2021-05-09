import os


myfile = open('test_file.txt', 'wt')
myfile.write("Hello World!\nThis is a text file for testing purpose.")
myfile.close()


print(os.path.exists('test_file.txt'))

print(os.path.isfile('test_file.txt'))

print(os.path.isdir('test_file.txt'))


#checking absolute pathname

print(os.path.isabs('/home/bapon/Desktop/annamalai_university/python3_program/system'))


#rename of a file

os.rename('test_file.txt', 'myfile.txt')



#check link

os.link('myfile.txt' ,'mylink')

os.symlink('myfile.txt','mysymlink')
