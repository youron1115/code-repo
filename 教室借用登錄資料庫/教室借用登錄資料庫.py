import sqlite3
path=r"D:\Code-repo\教室借用登錄資料庫\borrow_record_database.db"
def create_borrow_record_database():
    
    #需根據位置調整路徑
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrow_record_table (
            借出教室 TEXT NOT NULL,
            借出者 TEXT NOT NULL,
            用途 TEXT NOT NULL,
            證件 TEXT NOT NULL,
            借出用具 TEXT,
            連絡電話 TEXT NOT NULL,
            歸還時間 TEXT NOT NULL,
            借出時間 TEXT NOT NULL
        )
    ''')

    
    conn.commit()
    conn.close()

def insert_borrow_record():
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        
        classroom = input("輸入教室: ")
        borrower = input("輸入借用者: ")
        purpose = input("輸入租借用途: ")
        identification = input("輸入抵押證件: ")
        equipment = input("若有，輸入租借用具: ")
        contact_number = input("輸入連絡電話: ")
        return_time = input("輸入歸還時間: ")
        borrow_time = input("輸入租借時間: ")
        
        cursor.execute('''
            INSERT INTO borrow_record_table (借出教室, 借出者, 用途, 證件, 借出用具, 連絡電話, 歸還時間, 借出時間)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (classroom, borrower, purpose, identification, equipment, contact_number, return_time, borrow_time))

        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("資料庫連接錯誤:", error)

def query_borrow_records(classroom):
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM borrow_record_table WHERE 借出教室 = ?
        ''', (classroom, ))

        records = cursor.fetchall()
        for record in records:
            print(record)

        conn.close()
        
    except sqlite3.Error as error:
        print("資料庫連接錯誤:", error)

    
print("\n請輸入欲使用之服務:\n1.創建資料庫\n2.新增資料至資料庫中\n3.查詢紀錄\n")
choice=input("使用之服務:")

if choice=="1" or choice=="1.":
    create_borrow_record_database()
    print("已創建資料庫，資料庫位置:")
    print(path)
    
elif choice=="2" or choice=="2.":
    insert_borrow_record()
    print("\n請至資料庫確認是否已成功新增資料")
    
elif choice=="3" or choice=="3.":
    classroom = input("輸入欲查詢之紀錄之教室:")
    query_borrow_records(classroom)
    print("已顯示符合條件之紀錄")
else:
    print("你輸入的選項有誤!")