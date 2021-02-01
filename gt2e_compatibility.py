# TOOL FOR PARSING GT2-GT2E TRAINING FILES 
# WORK IN PROGRESS
# IT'LL CREATE A FILE NAMED RESULT
filename=input("Insert filename to parse: ")
tmp=open(filename, "r")
data=tmp.read()

rows=data.split("\n")
position_rows=[]

def get_position_rows(rws):
    for n in range(len(rws)-1):
        if rws[n][0:6] == 'tp=lbs':
            position_rows.append(rws[n])
        elif rws[n][0:6] == 'tp=h-r':
            position_rows.append(rws[n])
get_position_rows(rows)
print(position_rows)

f=open('result','w')
s1='\n'.join(position_rows)
f.write(s1)
f.close()
