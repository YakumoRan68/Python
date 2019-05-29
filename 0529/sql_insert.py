import sqlite3

connect = sqlite3.connect("D:\\201804011\\sqlite3\\test")
cursor = connect.cursor()

while(True) :
    grade_num = input("학번 : ")
    if grade_num == "0" :
        break
    name = input("성명 : ")
    email = input("이메일 : ")
    birthYY = input("생년 : ")
    query = "insert into student values('" + grade_num + "','" + name + "','" + email + "','" + birthYY + "')"
    print(query)

    cursor.execute(query)

connect.commit()
connect.close()