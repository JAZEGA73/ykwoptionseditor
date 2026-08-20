
data = input("Select location of the ykw save : ")
with open(data, 'rb') as f:
    f.seek(0x28, 0) 
    contenido = f.read(0x10).split(b"\x00")[0]
    try:
        contenido = contenido.decode("utf-8")
    except UnicodeDecodeError:
        contenido = contenido.decode("cp932")
print("Old name : {}".format(contenido))
newname = input("New name : ")
with open(data, 'r+b') as s:
    s.seek(0x28, 0)
    name = s.read(0x10).replace(contenido.encode("utf-8"), newname.encode("utf-8"))
    s.seek(0x28)
    s.write(name)
print("Done!")


