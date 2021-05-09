fout = open('bfile', 'wb')

bdata = bytes(range(0,256))
print(bdata)
size = len(bdata)

offset = 0
chunk = 100

while True:
    if offset > size:
        break
    else:
        fout.write(bdata[offset:offset+chunk])
        
        offset += chunk

fout.close()
