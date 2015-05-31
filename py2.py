import os 
os.chdir('D:/headfirstpython')
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print('said:',end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')
man=[]
other=[]
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split (':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('FIle error')
finally:
    man_file.close ()
    other_file.close()
    import os
os.chdir ('D:/headfirstpython')
with open ('james.txt') as jaf:
	data=jaf.readline()
	james=data.strip().split(',')

with open('julie.txt') as juf:
	data=juf.readline()
	julie=data.strip().split(',')
print('james'+str(james))
print('julie'+str(julie))
def sanitize (time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return (time_string)
    (min,secs)=time_string.split(splitter)
    return (min+'.'+secs)
clean_james=[]
clean_julie=[]
for eachline in james:
    clean_james.append(sanitize(eachline))
for eachline in julie:
    clean_julie.append(sanitize(eachline))
james=set(clean_james)
julie=set(clean_julie)
print('james:'+str(james))
print('julie:'+str(julie))

