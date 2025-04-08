import sqlite3


def create_database():
    try:
        with sqlite3.connect('Methodb.db') as conn:
            cursor = conn.cursor()
            cursor.executescript('''
            CREATE TABLE IF NOT EXISTS cyrs (
                Cyrs_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_Cyrs TEXT NOT NULL,
                teacher_id INTEGER NOT NULL,
                FOREIGN KEY (teacher_id) REFERENCES teacher(id_teacher)
            );
            
            CREATE TABLE IF NOT EXISTS practic (
                id_Practic INTEGER PRIMARY KEY AUTOINCREMENT,
                Vopros TEXT NOT NULL,
                id_Thems INTEGER NOT NULL,
                FOREIGN KEY (id_Thems) REFERENCES thems(id_Thems)
            );
            
            CREATE TABLE IF NOT EXISTS predmet (
                id_predmet INTEGER PRIMARY KEY AUTOINCREMENT,
                name_predmet TEXT NOT NULL,
                teacher_id INTEGER NOT NULL,
                FOREIGN KEY (teacher_id) REFERENCES teacher(id_teacher)
            );
            
            CREATE TABLE IF NOT EXISTS student (
                id_student INTEGER PRIMARY KEY AUTOINCREMENT,
                Cyrs_id INTEGER NOT NULL,
                Predmet_id INTEGER NOT NULL,
                FIO TEXT NOT NULL,
                Login TEXT UNIQUE NOT NULL,
                Password TEXT NOT NULL,
                FOREIGN KEY (Cyrs_id) REFERENCES cyrs(Cyrs_id)
                FOREIGN KEY (Predmet_id) REFERENCES predmet(id_predmet)
            );
            
            CREATE TABLE IF NOT EXISTS stud_otvet (
                Stud_otvet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_thems INTEGER NOT NULL,
                id_student INTEGER NOT NULL,
                otvet_prac TEXT,
                ball_test INTEGER,
                ball_prac INTEGER,
                FOREIGN KEY (id_thems) REFERENCES thems(id_Thems),
                FOREIGN KEY (id_student) REFERENCES student(id_student)
            );
            
            CREATE TABLE IF NOT EXISTS teacher (
                id_teacher INTEGER PRIMARY KEY AUTOINCREMENT,
                FIO TEXT NOT NULL,
                Login TEXT UNIQUE NOT NULL,
                Password TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS test_nesc_otvet (
                id_test_nesc INTEGER PRIMARY KEY AUTOINCREMENT,
                id_Thems INTEGER NOT NULL,
                Vopros TEXT NOT NULL,
                otvet_1 TEXT NOT NULL,
                otvet_2 TEXT NOT NULL,
                otvet_3 TEXT NOT NULL,
                otvet_4 TEXT NOT NULL,
                otvet_5 TEXT NOT NULL,
                correct_otvet TEXT NOT NULL,
                FOREIGN KEY (id_Thems) REFERENCES thems(id_Thems)
            );
            
            CREATE TABLE IF NOT EXISTS test_one_otvet (
                id_test_one INTEGER PRIMARY KEY AUTOINCREMENT,
                id_Thems INTEGER NOT NULL,
                Vopros TEXT NOT NULL,
                otvet_1 TEXT NOT NULL,
                otvet_2 TEXT NOT NULL,
                otvet_3 TEXT NOT NULL,
                correct_otvet TEXT NOT NULL,
                FOREIGN KEY (id_Thems) REFERENCES thems(id_Thems)
            );
            
            CREATE TABLE IF NOT EXISTS teoria (
                id_teoria INTEGER PRIMARY KEY AUTOINCREMENT,
                id_Thems INTEGER NOT NULL,
                Text_teoria TEXT NOT NULL,
                FOREIGN KEY (id_Thems) REFERENCES thems(id_Thems)
            );
            
            CREATE TABLE IF NOT EXISTS thems (
                id_Thems INTEGER PRIMARY KEY AUTOINCREMENT,
                predmet_id INTEGER NOT NULL,
                Cyrs_id INTEGER NOT NULL,
                name_Them TEXT NOT NULL,
                types_test INTEGER NOT NULL,
                types_prac INTEGER NOT NULL CHECK(types_prac IN (0,1)),
                FOREIGN KEY (Cyrs_id) REFERENCES cyrs(Cyrs_id),
                FOREIGN KEY (predmet_id ) REFERENCES predmet(id_predmet )
            );
            ''')  # Создание таблиц

    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")


create_database()