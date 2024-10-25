
string="Please contact ali.hassan@gmail.com for assistance."

with open('example.txt', 'w') as file:
    file.write("Hello, Python!\nThis is a sample file.")

newlist=string.split()
with_email=[]
for email in newlist:

    if '@' in email :
        with_email.append(email)

# print(with_email)
 
# print(masked_email[1])
masked_email=['aaaa@gmail.com','ashsjshdj@gmao.co']
maskedemail1=[]
for i in with_email:
    
    for j in i:
        index=i.find('@')
    newstr='*'*index+"@gmail.com"
    maskedemail1.append(newstr)
print(maskedemail1)


