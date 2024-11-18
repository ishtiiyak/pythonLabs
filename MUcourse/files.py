fhandle = open(r'C:\Users\BUZZ TECH\pythonLabs\MUcourse\txt\file.txt', 'r')
# for line in fhandle:
#     print(line,end="")


fhandle.seek(0)
lines = fhandle.readlines()
print("Read lines as list:\n", lines)