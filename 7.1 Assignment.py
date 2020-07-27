# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = fh.read()
y = x.upper()
print(y.rstrip())
