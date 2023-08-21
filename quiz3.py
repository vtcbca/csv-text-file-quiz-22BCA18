#count and print the total number of lines starting with 'a','b',and'c' in "intro.txt" file.
f1="c:\\sqlite3\\csv\\bca.txt"
f2="c:\\sqlite3\\csv\\information.txt"
string='bca stands for bachor of computer application'
with open(f1,"w")as textfile:
    data=textfile.write(string)
with open(f2,"r")as textfile:
    data=textfile.read(string)
    for i in data:
    if(i=="a" or i=="A" or i=="b" or i=="B" or i=="c" or i=="C"):
        count=count+1
print("total line:"count)


        
    
