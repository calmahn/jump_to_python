f = open("C:/Users/calm/Documents/jump_to_python/새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()