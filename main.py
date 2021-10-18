import random
import sqlite3

con = sqlite3.connect("quizz.db")
cur = con.cursor()

for j in range(1, 6):
    table = "SELECT *FROM level_" + str(j) + " WHERE id=" + str(random.randint(1, 2))

    for i in range(len(cur.execute(table).fetchall()[0]) - 2):
        print(cur.execute(table).fetchall()[0][i + 1])
    try:
        a = int(input())
    except:
        print("Хватит ломать код")
        exit()
    if a > 0 and a < 5:
        if cur.execute(table).fetchall()[0][6] == cur.execute(table).fetchall()[0][a + 1]:
            print("Правильно")
        else:
            print("Вы проиграли")
            exit()
    else:
        print("Такого ответа нету ._.")
        exit()
print("Вы выиграли")
con.commit()
cur.close()
con.close()
