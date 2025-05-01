import os
#(a)
print(os.listdir("."))
print("=============================")
#(b)
print(os.listdir(".."))
#(c)
test1 = "This is a test of the emergency text system"
f = open("test.txt","w")
f.write(test1)
f.close()
#(d)
print("========================")
with open("test.txt","r") as fout:
    test2 = fout.read()

if test1 == test2:
    print(True)
else:
    print(False)