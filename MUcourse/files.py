fhandle = open(r'C:\Users\BUZZ TECH\pythonLabs\MUcourse\txt\files.txt', 'r')
for line in fhandle:
    #line=line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)