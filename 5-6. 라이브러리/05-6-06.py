import tempfile
filename = tempfile.mkstemp()
print(filename)

f = tempfile.TemporaryFile()
f.close()