import sqlite3

connect = sqlite3.connect("D:\\201804011\\sqlite3\\test")
cursor = connect.cursor()

cursor.execute("select * from student")
print(" 학번    이름         이메일        생년")
print("=" * 40)

while(True) :
    row = cursor.fetchone()
    if row == None :
        break
    
    print("%s\t%s\t%-20s%s" % (row[0], row[1], row[2], row[3]))

connect.close()
