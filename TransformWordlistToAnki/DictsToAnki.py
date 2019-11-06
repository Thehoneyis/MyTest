import os
lastchar = '+'
tabs = 0
file1 = open('ass.txt', 'r', encoding = 'utf-8')
with open('b.txt', 'w', encoding = 'utf-8') as file2:
    for line in file1 :
        if line not in ['\n', '\r\n'] and line[0] != '$' and line[0] != '@':
            if line[0] == '+' :
                file2.write('\n')
            elif line[0] != lastchar[0] :
                file2.write('\t')
            
            
            file2.write(line[1:len(line)-1])
            lastchar = line[0]
