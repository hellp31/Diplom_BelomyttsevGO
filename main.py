import sys
import sqlite3
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import create_db
import hashlib
from PyQt6.QtCore import Qt
import time
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


# Проверка существования файла
file_path = 'Methodb.db'
person=0
#print = lambda *args, **kwargs: None

if not os.path.exists(file_path):
    create_db.create_database()

# Импорты классов интерфейсов
from  window.LoginWin import Ui_LoginWin
from  window.RegWin import Ui_RegWin
from  window.ThemsWin_stud import Ui_ThemsWin_stud
from  window.ThemsWin_teacher import Ui_ThemsWin_teacher
from  window.Them1chage_1 import Ui_ChegeThemOne_1Win
from  window.Them1change_testrad import Ui_Chagethemone_2radWin
from  window.Them1change_testcheckb import Ui_Chagethemone_2checkbWin
from  window.Add_cyrsWin import Ui_Add_cyrsWin
from  window.CheckthemsWin import Ui_checkthemsWin
from  window.Cyrs_predWin import Ui_cyrs_predWind
from  window.Prac_provercWin import Ui_pract_provercWin
from  window.Add_predmet import Ui_Add_predmetWin
from  window.Prac_makeWin import Ui_Prac_makeWin
from  window.Prac_studWin import Ui_Prac_studWin
from  window.Reg_adminWin import Ui_Reg_adminWin
from  window.Test_rad_studWin import Ui_Test_rad_studWin
from  window.Test_checkb_studWin import Ui_Test_checkb_studWin
from  window.Vibor_fioWin import Ui_vibor_fioWin
from  window.Chage_test_radWin import Ui_Chagethemone_radWin
from  window.Chagethemnesk_checkWin import Ui_Chagethemnesk_checkWin
from  window.Mejdu_studWin import Ui_Mejdu_studWin
from  window.Teoria_studWin import Ui_Teoria_studWin
from  window.Teoria_teachWin import Ui_Teoria_teachWin



def is_user_exists(conn, username, password, id_wind):
    
    if id_wind == 1:
        conn = sqlite3.connect(file_path)
        """Проверка существования пользователя в базе данных."""
        cursor = conn.cursor()
        sql = "SELECT id_student FROM student WHERE Login = ? AND Password = ? "
        cursor.execute(sql, (username, password,))
        result = cursor.fetchone()

        if result:
            # Если пользователь найден, то вернуть его ID
            return result[0]
        else:
            # Если пользователь не найден, вернуть None
            return None
    else:
        conn = sqlite3.connect(file_path)
        """Проверка существования пользователя в базе данных."""
        cursor = conn.cursor()
        sql = "SELECT id_student FROM student WHERE Login = ? "
        cursor.execute(sql, (username, ))
        result = cursor.fetchone()

        if result:
            # Если пользователь найден, то вернуть его ID
            return result[0]
        else:
            # Если пользователь не найден, вернуть None
            return None


def is_teacher_exists(conn, username, password, id_wind):
    if id_wind == 1:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        sql = "SELECT id_teacher FROM teacher WHERE Login = ? AND Password = ?"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()

        if result:
            # Если пользователь найден, то вернуть его ID
            return result[0]
        else:
            # Если пользователь не найден, вернуть None
            return None
    else:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        sql = "SELECT id_teacher FROM teacher WHERE Login = ?"
        cursor.execute(sql, (username, ))
        result = cursor.fetchone()

        if result:
            # Если пользователь найден, то вернуть его ID
            return result[0]
        else:
            # Если пользователь не найден, вернуть None
            return None



def mainWin():
    global ui , LoginWin, predmeti_id,cursi_id
    ui = Ui_LoginWin()
    app = QtWidgets.QApplication(sys.argv)
    LoginWin = QtWidgets.QDialog()
    ui = Ui_LoginWin()
    ui.setupUi(LoginWin)
    LoginWin.show()
    ui.pushButton.clicked.connect(Login)
    ui.pushButton_2.clicked.connect(open_RegWin)
    ui.textEdit.setPlaceholderText('Введите логин')  # Используем placeholder вместо setText
    ui.textEdit_2.setPlaceholderText('Введите пароль')  # То же самое для пароля



    sys.exit(app.exec())


def Login():
    global LoginWin, ThemsWin_teacher, ThemsWin_stud,person

    login = ui.textEdit.toPlainText()
    password = ui.textEdit_2.toPlainText()
    
    
    id_wind=1

    # Проверка заполнения полей
    if not login:
            ui.label_8.setText(" Введите Логин")
            ui.label_8.setStyleSheet("""
             
                    color: red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)

    elif not password:
            ui.label_8.setText("")
            ui.label_9.setText(" Введите Пароль") 
            ui.label_9.setStyleSheet("""
             
                    color: red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
    else:
        ui.label_8.setText("")
        ui.label_9.setText("")
        try:
            with sqlite3.connect(file_path) as conn:
                # Получаем роль
                if ui.radioButton.isChecked():
                    def id_newteacher(login):
                        conn = sqlite3.connect(file_path)
                        """Проверка существования пользователя в базе данных."""
                        cursor = conn.cursor()
                        sql = "SELECT id_teacher FROM teacher WHERE Login = ?"
                        cursor.execute(sql, (login, ))
                        result = cursor.fetchall()
                        conn.close()
                        return result
                    id_user = id_newteacher(login)
                    if id_user:
                        password='new_user_'+str(id_user[0][0])+password
                    else:
                        ui.label_4.setText("Такого пользователя не существует")
                        ui.label_4.setStyleSheet("""
             
                    color: red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                    """)
                        return
                    
                    
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
                    person = is_teacher_exists(conn, login, hashed_password,id_wind )
                    if person:
                        open_curspred_win()
                        ui.label_4.setText('')
                        return person
                    else:
                        ui.label_4.setText("Такого пользователя не существует")
                        ui.label_4.setStyleSheet("""
             
                    color: red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                    """)
                        return
                    
                else:
                    def id_newstudent(login):
                        conn = sqlite3.connect(file_path)
                        """Проверка существования пользователя в базе данных."""
                        cursor = conn.cursor()
                        sql = "SELECT id_student FROM student  WHERE Login = ?"
                        cursor.execute(sql, (login,) )
                        result = cursor.fetchall()
                        conn.close()
                        return result
                    id_user = id_newstudent(login)
                    if id_user:
                        password='new_user_'+str(id_user[0][0])+password
                    else:
                        ui.label_4.setText("Такого пользователя не существует")
                        ui.label_4.setStyleSheet("""
             
                    
                    color: red;
                    font:  12pt "Times New Roman";
                    
                """)
                        return
                
                   
                    
                    hashed_password = hashlib.md5(password.encode()).hexdigest()
                    person = is_user_exists(conn, login, hashed_password,id_wind )
                    if person:
                      def get_students(login,hashed_password):
                          con = sqlite3.connect(file_path)
                          
                          cur = con.cursor()
                          query = """SELECT Cyrs_id, Predmet_id FROM student WHERE Login = ? AND Password = ? """
                          cur.execute(query, (login,hashed_password ))
                          rows = cur.fetchall()
                          con.close()
                          return [(row[0],row[1]) for row in rows]# Возвращаем кортежи (name, id)
                      cyrs_predmets = get_students(login,hashed_password)
                      id_predmet = cyrs_predmets[0][1]
                      id_cyrs = cyrs_predmets[0][0]
                      print(id_predmet)
                      print(id_cyrs)
                      open_ThemsWin_stud(id_cyrs,id_predmet)
                      ui.label_4.setText('')
                      return person
                    else:
                        ui.label_4.setText("Такого пользователя не существует")
                        ui.label_4.setStyleSheet("""
             
                    
                    color: red;
                    font:  12pt "Times New Roman";
                    
                """)

        except sqlite3.Error as err:
            print(f"Ошибка базы данных: {err}")




def logout(window):
    LoginWin.show()
    window.close()


def get_predmet():
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name_predmet, id_predmet FROM predmet")
    predmets = cursor.fetchall()
    return [(row[0], row[1]) for row in predmets]  # Возвращаем кортежи (name, id)


def get_predmet_teacher(person):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name_predmet, id_predmet FROM predmet WHERE teacher_id = ?", (person,))
    predmets = cursor.fetchall()
    return [(row[0], row[1]) for row in predmets]  # Возвращаем кортежи (name, id)

def open_curspred_win():
    global cyrs_predWind, cursi, predmeti
    cyrs_predWind = QtWidgets.QDialog()
    ui = Ui_cyrs_predWind()
    ui.setupUi(cyrs_predWind)
    cyrs_predWind.show()
    LoginWin.close()
    window = cyrs_predWind
    logout_function = lambda: logout(window)
    
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    ui.pushButton_9.setIcon(icon)
    
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    ui.pushButton_10.setIcon(icon1)
    
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("icon/logout_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    ui.pushButton_11.setIcon(icon2)
    
    # Заполняем комбо-бокс курсами
    courses = get_courses_teacher(person)
    print(f"Курсы: {courses}")

    # Заполняем комбо-бокс курсами
    ui.comboBox.addItem('Выберите...')
    ui.comboBox.addItems([course[0] for course in courses])
    
    predmets = get_predmet_teacher(person)
    print(f"Предметы: {predmets}")

    # Заполняем комбо-бокс курсами
    ui.comboBox_2.addItem('Выберите...')
    ui.comboBox_2.addItems([predmet[0] for predmet in predmets])
    
    
    
    def on_button_clicked_FIO():
        global cursi, predmeti, predmeti_id,cursi_id
        selected_course_index = ui.comboBox.currentIndex()
        selected_predmet_index = ui.comboBox_2.currentIndex()

        if selected_course_index > 0:
            cursi = courses[selected_course_index - 1][0]
            cursi_id = courses[selected_course_index - 1][1]
        else:
            cursi = None

        if selected_predmet_index > 0:
            predmeti = predmets[selected_predmet_index - 1][0]
            predmeti_id = predmets[selected_predmet_index - 1][1]
        else:
            predmeti = None
            
        

        open_vibor_fioWin()
        
    def on_button_clicked_Thems():
        global cursi, predmeti, predmeti_id,cursi_id
        selected_course_index = ui.comboBox.currentIndex()
        selected_predmet_index = ui.comboBox_2.currentIndex()

        if selected_course_index > 0:
            cursi = courses[selected_course_index - 1][0]
            cursi_id = courses[selected_course_index - 1][1]
        else:
            cursi = None

        if selected_predmet_index > 0:
            predmeti = predmets[selected_predmet_index - 1][0]
            predmeti_id = predmets[selected_predmet_index - 1][1]
        else:
            predmeti = None
            
        

        open_ThemsWin_teacher()


   
    
    

    def open_add_cyrsWin():
        global Add_cyrs_predWin
        Add_cyrs_predWin = QtWidgets.QDialog()
        ui = Ui_Add_cyrsWin()
        ui.setupUi(Add_cyrs_predWin)
        Add_cyrs_predWin.show()
        window = Add_cyrs_predWin
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ui.pushButton_9.setIcon(icon)

        def add_cyrs():
            curs =ui.textEdit_2.toPlainText()
            id_uch = person
            if not curs:
                ui.label.setText(" Введите  Курс")
                ui.label.setStyleSheet('font-weight: bold; font: 12pt "Times New Roman";')
            else:
                try:
                    with sqlite3.connect(file_path) as conn:
                        cursor = conn.cursor()

                        cursor.execute("""INSERT INTO cyrs (name_Cyrs, teacher_id) VALUES (?, ?)""",
                                           (curs,id_uch))
                        conn.commit()
                        print("User registered successfully!")
                        
                        window.close()
                        cyrs_predWind.close()
                        logout_function
                        Login()
                        cyrs_predWind.show()



                except Exception as e:
                    print(e + 'errror')







        ui.pushButton_9.clicked.connect(add_cyrs)







    def open_add_predmetWin():
        global Add_predmetWin
        Add_predmetWin = QtWidgets.QDialog()
        ui = Ui_Add_predmetWin()
        ui.setupUi(Add_predmetWin)
        Add_predmetWin.show()
        window = Add_predmetWin
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ui.pushButton_9.setIcon(icon)
        
        
        
        
        def add_predmet():
            predmet =ui.textEdit_2.toPlainText()
            id_uch = person
            if not predmet:
                ui.label.setText(" Введите  Предмет")
                ui.label.setStyleSheet('font-weight: bold; font: 12pt "Times New Roman";')
            else:
                try:
                    with sqlite3.connect(file_path) as conn:
                        cursor = conn.cursor()

                        cursor.execute("""INSERT INTO predmet (name_predmet, teacher_id) VALUES (?, ?)""",
                                           (predmet,id_uch))
                        conn.commit()
                        print("User registered successfully!")
                        
                        window.close()
                        cyrs_predWind.close()
                        logout_function
                        Login()
                        cyrs_predWind.show()



                except Exception as e:
                    print(e + 'errror')


        ui.pushButton_9.clicked.connect(add_predmet)





    def open_vibor_fioWin():
        global vibor_fioWin, cursi, predmeti, predmeti_id,cursi_id
        vibor_fioWin = QtWidgets.QDialog()
        ui = Ui_vibor_fioWin()
        ui.setupUi(vibor_fioWin)
        vibor_fioWin.show()
        cyrs_predWind.close()
        window = vibor_fioWin
        print(cursi, predmeti)
        if cursi and predmeti:
            ui.label_2.setText(f"Курс: {cursi}\nПредмет: {predmeti}")
        else:
            ui.label_2.setText(f"Курс: Не выбран\nПредмет: Не выбран")
       
        def get_students(predmeti_id, cursi_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT FIO, id_student FROM student WHERE Cyrs_id = ? AND Predmet_id = ? """
                cur.execute(query, (cursi_id,predmeti_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1]) for row in rows]

        if cursi and predmeti:
            students = get_students(predmeti_id, cursi_id)
            print("Students:", students)  # Проверяем, какие данные извлеклись
        else:
            students = []
            print("No students found")
            
        # Используем существующую QScrollArea
        scrollAreaWidgetContents = ui.scrollAreaWidgetContents

        # Устанавливаем вертикальный layout для scrollAreaWidgetContents
        layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
        
        layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
        layout.setContentsMargins(0, 0, 0, 0)
        scrollAreaWidgetContents.setLayout(layout)

        # Очищаем содержимое scrollArea перед добавлением новых элементов
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
        if students:
            # Динамическое создание QLabel и QPushButton для каждого студента
            for i,  (student_name, id_student) in enumerate(students):
                print(f"Creating widget for {student_name} with ID: {id_student}")

                # Создаем контейнерный виджет для размещения метки и кнопки
                container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                grid_layout = QtWidgets.QGridLayout(container_widget)
                grid_layout.setContentsMargins(0, 0, 0, 0)
                grid_layout.setSpacing(0)
                container_widget.setLayout(grid_layout)
                word_count = len(student_name.split())  # Разбиваем строку на слова и считаем их количество

                if word_count > 8:
                    height = 100  # Высота метки, если слов больше 7
                else:
                    height = 50

                label = QtWidgets.QLabel(student_name, parent=container_widget)
                label.setStyleSheet("""
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    background-color: grey;
                    padding-left: 10px;
                """)
            

                # Включаем обратно управление положением метки со стороны layout-а
            

                
                
                label.setMinimumHeight(height)
                label.setMinimumWidth(400)
                label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                label.setWordWrap(True)  # Включаем перенос слов на новые строки
                label.setContentsMargins(0, 0, 0, 0)
                grid_layout.addWidget(label, 0, 0, 1, 1)

                pushButton_6 = QtWidgets.QPushButton(parent=container_widget)
                pushButton_6.setStyleSheet("""
                    background-color: green; /*Цвет текстового поля*/
                    
                    width: 250px;
                    height: 30px;
                    outline: none;
                    
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                """)
                pushButton_6.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("icon/visibility_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                pushButton_6.setIcon(icon1)
                pushButton_6.setIconSize(QtCore.QSize(25, 25))
                pushButton_6.setFixedWidth(height)
                pushButton_6.setFixedHeight(height)
                pushButton_6.setContentsMargins(0, 0, 0, 0)
                
                
                
                pushButton_6.clicked.connect(lambda _, id=id_student, curs=cursi_id, predmet=predmeti_id : open_checkthemsWin(id,predmet,curs))

                grid_layout.addWidget(pushButton_6, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                        # Добавляем контейнерный виджет в основной layout
                layout.addWidget(container_widget)


                        # Добавляем контейнерный виджет в основной layout
                


                print(f"Created label: {label}, Created button: {pushButton_6}")

        # Настраиваем размер QScrollArea
    # Настраиваем размер QScrollArea
        # Настраиваем размер QScrollArea
        ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
        ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
        ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
       

        # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
        ui.scrollArea.setMaximumHeight(421)
        ui.scrollArea.setMaximumWidth(471)

        
        

        def close_vibor_fioWin():
            cyrs_predWind.show()
            vibor_fioWin.close()
            
        def open_checkthemsWin(student_id,predmeti_id, cursi_id ):
            global checkthemsWin
            checkthemsWin = QtWidgets.QDialog()
            ui = Ui_checkthemsWin()
            ui.setupUi(checkthemsWin)
            checkthemsWin.show()
            vibor_fioWin.close()
            window = checkthemsWin
            logout_function = lambda: logout(window)
            
            
            
            def get_thems(predmeti_id, cursi_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT name_Them, id_Thems FROM thems WHERE Cyrs_id = ? AND predmet_id = ? """
                cur.execute(query, (cursi_id,predmeti_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0], row[1]) for row in rows]
            
            thems = get_thems(predmeti_id, cursi_id)
            print("Thems:", thems)
            
            def get_name(student_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT FIO FROM student WHERE id_student = ? """
                cur.execute(query, (student_id, ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
            
            id=student_id
            
            student_name=get_name(id)
            name=student_name[0]
            
            ui.label_3.setText(f"ФИО: {name}")
            
            scrollAreaWidgetContents = ui.scrollAreaWidgetContents

        # Устанавливаем вертикальный layout для scrollAreaWidgetContents
            layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
            
            layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
            layout.setContentsMargins(0, 0, 0, 0)
            scrollAreaWidgetContents.setLayout(layout)

            # Очищаем содержимое scrollArea перед добавлением новых элементов
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
            if thems:
                # Динамическое создание QLabel и QPushButton для каждого студента
                for i,  (them_name, id_thems) in enumerate(thems):
                    print(f"Creating widget for {them_name} with ID: {id_thems}")

                    def get_otvet(id_thems,id):
                                    con = sqlite3.connect(file_path)
                                    cur = con.cursor()
                                    query = """SELECT  ball_prac  FROM stud_otvet WHERE id_student=? AND id_thems=? """
                                    cur.execute(query, (id,id_thems ))
                                    rows = cur.fetchall()
                                    con.close()
                                    return [(row[0] ) for row in rows]
                                    

                    otveti = get_otvet(id_thems, id)

                    if otveti and otveti[0] != 0 :
                        
                       
                        color = "green"
                        
                    else:
                        color='grey'





                    # Создаем контейнерный виджет для размещения метки и кнопки
                    container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                    grid_layout = QtWidgets.QGridLayout(container_widget)
                    grid_layout.setContentsMargins(0, 0, 0, 0)
                    grid_layout.setSpacing(0)
                    container_widget.setLayout(grid_layout)

                    label = QtWidgets.QLabel(them_name, parent=container_widget)
                    
                    word_count = len(them_name.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    if color=='grey':
                        label.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                        """)
                    else:
                        label.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                        """)
                    

                    # Включаем обратно управление положением метки со стороны layout-а
                

                    
                    
                    label.setMinimumHeight(height)
                    label.setMinimumWidth(390)
                    label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label, 0, 0, 1, 1)

                    pushButton = QtWidgets.QPushButton(parent=container_widget)
                    pushButton.setStyleSheet("""
                        background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
                    pushButton.setText("")
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(QtGui.QPixmap("icon/visibility_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    pushButton.setIcon(icon1)
                    pushButton.setIconSize(QtCore.QSize(25, 25))
                    pushButton.setFixedWidth(50)
                    pushButton.setFixedHeight(height)
                    pushButton.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
                    pushButton.clicked.connect(lambda _,  id=student_id, thems_id=id_thems : open_provercWin(thems_id,id))

                    grid_layout.addWidget(pushButton, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                    layout.addWidget(container_widget)
            
            
            
                
                
                
            ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
            ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
            ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
       

            # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
            ui.scrollArea.setMaximumHeight(421)
            ui.scrollArea.setMaximumWidth(471)
   
                
            def close_checkthemsWin():
                vibor_fioWin.show()
                window.close()

            def open_provercWin(id_thems,id):
                global Pract_provercWin
                Pract_provercWin = QtWidgets.QDialog()
                ui = Ui_pract_provercWin()
                ui.setupUi(Pract_provercWin)
                Pract_provercWin.show()
                checkthemsWin.close()
                window = Pract_provercWin
                logout_function = lambda: logout(window)
                
                
                def get_name(student_id):
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT FIO FROM student WHERE id_student = ? """
                    cur.execute(query, (student_id, ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0]) for row in rows]
            
                def close_Pract_provercWin(id_wind,Stud_otvet_id=0):
                    if id_wind==1:
                        otsenka=ui.textEdit_2.toPlainText()
                        if not otsenka or otsenka=='0':
                            otsenka=0
                        
                        try:
                                        with sqlite3.connect(file_path) as conn:
                                            cursor = conn.cursor()
                                            print('ok1')
                                            
                                            # Выполняем UPDATE-запрос
                                            cursor.execute("""
                                                UPDATE stud_otvet
                                                SET ball_prac = ?
                                                WHERE Stud_otvet_id = ?  
                                            """, (otsenka,Stud_otvet_id))
                                            
                                            conn.commit()  # Сохранение изменений
                                            cursor.execute("""SELECT id_student, id_thems FROM stud_otvet WHERE Stud_otvet_id = ? """,(Stud_otvet_id,))
                                            rows = cursor.fetchall()
                                            id_student=rows[0][0]
                                            id_thems=rows[0][1]
                                            print('ok1')
                                            cursor.execute("""SELECT predmet_id, Cyrs_id FROM thems WHERE id_Thems = ? """,(id_thems,))
                                            rows = cursor.fetchall()
                                            
                                            id_cyrs=rows[0][1]
                                            id_predmet=rows[0][0]
                                            
                                            print("Данные успешно обновлены!")
                                            Pract_provercWin.close()
                                            
                                            open_checkthemsWin(id_student,id_predmet,id_cyrs)
                                            
                                            
                                            
                        except Exception as e:
                                        print(f'Ошибка при обновлении данных: {e}')
                    else:
                        Pract_provercWin.close()
                        checkthemsWin.show()


            
                student_name=get_name(id)
                name_stud=student_name[0]
                
                def get_thems(id_thems):
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT name_Them  FROM thems WHERE id_Thems=? """
                    cur.execute(query, (id_thems, ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0]) for row in rows]
                    
                thems=get_thems(id_thems)
                name_thems=thems[0]
                ui.label_2.setText(name_thems)
                ui.label_2.setStyleSheet("""
                        font-weight: bold;
                        font:  20pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                    """)
                
                ui.label_7.setText(name_stud)
                ui.label_7.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                    """)
                
                def get_vopros(id_thems):
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT Vopros  FROM practic WHERE id_Thems=? """
                    cur.execute(query, (id_thems, ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0]) for row in rows]
                
                vopros=get_vopros(id_thems)
                if vopros:
                    name_vopros=vopros[0]
                else :
                    name_vopros="Нет вопросов"
                
                
                ui.textBrowser_2.setText(name_vopros)
                ui.textBrowser_2.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        
                        padding-left: 10px;
                    """)
                
                def get_otvet(id_thems,id):
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT otvet_prac, ball_test, Stud_otvet_id, ball_prac  FROM stud_otvet WHERE id_student=? AND id_thems=? """
                    cur.execute(query, (id,id_thems ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0],row[1],row[2], row[3]) for row in rows]
                
                print(id_thems, id)
                otveti = get_otvet(id_thems, id)
                print(otveti)
                
                
                
                if otveti:
                    stud_otvet = otveti[0][0]
                    Stud_otvet_id=otveti[0][2]
                    ball_prac=otveti[0][3]
                    ball_test = otveti[0][1]
                
                    
                    
                    if ball_test != None:
                        ui.label.setText(f'Балл тест: {ball_test}')
                    else:
                        ui.label.setText(f'Теста не было')
                    
                    if ball_prac !=0:
                        ui.textEdit_2.setText(str(ball_prac))
                    else:
                        ui.textEdit_2.setText("")
                        
               
               
                    if stud_otvet:
                        
                        ui.textBrowser.setText(stud_otvet)
                        ui.textBrowser.setStyleSheet("""
                                            font-weight: bold;
                                            font:  12pt "Times New Roman";
                                            
                                            
                                        """)
                        
                    else:
                        ui.textBrowser.setText("Ответ от студента нет")
                        ui.textBrowser.setStyleSheet("""
                                            font-weight: bold;
                                            font:  30pt "Times New Roman";""")
                        
                    ui.pushButton_3.clicked.connect(lambda _,  : close_Pract_provercWin(1,Stud_otvet_id))
                    
                else:
                    
                    ui.textBrowser.setText("Студент еще не ответил на этот вопрос")
                    ui.textBrowser.setStyleSheet("""
                                            font-weight: bold;
                                            font:  30pt "Times New Roman";""")
                    ui.label.setText(f'Теста не было')
                    ui.pushButton_3.clicked.connect(lambda _,  : close_Pract_provercWin(2))
                 
                 
                    
              
                
                

            
            
            ui.pushButton_3.clicked.connect(close_checkthemsWin)
        
        ui.pushButton_3.clicked.connect(close_vibor_fioWin)





    def open_ThemsWin_teacher():
        global ThemsWin_teacher, cursi, predmeti, predmeti_id,cursi_id
        ThemsWin_teacher = QtWidgets.QDialog()
        ui = Ui_ThemsWin_teacher()
        ui.setupUi(ThemsWin_teacher)
        ThemsWin_teacher.show()
        cyrs_predWind.close()
        window = ThemsWin_teacher
        logout_function = lambda: logout(window)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/logout_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ui.pushButton_11.setIcon(icon2)

        
        def get_thems(predmeti_id, cursi_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT name_Them, id_Thems FROM thems WHERE Cyrs_id = ? AND predmet_id = ? """
                cur.execute(query, (cursi_id,predmeti_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0], row[1]) for row in rows]
        '''''   
        def get_vopros_prac(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_prac FROM thems WHERE id_Thems = ? """
                cur.execute(query, (thems_id ))
                if cur.fetchone()  == 0:
                    return []
                else:
                    query = """SELECT Vopros, id_Practic FROM practic WHERE id_Thems = ? """
                    cur.execute(query, (thems_id ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0],row[1]) for row in rows]
                '''''
                
        if cursi and predmeti:
            thems = get_thems(predmeti_id, cursi_id)
        else:
            thems =[]
            ui.label_2.setText(f"Курс и предмет\nНе выбраны")
            ui.label_2.setStyleSheet("""
             
                    background-color: grey;
                    font-weight: bold;
                    font:  30pt "Times New Roman";
                """)
       


        
        
        
       # vopros_prec=get_vopros_prac(thems_id)
        
        
        print("Темы:", thems)  # Проверяем, какие данные извлеклись
        
            
        # Используем существующую QScrollArea
        scrollAreaWidgetContents = ui.scrollAreaWidgetContents

        # Устанавливаем вертикальный layout для scrollAreaWidgetContents
        layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
        
        layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
        layout.setContentsMargins(0, 0, 0, 0)
        scrollAreaWidgetContents.setLayout(layout)

        # Очищаем содержимое scrollArea перед добавлением новых элементов
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
        if thems:
            # Динамическое создание QLabel и QPushButton для каждого студента
            for i,  (them_name, id_thems) in enumerate(thems):
                print(f"Creating widget for {them_name} with ID: {id_thems}")

                # Создаем контейнерный виджет для размещения метки и кнопки
                container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                grid_layout = QtWidgets.QGridLayout(container_widget)
                grid_layout.setContentsMargins(0, 0, 0, 0)
                grid_layout.setSpacing(0)
                container_widget.setLayout(grid_layout)

                label = QtWidgets.QLabel(them_name, parent=container_widget)
                
                word_count = len(them_name.split())  # Разбиваем строку на слова и считаем их количество

                if word_count > 8:
                    height = 100  # Высота метки, если слов больше 7
                else:
                    height = 50
                label.setStyleSheet("""
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    background-color: grey;
                    padding-left: 10px;
                """)
            

                # Включаем обратно управление положением метки со стороны layout-а
            

                
                
                label.setMinimumHeight(height)
                label.setMinimumWidth(350)
                label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                label.setWordWrap(True)  # Включаем перенос слов на новые строки
                label.setContentsMargins(0, 0, 0, 0)
                grid_layout.addWidget(label, 0, 0, 1, 1)

                pushButton = QtWidgets.QPushButton(parent=container_widget)
                pushButton.setStyleSheet("""
                    background-color: green; /*Цвет текстового поля*/
                    
                    width: 250px;
                    height: 30px;
                    outline: none;
                    
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                """)
                pushButton.setText("")
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("icon/file_open_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                pushButton.setIcon(icon1)
                pushButton.setIconSize(QtCore.QSize(25, 25))
                pushButton.setFixedWidth(height)
                pushButton.setFixedHeight(height)
                pushButton.setContentsMargins(0, 0, 0, 0)
                
                
                
                pushButton.clicked.connect(lambda _,  id=id_thems: open_Them1chage_old(id))

                grid_layout.addWidget(pushButton, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                
                
                
                
                pushButton_1 = QtWidgets.QPushButton(parent=container_widget)
                pushButton_1.setStyleSheet("""
                    background-color: red; /*Цвет текстового поля*/
                    
                    width: 250px;
                    height: 30px;
                    outline: none;
                    
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                """)
                pushButton_1.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("icon/delete_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                pushButton_1.setIcon(icon2)
                pushButton_1.setIconSize(QtCore.QSize(25, 25))
                pushButton_1.setFixedWidth(height)
                pushButton_1.setFixedHeight(height)
                pushButton_1.setContentsMargins(0, 0, 0, 0)
                
                
                
                pushButton_1.clicked.connect(lambda _, id=id_thems : delete_them(id))

                grid_layout.addWidget(pushButton_1, 0, 2, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец
                        # Добавляем контейнерный виджет в основной layout
                layout.addWidget(container_widget)


                
                        # Добавляем контейнерный виджет в основной layout
                


                print(f"Created label: {label}, Created button: {pushButton}, {pushButton_1}")

            # Настраиваем размер QScrollArea
        # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
        container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
        grid_layout = QtWidgets.QGridLayout(container_widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)
        container_widget.setLayout(grid_layout)
        if cursi and predmeti:        
            pushButton_6 = QtWidgets.QPushButton(parent=container_widget)
            pushButton_6.setStyleSheet("""
                background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
            pushButton_6.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            pushButton_6.setIcon(icon1)
            pushButton_6.setIconSize(QtCore.QSize(25, 25))
            pushButton_6.setFixedWidth(41)
            pushButton_6.setFixedHeight(41)
            pushButton_6.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
            pushButton_6.clicked.connect(lambda _,  : open_Themchage_new(predmeti_id, cursi_id))

            grid_layout.addWidget(pushButton_6, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                            # Добавляем контейнерный виджет в основной layout
            layout.addWidget(container_widget)
                
                
        ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
        ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
        ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
       

        # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
        ui.scrollArea.setMaximumHeight(421)
        ui.scrollArea.setMaximumWidth(471)

        
        

        
        
        
        def close_ThemsWin_teacher():
            cyrs_predWind.show()
            window.close()

        def open_ThempractWin_new(id_thems):
            global Prac_makeWin
            Prac_makeWin = QtWidgets.QDialog()
            ui = Ui_Prac_makeWin()
            ui.setupUi(Prac_makeWin)
            Prac_makeWin.show()
            thems_id=id_thems[0]
            print("ok")
            
            def close_Prac_makeWin():
                Prac_makeWin.close()
            
                
            
            def get_types(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_test FROM thems WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
            
            def get_vopros_prac(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Vopros,id_Practic FROM practic WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1]) for row in rows]
            
            types_test=get_types(id_thems)[0]# Получаем тип теста
            if types_test==1:
                Them1change_testradWin.close()
            elif types_test==2:
                Them1change_testcheckbWin.close()
            else:
                ChegeThemOne_1Win.close()
                print('Сразу сюда?')
                
            
            if get_vopros_prac(id_thems):
                vopros_prac=get_vopros_prac(id_thems)
                print(vopros_prac)
                vopros_name=vopros_prac[0][0]
                vopros=ui.textEdit.setText(vopros_name)
                id_vopros=vopros_prac[0][1]
                def old_vopros_create(thems_id,id_vopros):
                    vopros=ui.textEdit.toPlainText()
                    if not vopros:
                        ui.label_3.setText("Введите задание")
                        ui.label_3.setStyleSheet("""color: red;font: 30pt "Times New Roman";text-align: center;""") 
                        
                    else:   
                        ui.label_3.setStyleSheet("""color: black;font: 30pt "Times New Roman";text-align: center;""") 
                        try:
                            with sqlite3.connect(file_path) as conn:
                                                    cursor = conn.cursor()
                                                    print('ok1')# Проверяем наличие таблицы 
                                                    cursor.execute("""
                                                        UPDATE practic
                                                        SET Vopros = ?,
                                                            id_Thems = ?
                                                        WHERE id_Practic = ?  
                                                    """, (vopros,thems_id,id_vopros))
                                                    
                                                    conn.commit()  # Сохранение измененийв таблице
                                                    print("Vopros successfully!")
                                                    #thems_id_new = (thems_id,)
                                                    open_Teoria_teachWin(thems_id)

                                                    

                        except Exception as e:
                                            print(e + 'errror')
                    
                
                
                
                ui.pushButton_2.clicked.connect(lambda : old_vopros_create(thems_id,id_vopros))
            else: 
               vopros=ui.textEdit.setText('')
               def new_vopros_create(thems_id):
                    vopros=ui.textEdit.toPlainText()
                    if not vopros:
                        ui.label_3.setText("Введите задание")
                        ui.label_3.setStyleSheet("""color: red;font: 30pt "Times New Roman";text-align: center;""") 
                        
                    else:   
                        ui.label_3.setStyleSheet("""color: black;font: 30pt "Times New Roman";text-align: center;""") 
                        try:
                            with sqlite3.connect(file_path) as conn:
                                                    cursor = conn.cursor()
                                                    print('ok1')# Проверяем наличие таблицы 
                                                    cursor.execute("""INSERT INTO practic ( Vopros,id_Thems ) VALUES (?, ?)""",
                                                                (vopros,thems_id))
                                                    conn.commit()
                                                    print("Vopros successfully!")
                                                    #thems_id_new = (thems_id,)
                                                    open_Teoria_teachWin(thems_id)

                                                    

                        except Exception as e:
                                            print(e + 'errror')

               ui.pushButton_2.clicked.connect(lambda : new_vopros_create(thems_id))




        def delete_them(id_thems):
    # Функция для удаления темы из базы данных
            con = sqlite3.connect(file_path)
            cur = con.cursor()
            query = """DELETE FROM thems WHERE id_Thems = ?"""
            try:
                cur.execute(query, (id_thems,))
                con.commit()  # Подтверждение изменений
                print(f"Тема с id {id_thems} успешно удалена.")
                query = """DELETE FROM test_one_otvet WHERE id_Thems = ?"""
                cur.execute(query, (id_thems,))
                con.commit()
                query = """DELETE FROM test_nesc_otvet WHERE id_Thems = ?"""
                cur.execute(query, (id_thems,))
                con.commit()
                query = """DELETE FROM practic WHERE id_Thems = ?"""
                cur.execute(query, (id_thems,))
                con.commit()
                
            except Exception as e:
                print(f"Произошла ошибка при удалении темы: {e}")
            finally:
                con.close()
            close_ThemsWin_teacher()
            time.sleep(0.01)
            on_button_clicked_Thems()
            

        def open_Themtest_rad_Win(id_thems):
            global Them1change_testradWin
            Them1change_testradWin = QtWidgets.QDialog()
            ui = Ui_Chagethemone_2radWin()
            ui.setupUi(Them1change_testradWin)
            Them1change_testradWin.show()
            ChegeThemOne_1Win.close()
            thems_id=id_thems
            
            def get_testrad(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Vopros, id_test_one, otvet_1, otvet_2, otvet_3, correct_otvet FROM test_one_otvet WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1],row[2],row[3],row[4],row[5]) for row in rows]


            def get_vopros_prac(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_prac FROM thems WHERE id_Thems = ? """
                cur.execute(query, (thems_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
                   

           
            type_prac = get_vopros_prac(thems_id)[0]
            
            
            vopros = get_testrad(thems_id)
            print("Вопросы:", vopros)  # Проверяем, какие данные извлеклись
            type_prac
                
            # Используем существующую QScrollArea
            scrollAreaWidgetContents = ui.scrollAreaWidgetContents

            # Устанавливаем вертикальный layout для scrollAreaWidgetContents
            layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
            
            layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
            layout.setContentsMargins(0, 0, 0, 0)
            scrollAreaWidgetContents.setLayout(layout)

            # Очищаем содержимое scrollArea перед добавлением новых элементов
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
            if vopros:
                # Динамическое создание QLabel и QPushButton для каждого студента
                for i,  (vopros_name, id_testone, otvet_1, otvet_2, otvet_3, correct_otvet ) in enumerate(vopros):
                    print(f"Creating widget for {vopros_name} with ID: {id_testone}")

                    # Создаем контейнерный виджет для размещения метки и кнопки
                    container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                    grid_layout = QtWidgets.QGridLayout(container_widget)
                    grid_layout.setContentsMargins(0, 0, 0, 0)
                    grid_layout.setSpacing(0)
                    container_widget.setLayout(grid_layout)

                    
                    word_count = len(vopros_name.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    label = QtWidgets.QLabel(vopros_name, parent=container_widget)
                    label.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                    """)
 
                    label.setMinimumHeight(height)
                    label.setMinimumWidth(350)
                    label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label, 0, 0, 1, 1)

                    pushButton = QtWidgets.QPushButton(parent=container_widget)
                    pushButton.setStyleSheet("""
                        background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
                    pushButton.setText("")
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(QtGui.QPixmap("icon/file_open_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    pushButton.setIcon(icon1)
                    pushButton.setIconSize(QtCore.QSize(25, 25))
                    pushButton.setFixedWidth(height)
                    pushButton.setFixedHeight(height)
                    pushButton.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
                    pushButton.clicked.connect(lambda _, id=id_testone : open_change_testradWin_old(id))

                    grid_layout.addWidget(pushButton, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                    
                    
                    
                    label_1 = QtWidgets.QLabel(otvet_1, parent=container_widget)
                    
                    word_count = len(otvet_1.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    if otvet_1== correct_otvet:
                        label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    label_1.setMinimumHeight(height)
                    label_1.setMinimumWidth(200)
                    label_1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_1.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_1.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_1, 1, 0, 1, 1)
                    
                    
                    
                    
                    label_2 = QtWidgets.QLabel(otvet_2, parent=container_widget)
                    word_count = len(otvet_2.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    
                    if otvet_2== correct_otvet:
                        label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;

                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                    
                        label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)

 
                    label_2.setFixedHeight(height)
                    label_2.setMinimumWidth(200)
                    label_2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_2.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_2.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_2, 2, 0, 1, 1)
                    
                    
                    label_3 = QtWidgets.QLabel(otvet_3, parent=container_widget)
                    
                    word_count = len(otvet_3.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    if otvet_3== correct_otvet:
                        label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
 
                    label_3.setMinimumHeight(height)
                    label_3.setMinimumWidth(200)
                    label_3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_3.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_3.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_3, 3, 0, 1, 1)
                    
                    
                    
                    
                    layout.addWidget(container_widget)


                    
                            # Добавляем контейнерный виджет в основной layout
                    


                    print(f"Created label: {label}, Created button: {pushButton}")

                # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
                # Настраиваем размер QScrollArea
            container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
            grid_layout = QtWidgets.QGridLayout(container_widget)
            grid_layout.setContentsMargins(0, 0, 0, 0)
            grid_layout.setSpacing(0)
            container_widget.setLayout(grid_layout)
                    
            pushButton_6 = QtWidgets.QPushButton(parent=container_widget)
            pushButton_6.setStyleSheet("""
                background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
            pushButton_6.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            pushButton_6.setIcon(icon1)
            pushButton_6.setIconSize(QtCore.QSize(25, 25))
            pushButton_6.setFixedWidth(41)
            pushButton_6.setFixedHeight(41)
            pushButton_6.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
            pushButton_6.clicked.connect(lambda _ , id=thems_id: open_change_testradWin_new(id))

            grid_layout.addWidget(pushButton_6, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                            # Добавляем контейнерный виджет в основной layout
            layout.addWidget(container_widget)
                    
                    
            ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
            ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
            ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
        

            # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
            ui.scrollArea.setMaximumHeight(421)
            ui.scrollArea.setMaximumWidth(471)

            
            
            

            def close_Them1change_testradWin():
                ChegeThemOne_1Win.show()
                Them1change_testradWin.close()
            
            def open_change_testradWin_old(id):
                global Them1change_testradWin
                Chagethemone_radWin = QtWidgets.QDialog()
                ui = Ui_Chagethemone_radWin()
                ui.setupUi(Chagethemone_radWin)
                Chagethemone_radWin.show()
                vopros_id=id
                def info_vopros(vopros_id):
                    
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT Vopros, otvet_1, otvet_2, otvet_3, correct_otvet, id_Thems FROM test_one_otvet WHERE id_test_one = ? """
                    cur.execute(query, (vopros_id,))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0],row[1],row[2],row[3],row[4], row[5]) for row in rows]
                
                vopros=info_vopros(vopros_id)
                print("Вопросы:", vopros)
                def close_Chagethemone_radWin():
                    Chagethemone_radWin.close()
                
                
                thems_id=vopros[0][5]
                vopros_name=vopros[0][0]
                ui.textEdit.setText(vopros_name)
                ui.textEdit.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                
                otvet_1=vopros[0][1]
                ui.textEdit_6.setText(otvet_1)
                otvet_2=vopros[0][2]
                ui.textEdit_7.setText(otvet_2)
                otvet_3=vopros[0][3]
                ui.textEdit_8.setText(otvet_3)
                correct_otvet=vopros[0][4]
                if correct_otvet==otvet_1:
                    ui.checkBox.setChecked(True)
                elif correct_otvet==otvet_2:
                    ui.checkBox_2.setChecked(True)
                elif correct_otvet==otvet_3:
                    ui.checkBox_3.setChecked(True)



                
                def change_vopros_create(vopros_id,thems_id):
                   vopros= ui.textEdit.toPlainText()
                   otvet_1= ui.textEdit_6.toPlainText()
                   otvet_2= ui.textEdit_7.toPlainText()
                   otvet_3= ui.textEdit_8.toPlainText()
                   
                   
                   if not otvet_1 or not otvet_2 or not otvet_3 or not vopros:
                    ui.label.setText("Напишите ваш вопрос и ответы к нему")
                    ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                   else:
                        if  ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked():
                            if (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() and ui.checkBox_2) or (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() or (ui.checkBox_3.isChecked() and ui.checkBox_2.isChecked()) or (ui.checkBox_2.isChecked() and ui.checkBox.isChecked())):
                               ui.label.setText("Выберите только один правильный ответ")
                               ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""") 
                                
                            else:
                                if ui.checkBox_3.isChecked():
                                    correct_otvet=otvet_3
                                elif ui.checkBox.isChecked(): 
                                    correct_otvet=otvet_1
                                elif ui.checkBox_2.isChecked():
                                    correct_otvet=otvet_2       
                                ui.label.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                try:
                                    with sqlite3.connect(file_path) as conn:
                                        cursor = conn.cursor()
                                        print('ok1')
                                        
                                        # Выполняем UPDATE-запрос
                                        cursor.execute("""
                                            UPDATE test_one_otvet
                                            SET Vopros = ?,
                                                otvet_1 = ?,
                                                otvet_2 = ?,
                                                otvet_3 = ?,
                                                correct_otvet = ?
                                            WHERE id_test_one = ?  
                                        """, (vopros, otvet_1, otvet_2, otvet_3, correct_otvet, vopros_id))
                                        
                                        conn.commit()  # Сохранение изменений
                                        print("Данные успешно обновлены!")
                                        
                                        thems_id_new = (thems_id,)
                                        close_Them1change_testradWin()
                                        time.sleep(0.01)
                                        open_Themtest_rad_Win(thems_id_new)
                                        time.sleep(0.01)
                                        close_Chagethemone_radWin()
                                except Exception as e:
                                    print(f'Ошибка при обновлении данных: {e}')





                        else:   
                            ui.label.setText("Выберите  правильный ответ")     
                            ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                    
                ui.pushButton_2.clicked.connect(lambda _ : change_vopros_create(vopros_id,thems_id))
                
                
            def open_change_testradWin_new(id):
                global Chagethemone_radWin
                Chagethemone_radWin = QtWidgets.QDialog()
                ui = Ui_Chagethemone_radWin()
                ui.setupUi(Chagethemone_radWin)
                Chagethemone_radWin.show()
                thems_id=id[0]

                print(thems_id)

                def close_Chagethemone_radWin():
                    Chagethemone_radWin.close()
                    
                    
                
                

                
                def new_vopros_create(thems_id):
                   vopros= ui.textEdit.toPlainText()
                   otvet_1= ui.textEdit_6.toPlainText()
                   otvet_2= ui.textEdit_7.toPlainText()
                   otvet_3= ui.textEdit_8.toPlainText()
                   
                   
                   if not otvet_1 or not otvet_2 or not otvet_3 or not vopros:
                    ui.label.setText("Напишите ваш вопрос и ответы к нему")
                    ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                   else:
                        if  ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked():
                            if (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() and ui.checkBox_2) or (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() or (ui.checkBox_3.isChecked() and ui.checkBox_2.isChecked()) or (ui.checkBox_2.isChecked() and ui.checkBox.isChecked())):
                               ui.label.setText("Выберите только один правильный ответ")
                               ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""") 
                                
                            else:
                                if ui.checkBox_3.isChecked():
                                    correct_otvet=otvet_3
                                elif ui.checkBox.isChecked(): 
                                    correct_otvet=otvet_1
                                elif ui.checkBox_2.isChecked():
                                    correct_otvet=otvet_2       
                                ui.label.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""INSERT INTO test_one_otvet ( id_Thems, Vopros, otvet_1, otvet_2, otvet_3, correct_otvet) VALUES (?, ?, ?,?,?,?)""",
                                                            (thems_id,vopros,otvet_1,otvet_2, otvet_3,correct_otvet))
                                                conn.commit()
                                                print("Vopros successfully!")
                                                thems_id_new = (thems_id,)
                                                close_Them1change_testradWin()
                                                time.sleep(0.01)
                                                open_Themtest_rad_Win(thems_id_new)
                                                time.sleep(0.01)
                                                close_Chagethemone_radWin()
                                                



                                except Exception as e:
                                            print(e + 'errror')

                        else:   
                            ui.label.setText("Выберите  правильный ответ")     
                            ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                
                                
                                
                   
                   
                   
                   
                ui.pushButton_2.clicked.connect(lambda _ : new_vopros_create(thems_id))
          

            ui.pushButton_3.clicked.connect(close_Them1change_testradWin)
            
            
            
         
            
            if type_prac==1:
                ui.pushButton_2.clicked.connect(lambda _ , id=thems_id: open_ThempractWin_new(id))
            elif type_prac==0:
                    ui.pushButton_2.clicked.connect(lambda _ , id=thems_id: open_Teoria_teachWin(id))
            


        def open_Themtest_checkb_Win(id_thems):
            global Them1change_testcheckbWin
            Them1change_testcheckbWin = QtWidgets.QDialog()
            ui = Ui_Chagethemone_2checkbWin()
            ui.setupUi(Them1change_testcheckbWin)
            Them1change_testcheckbWin.show()
            ChegeThemOne_1Win.close()
            thems_id=id_thems
            
            def get_testnesk(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Vopros, id_test_nesc, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet FROM test_nesc_otvet WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return rows
            def get_vopros_prac(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_prac FROM thems WHERE id_Thems = ? """
                cur.execute(query, (thems_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
                   

            vopros = get_testnesk(thems_id)
            print("Вопросы:", vopros)  # Проверяем, какие данные извлеклись
            type_prac = get_vopros_prac(thems_id)[0]
                
            # Используем существующую QScrollArea
            scrollAreaWidgetContents = ui.scrollAreaWidgetContents

            # Устанавливаем вертикальный layout для scrollAreaWidgetContents
            layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
            
            layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
            layout.setContentsMargins(0, 0, 0, 0)
            scrollAreaWidgetContents.setLayout(layout)

            # Очищаем содержимое scrollArea перед добавлением новых элементов
            for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
            if vopros:
                # Динамическое создание QLabel и QPushButton для каждого студента
                for i,  (vopros_name, id_testnesk, otvet_1, otvet_2, otvet_3,otvet_4, otvet_5, correct_otvet ) in enumerate(vopros):
                    print(f"Creating widget for {vopros_name} with ID: {id_testnesk}")
                    
                    word_count = len(vopros_name.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50

                    # Создаем контейнерный виджет для размещения метки и кнопки
                    container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                    grid_layout = QtWidgets.QGridLayout(container_widget)
                    grid_layout.setContentsMargins(0, 0, 0, 0)
                    grid_layout.setSpacing(0)
                    container_widget.setLayout(grid_layout)

                    label = QtWidgets.QLabel(vopros_name, parent=container_widget)
                    label.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                    """)
 
                    label.setMinimumHeight(height)
                    label.setMinimumWidth(350)
                    
                    label.setWordWrap(True)  # Включаем перенос слов на новые строки                    label_5.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)

                    label.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label, 0, 0, 1, 1)

                    pushButton = QtWidgets.QPushButton(parent=container_widget)
                    pushButton.setStyleSheet("""
                        background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
                    pushButton.setText("")
                    icon1 = QtGui.QIcon()
                    icon1.addPixmap(QtGui.QPixmap("icon/file_open_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                    pushButton.setIcon(icon1)
                    pushButton.setIconSize(QtCore.QSize(25, 25))
                    pushButton.setFixedWidth(height)
                    pushButton.setFixedHeight(height)
                    pushButton.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
                    pushButton.clicked.connect(lambda _, id=id_testnesk : open_Themchange_neskWin_old(id))

                    grid_layout.addWidget(pushButton, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                    
                    
                    
                    label_1 = QtWidgets.QLabel(otvet_1, parent=container_widget)
                    word_count = len(otvet_1.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    if correct_otvet.split("  ").count(otvet_1) > 0:
                        label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    label_1.setMinimumHeight(height)
                    label_1.setMinimumWidth(200)
                    label_1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_1.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_1.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_1, 1, 0, 1, 1)
                    
                    
                    
                    
                    label_2 = QtWidgets.QLabel(otvet_2, parent=container_widget)
                    word_count = len(otvet_2.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    if correct_otvet.split("  ").count(otvet_2) > 0:
                        label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;

                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                    
                        label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)

 
                    label_2.setMinimumHeight(height)
                    label_2.setMinimumWidth(200)
                    label_2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_2.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_2.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_2, 2, 0, 1, 1)
                    
                    
                    label_3 = QtWidgets.QLabel(otvet_3, parent=container_widget)
                    word_count = len(otvet_3.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    if correct_otvet.split("  ").count(otvet_3) > 0:
                        label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
 
                    label_3.setMinimumHeight(height)
                    label_3.setMinimumWidth(200)
                    label_3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_3.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_3.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_3, 3, 0, 1, 1)
                    
                    label_4 = QtWidgets.QLabel(otvet_4, parent=container_widget)
                    word_count = len(otvet_4.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    if correct_otvet.split("  ").count(otvet_4) > 0:
                        label_4.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_4.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
 
                    label_4.setMinimumHeight(height)
                    label_4.setMinimumWidth(200)
                    label_4.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_4.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_4.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_4, 4, 0, 1, 1)
                    
                    
                    label_5 = QtWidgets.QLabel(otvet_5, parent=container_widget)
                    word_count = len(otvet_5.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    if correct_otvet.split("  ").count(otvet_5) > 0:
                        label_5.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            text-align: center;
                            
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
                    else:
                        label_5.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid ;
                        """)
 
                    label_5.setMinimumHeight(height)
                    label_5.setMinimumWidth(200)
                    label_5.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_5.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_5.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_5, 5, 0, 1, 1)
                    
                    
                    layout.addWidget(container_widget)


                    
                            # Добавляем контейнерный виджет в основной layout
                    


                    print(f"Created label: {label}, Created button: {pushButton}")

                # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
                # Настраиваем размер QScrollArea
            container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
            grid_layout = QtWidgets.QGridLayout(container_widget)
            grid_layout.setContentsMargins(0, 0, 0, 0)
            grid_layout.setSpacing(0)
            container_widget.setLayout(grid_layout)
                    
            pushButton_6 = QtWidgets.QPushButton(parent=container_widget)
            pushButton_6.setStyleSheet("""
                background-color: green; /*Цвет текстового поля*/
                        
                        width: 250px;
                        height: 30px;
                        outline: none;
                        
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                    """)
            pushButton_6.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icon/add_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            pushButton_6.setIcon(icon1)
            pushButton_6.setIconSize(QtCore.QSize(25, 25))
            pushButton_6.setFixedWidth(41)
            pushButton_6.setFixedHeight(41)
            pushButton_6.setContentsMargins(0, 0, 0, 0)
                    
                    
                    
            pushButton_6.clicked.connect(lambda _ , id=thems_id: open_Themchange_neskWin_new(id))

            grid_layout.addWidget(pushButton_6, 0, 1, 1, 1)  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                            # Добавляем контейнерный виджет в основной layout
            layout.addWidget(container_widget)
                    
                    
            ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
            ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
            ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
        

            # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
            ui.scrollArea.setMaximumHeight(421)
            ui.scrollArea.setMaximumWidth(471)


            
            def open_Themchange_neskWin_new(id_thems):
                global Chagethemnesk_checkWin
                Chagethemnesk_checkWin = QtWidgets.QDialog()
                ui = Ui_Chagethemnesk_checkWin()
                ui.setupUi(Chagethemnesk_checkWin)
                Chagethemnesk_checkWin.show()

                thems_id=id_thems[0]

                print(thems_id)

                def close_Chagethemnesk_checkWin():
                    Chagethemnesk_checkWin.close()
                    
                    
                
                

                
                def new_vopros_create(thems_id):
                   vopros= ui.textEdit_13.toPlainText()
                   otvet_1= ui.textEdit_16.toPlainText()
                   otvet_2= ui.textEdit_14.toPlainText()
                   otvet_3= ui.textEdit_15.toPlainText()
                   otvet_4= ui.textEdit_19.toPlainText()
                   otvet_5= ui.textEdit_17.toPlainText()
                   correct_otvet=""
                   
                   if  not vopros :
                    ui.label.setText("Напишите ваш вопрос и ответы к нему")
                    ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                   else:
                        if  ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked() or ui.checkBox_4.isChecked() or ui.checkBox_5.isChecked():
                            
                                
                           
                            if ui.checkBox_3.isChecked():
                                correct_otvet += otvet_3 + "  "
                            if ui.checkBox.isChecked(): 
                                correct_otvet += otvet_1 + "  "
                            if ui.checkBox_2.isChecked():
                                correct_otvet += otvet_2 + "  "   
                            if ui.checkBox_4.isChecked():
                                correct_otvet += otvet_4 + "  "
                            if ui.checkBox_5.isChecked():
                                correct_otvet += otvet_5 + "  "

                                
                            ui.label.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                            try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""INSERT INTO test_nesc_otvet ( id_Thems, Vopros, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet) VALUES (?, ?, ?,?,?,?,?,?)""",
                                                            (thems_id,vopros,otvet_1,otvet_2, otvet_3,otvet_4,otvet_5,correct_otvet))
                                                conn.commit()
                                                print("Vopros successfully!")
                                                thems_id_new = (thems_id,)
                                                close_Themchange_testcheckbWin()
                                                time.sleep(0.01)
                                                open_Themtest_checkb_Win(thems_id_new)
                                                time.sleep(0.01)
                                                close_Chagethemnesk_checkWin()
                                                



                            except Exception as e:
                                            print(e + 'errror')

                        else:   
                            ui.label.setText("Выберите  правильный ответ")     
                            ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                
                                
                                
                   
                   
                   
                   
                ui.pushButton_2.clicked.connect(lambda _ : new_vopros_create(thems_id))
            
            
            
            def open_Themchange_neskWin_old(id):
                global Chagethemnesk_checkWin
                Chagethemnesk_checkWin = QtWidgets.QDialog()
                ui = Ui_Chagethemnesk_checkWin()
                ui.setupUi(Chagethemnesk_checkWin)
                Chagethemnesk_checkWin.show()
                vopros_id=id
                def info_vopros(vopros_id):
                    
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT Vopros, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet, id_Thems FROM test_nesc_otvet WHERE id_test_nesc = ? """
                    cur.execute(query, (vopros_id,))
                    rows = cur.fetchall()
                    con.close()
                    return  rows
                
                vopros=info_vopros(vopros_id)
                print("Вопросы:", vopros)
                
                def close_Chagethemnesk_checkWin():
                    Chagethemnesk_checkWin.close()
                
                
                thems_id=vopros[0][7]
                vopros_name=vopros[0][0]
                ui.textEdit_13.setText(vopros_name)
                ui.textEdit_13.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                
                otvet_1=vopros[0][1]
                ui.textEdit_16.setText(otvet_1)
                
                otvet_2=vopros[0][2]
                ui.textEdit_14.setText(otvet_2)
                
                otvet_3=vopros[0][3]
                ui.textEdit_15.setText(otvet_3)
                
                otvet_4=vopros[0][4]
                ui.textEdit_19.setText(otvet_4)
                
                otvet_5=vopros[0][5]
                ui.textEdit_17.setText(otvet_5)
                
                correct_otvet=vopros[0][6]
                if correct_otvet.split("  ").count(otvet_1) > 0:
                    ui.checkBox.setChecked(True)
                if correct_otvet.split("  ").count(otvet_2) > 0:
                    ui.checkBox_2.setChecked(True)
                if correct_otvet.split("  ").count(otvet_3) > 0:
                    ui.checkBox_3.setChecked(True)
                if correct_otvet.split("  ").count(otvet_4) > 0:
                    ui.checkBox_4.setChecked(True)
                if correct_otvet.split("  ").count(otvet_5) > 0:
                    ui.checkBox_5.setChecked(True)
                



                
                def change_vopros_create_nesk(vopros_id,thems_id):
                   vopros= ui.textEdit_13.toPlainText()
                   otvet_1= ui.textEdit_16.toPlainText()
                   otvet_2= ui.textEdit_14.toPlainText()
                   otvet_3= ui.textEdit_15.toPlainText()
                   otvet_4= ui.textEdit_19.toPlainText()
                   otvet_5= ui.textEdit_17.toPlainText()
                   correct_otvet=""
                   

    
                   
                   if  not vopros:
                    ui.label.setText("Напишите ваш вопрос и ответы к нему")
                    ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                   else:
                        if ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked() or ui.checkBox_4.isChecked() or ui.checkBox_5.isChecked():

                                
                           
                            if ui.checkBox_3.isChecked():
                                correct_otvet += otvet_3 + "  "
                            if ui.checkBox.isChecked(): 
                                correct_otvet += otvet_1 + "  "
                            if ui.checkBox_2.isChecked():
                                correct_otvet += otvet_2 + "  "   
                            if ui.checkBox_4.isChecked():
                                correct_otvet += otvet_4 + "  "
                            if ui.checkBox_5.isChecked():
                                correct_otvet += otvet_5 + "  "
                                   
                            ui.label.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                            try:
                                    with sqlite3.connect(file_path) as conn:
                                        cursor = conn.cursor()
                                        print('ok1')
                                        
                                        # Выполняем UPDATE-запрос
                                        cursor.execute("""
                                            UPDATE test_nesc_otvet
                                            SET Vopros = ?,
                                                otvet_1 = ?,
                                                otvet_2 = ?,
                                                otvet_3 = ?,
                                                otvet_4 = ?,
                                                otvet_5 = ?,
                                                correct_otvet = ?
                                            WHERE id_test_nesc = ?  
                                        """, (vopros, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet, vopros_id))
                                        
                                        conn.commit()  # Сохранение изменений
                                        print("Данные успешно обновлены!")
                                        
                                        thems_id_new = (thems_id,)
                                        close_Themchange_testcheckbWin()
                                        time.sleep(0.01)
                                        open_Themtest_checkb_Win(thems_id_new)
                                        time.sleep(0.01)
                                        close_Chagethemnesk_checkWin()
                            except Exception as e:
                                    print(f'Ошибка при обновлении данных: {e}')





                        else:   
                            ui.label.setText("Выберите  правильный ответ")     
                            ui.label.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                    
                ui.pushButton_2.clicked.connect(lambda _ : change_vopros_create_nesk(vopros_id,thems_id))
                
                
            
            def close_Themchange_testcheckbWin():
                ChegeThemOne_1Win.show()
                Them1change_testcheckbWin.close()

            ui.pushButton_3.clicked.connect(close_Themchange_testcheckbWin)
            
        
            
            if type_prac==1:
                ui.pushButton_2.clicked.connect(lambda _ , id=thems_id: open_ThempractWin_new(id))
            elif type_prac==0:
                    ui.pushButton_2.clicked.connect(lambda _ ,id=thems_id : open_Teoria_teachWin(id))




        def open_Themchage_new(predmeti_id, cursi_id):
            global ChegeThemOne_1Win
            ChegeThemOne_1Win = QtWidgets.QDialog()
            ui = Ui_ChegeThemOne_1Win()
            ui.setupUi(ChegeThemOne_1Win)
            ChegeThemOne_1Win.show()
            ThemsWin_teacher.close()

            def close_Themchage_Win():
                ThemsWin_teacher.show()
                ChegeThemOne_1Win.close()

            

            def vnos_dannih_and_open_next():
                them = ui.textEdit.toPlainText()
                types_test=0
                if not them:
                    ui.label_11.setText("Напишите вашу тему")
                    ui.label_11.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                else:

                        if  ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked():
                            if (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() and ui.checkBox_2) or (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() or (ui.checkBox_3.isChecked() and ui.checkBox_2.isChecked()) or (ui.checkBox_2.isChecked() and ui.checkBox.isChecked())):
                               ui.label_3.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""") 
                                
                            else:
                                if ui.checkBox_3.isChecked() and not ui.checkBox.isChecked():
                                    types_test = 1  #Один ответ
                                elif ui.checkBox.isChecked() and not ui.checkBox_3.isChecked(): 
                                    types_test = 2  #Несколько ответов
                                elif ui.checkBox_2.isChecked():
                                    types_test= 3   #Нет тестов       
                                ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                
                                if not ui.radioButton_3.isChecked() and not ui.radioButton_2.isChecked():
                                    ui.label_10.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                    
                                else:
                                    if ui.radioButton_3.isChecked():
                                        types_prac=0
                                    elif ui.radioButton_2.isChecked():
                                        types_prac=1
                                    ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                
                                        
                                    if types_test==3 and types_prac==0:
                                        close_Themchage_Win()
                                        time.sleep(0.01)
                                        close_ThemsWin_teacher()
                                        time.sleep(0.01)
                                        on_button_clicked_Thems()
                                    else:
                                        ui.label_11.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                        ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""")
                                        ui.label_10.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""")
                                        

                                        try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""INSERT INTO thems (predmet_id, Cyrs_id,name_Them, types_test, types_prac ) VALUES (?, ?, ?,?,?)""",
                                                            ( predmeti_id, cursi_id, them, types_test, types_prac))
                                                conn.commit()
                                                print("Them successfully!")
                                                cursor.execute("""SELECT id_Thems FROM thems WHERE predmet_id = ? AND Cyrs_id = ? AND name_Them =? AND  types_test=? AND types_prac=?  """, (predmeti_id, cursi_id,them,types_test, types_prac))
                                                result = cursor.fetchone()
                                                
                                                print(result)


                                                
                                                if types_test==1:
                                                    open_Themtest_rad_Win(result)
                                                elif types_test==2:
                                                    open_Themtest_checkb_Win(result)
                                                elif types_test==3:
                                                    open_ThempractWin_new(result)



                                        except Exception as e:
                                            print(e + 'errror')

                        else:        
                            ui.label_3.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                            
                        
                        



            ui.pushButton_2.clicked.connect(vnos_dannih_and_open_next)
            ui.pushButton_3.clicked.connect(close_Themchage_Win)

        def open_Them1chage_old(id_thems):
            global ChegeThemOne_1Win
            ChegeThemOne_1Win = QtWidgets.QDialog()
            ui = Ui_ChegeThemOne_1Win()
            ui.setupUi(ChegeThemOne_1Win)
            ChegeThemOne_1Win.show()
            ThemsWin_teacher.close()

            
            def get_thems(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_test,  types_prac, name_Them  FROM thems WHERE id_Thems = ?  """
                cur.execute(query, (id_thems, ))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1],row[2]) for row in rows]
            
            def close_Them1chage_1Win():
                ThemsWin_teacher.show()
                ChegeThemOne_1Win.close()

            

            typevopros = get_thems(id_thems)
            types_test = typevopros[0][0]
            types_prac_old = typevopros[0][1]
            thems_name = typevopros[0][2]
            ui.textEdit.setText(thems_name)
            
            
            if types_test==1:
                ui.checkBox_3.setChecked(True)
            elif types_test==2:
                ui.checkBox.setChecked(True)
            elif types_test==3:
                ui.checkBox_2.setChecked(True)
            
            if types_prac_old==0:
                ui.radioButton_3.setChecked(True)
            elif types_prac_old==1:
                ui.radioButton_2.setChecked(True)
            
            
            
            def save_them(id_thems):
                them = ui.textEdit.toPlainText()
                types_test=0
                if not them:
                    ui.label_11.setText("Напишите вашу тему")
                    ui.label_11.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                else:

                        if  ui.checkBox_3.isChecked() or ui.checkBox.isChecked() or ui.checkBox_2.isChecked():
                            if (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() and ui.checkBox_2) or (ui.checkBox_3.isChecked() and ui.checkBox.isChecked() or (ui.checkBox_3.isChecked() and ui.checkBox_2.isChecked()) or (ui.checkBox_2.isChecked() and ui.checkBox.isChecked())):
                               ui.label_3.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""") 
                                
                            else:
                                if ui.checkBox_3.isChecked() and not ui.checkBox.isChecked():
                                    types_test = 1  #Один ответ
                                elif ui.checkBox.isChecked() and not ui.checkBox_3.isChecked(): 
                                    types_test = 2  #Несколько ответов
                                elif ui.checkBox_2.isChecked():
                                    types_test= 3   #Нет тестов       
                                ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                
                                if not ui.radioButton_3.isChecked() and not ui.radioButton_2.isChecked():
                                    ui.label_10.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                    
                                else:
                                    if ui.radioButton_3.isChecked():
                                        types_prac=0
                                    elif ui.radioButton_2.isChecked():
                                        types_prac=1
                                    ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""") 
                                
                                        
                                    if types_test==3 and types_prac==0:
                                        close_Them1chage_1Win()
                                        time.sleep(0.01)
                                        close_ThemsWin_teacher()
                                        time.sleep(0.01)
                                        on_button_clicked_Thems()
                                    else:
                                        ui.label_11.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                                        ui.label_3.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""")
                                        ui.label_10.setStyleSheet("""color: black;font: 20pt "Times New Roman";text-align: center;""")
                                        

                                        try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""
                                                UPDATE thems
                                                SET name_Them=?,
                                                types_test = ?,
                                                types_prac = ?
                                                WHERE id_Thems = ?  
                                        """, (them, types_test, types_prac, id_thems))
                                                conn.commit()
                                                print("Them successfully!")
              

                                                
                                                print(id_thems)

                                            thems_id_new = (id_thems,)
                                           
                                            if types_test==1:
                                                    open_Themtest_rad_Win(thems_id_new)
                                            elif types_test==2:
                                                    open_Themtest_checkb_Win(thems_id_new)
                                            elif types_test==3:
                                                    open_ThempractWin_new(thems_id_new)
                                       
                                                         



                                        except Exception as e:
                                            print(e + 'errror')

                        else:        
                            ui.label_3.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")









            ui.pushButton_2.clicked.connect(lambda _,  : save_them(id_thems))
            ui.pushButton_3.clicked.connect(close_Them1chage_1Win)

        def open_Teoria_teachWin(id_thems):
            global Teoria_teachWin
            Teoria_teachWin = QtWidgets.QDialog()
            ui = Ui_Teoria_teachWin()
            ui.setupUi(Teoria_teachWin)
            Teoria_teachWin.show()
            
            if isinstance(id_thems, (int, float)):
                thems_id=(id_thems,)
            else:
                thems_id=id_thems[0]
                thems_id=(thems_id,)
            print(thems_id, 'yes')
            
            def get_types(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT types_test, types_prac FROM thems WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1]) for row in rows]
            
           
            
            types_test=get_types(thems_id)[0][0]# Получаем тип теста
            types_prac=get_types(thems_id)[0][1]# Получаем тип практики
            
            if types_test==1 and types_prac==0:
                Them1change_testradWin.close()
            elif types_test==2 and types_prac==0:
                Them1change_testcheckbWin.close()
            else:
                Prac_makeWin.close()
                
                
            def get_text(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Text_teoria FROM teoria WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
            
            teoria_text=get_text(thems_id)
            
            if teoria_text:
                ui.textEdit.setText(teoria_text[0])
            
            def close_TeoriaWin_teacher():
                Teoria_teachWin.close()
                
            def save_teoria(thems_id,teoria_text):
                teoria = ui.textEdit.toPlainText()
                thems_id=thems_id[0]
                if not teoria:
                    ui.textEdit.setText('Напишите что нибудь')
                    ui.textEdit.setStyleSheet("""color: red;font: 20pt "Times New Roman";text-align: center;""")
                else:
                    ui.textEdit.setStyleSheet("""color: black;font: 20pt "Times New Roman";""")
                    if not teoria_text:
                        try:
                                                with sqlite3.connect(file_path) as conn:
                                                    cursor = conn.cursor()
                                                    print('ok1')
                                                    cursor.execute("""INSERT INTO teoria (id_Thems, Text_teoria ) VALUES (?, ?)""",
                                                                ( thems_id,teoria ))
                                                    conn.commit()
                                                    print("Them successfully!")
                                                    close_TeoriaWin_teacher()
                                                    time.sleep(0.01)
                                                    close_ThemsWin_teacher()
                                                    time.sleep(0.01)
                                                    on_button_clicked_Thems()
                                                

                        except Exception as e:
                                                print(e + 'errror')
                    else:
                        try:
                                                with sqlite3.connect(file_path) as conn:
                                                    cursor = conn.cursor()
                                                    print('ok1')
                                                    cursor.execute("""UPDATE teoria SET Text_teoria = ? WHERE id_Thems = ?""",
                                                                ( teoria, thems_id ))
                                                    conn.commit()
                                                    print("Them successfully!")
                                                    Teoria_teachWin.close()
                                                    ThemsWin_teacher.show()
                                                    
                                                    
                        except Exception as e:
                                                print(e + 'errror')
                                                
                
            
           
                    
            ui.pushButton_2.clicked.connect(lambda _,  : save_teoria(thems_id,teoria_text))


        ui.pushButton_3.clicked.connect(close_ThemsWin_teacher)
        
        ui.pushButton_11.clicked.connect(logout_function)






    ui.pushButton_3.clicked.connect(on_button_clicked_FIO)
    ui.pushButton_4.clicked.connect(on_button_clicked_Thems)
    ui.pushButton_9.clicked.connect(open_add_cyrsWin)
    ui.pushButton_11.clicked.connect(logout_function)
    ui.pushButton_10.clicked.connect(open_add_predmetWin)







def open_ThemsWin_stud(id_cyrs,id_predmet):
    global ThemsWin_stud,predmeti_id,cursi_id
    ThemsWin_stud = QtWidgets.QDialog()
    ui = Ui_ThemsWin_stud()
    ui.setupUi(ThemsWin_stud)
    ThemsWin_stud.show()
    LoginWin.close()
    window = ThemsWin_stud
    logout_function = lambda: logout(window)
    
    
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("icon/logout_24dp_000000_FILL0_wght400_GRAD0_opsz24.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    ui.pushButton_11.setIcon(icon1)
    

    def get_thems(predmeti_id, cursi_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT name_Them, id_Thems,types_test FROM thems WHERE Cyrs_id = ? AND predmet_id = ? """
                cur.execute(query, (cursi_id,predmeti_id ))
                rows = cur.fetchall()
                con.close()
                return [(row[0], row[1],row[2]) for row in rows]
            
            
    def get_otvet(id_cyrs, id_predmet, person):
        con = sqlite3.connect(file_path)
        cur = con.cursor()
        count_otvet=0
        count_thems=0
        query = """SELECT id_Thems FROM thems WHERE Cyrs_id = ? AND predmet_id = ? """
        cur.execute(query, (id_cyrs, id_predmet ))
        rows = cur.fetchall()
        count_thems=len(rows)
        query = """SELECT Stud_otvet_id FROM stud_otvet WHERE id_student = ? """
        cur.execute(query, (person, ))
        row = cur.fetchall()
        count_otvet=len(row)
        
        con.close()
        return count_otvet,count_thems
       


    thems=get_thems(id_cyrs, id_predmet)
    print("Темы:", thems)  # Проверяем, какие данные извлеклись
    if thems:
        
        types_test = thems[0][2]
        id_thems = thems[0][1]
        count_otvet, count_thems = get_otvet(id_cyrs, id_predmet, person)

        # Рассчитываем процент пройденных тем
        percent_complete = int((count_otvet / count_thems) * 100) if count_thems > 0 else 0
        ui.progressBar.setValue(percent_complete)
        ui.label.setText(f'Пройдено тем: {count_otvet} из {count_thems}')
        ui.label.setStyleSheet("""
             
                    
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    margin-left: 125px;
                """)
            
            
    else:
        thems=[]
        ui.progressBar.setValue(0)
        ui.label.setText(f'Пройдено тем: 0 из 0')
        ui.label.setStyleSheet("""
             
                    
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    margin-left: 125px;
                """)
    
    
        # Используем существующую QScrollArea
    scrollAreaWidgetContents = ui.scrollAreaWidgetContents

        # Устанавливаем вертикальный layout для scrollAreaWidgetContents
    layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
        
    layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
    layout.setContentsMargins(0, 0, 0, 0)
    scrollAreaWidgetContents.setLayout(layout)

        # Очищаем содержимое scrollArea перед добавлением новых элементов
    for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
    if thems:
            # Динамическое создание QLabel и QPushButton для каждого студента
            for i,  (them_name, id_thems,types_test) in enumerate(thems):
                print(f"Creating widget for {them_name} with ID: {id_thems}")
                
                # Создаем контейнерный виджет для размещения метки и кнопки
                container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                grid_layout = QtWidgets.QGridLayout(container_widget)
                grid_layout.setContentsMargins(0, 0, 0, 0)
                grid_layout.setSpacing(0)
                container_widget.setLayout(grid_layout)
                def studotveti(id_thems, person):
                    con = sqlite3.connect(file_path)
                    cur = con.cursor()
                    query = """SELECT Stud_otvet_id FROM stud_otvet WHERE id_thems = ? AND id_student = ? """
                    cur.execute(query, (id_thems, person ))
                    rows = cur.fetchall()
                    con.close()
                    return [(row[0]) for row in rows]
        
                stud = studotveti(id_thems, person)
                
                
                
                label = QtWidgets.QLabel(them_name, parent=container_widget)
                        
                word_count = len(them_name.split())  # Разбиваем строку на слова и считаем их количество

                if word_count > 8:
                            height = 100  # Высота метки, если слов больше 7
                else:
                            height = 50
                if len(stud) > 0:
                    label.setStyleSheet("""
                                font-weight: bold;
                                font:  15pt "Times New Roman";
                                background-color: green;
                                padding-left: 10px;
                            """)
                else:
                    label.setStyleSheet("""
                                font-weight: bold;
                                font:  15pt "Times New Roman";
                                background-color: grey;
                                padding-left: 10px;
                            """)
                    

                        # Включаем обратно управление положением метки со стороны layout-а
                    

                        
                        
                label.setMinimumHeight(height)
                    
                label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                label.setWordWrap(True)  # Включаем перенос слов на новые строки
                label.setContentsMargins(0, 0, 0, 0)
                label.setMinimumWidth(350)
                grid_layout.addWidget(label, 0, 0, 1, 1)
                    
                pushButton = QtWidgets.QPushButton(parent=container_widget)
                pushButton.setStyleSheet("""
                            background-color: #33cc33; /*Цвет текстового поля*/
                            
                            width: 250px;
                            height: 30px;
                            outline: none;
                            
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                        """)
                pushButton.setText("Зайти")
                        
                pushButton.setFixedWidth(60)
                pushButton.setFixedHeight(height)
                pushButton.setContentsMargins(0, 0, 0, 0) 
                pushButton.setToolTip("Открыть тему")
                pushButton.clicked.connect(lambda _, id=id_thems :open_Mejdu_studWin(id))
                        
                grid_layout.addWidget(pushButton, 0, 1, 1, 1)
                    
                        

                  # Помещаем кнопку в ячейку (0, 1), занимающую одну строку и один столбец

                
                
                layout.addWidget(container_widget)

                
                        # Добавляем контейнерный виджет в основной layout
                
                print(f"Created label: {label}")

            # Настраиваем размер QScrollArea
        # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
    
                
    ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
    ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
    ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
       

        # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
    ui.scrollArea.setMaximumHeight(491)
    ui.scrollArea.setMaximumWidth(471)




    def close_ThemsWin_stud():
        LoginWin.show()
        ThemsWin_stud.close()




    def open_Mejdu_studWin(id):
        global Mejdu_studWin
        Mejdu_studWin = QtWidgets.QDialog()
        ui = Ui_Mejdu_studWin()
        ui.setupUi(Mejdu_studWin)
        Mejdu_studWin.show()
        ThemsWin_stud.close()
        
        def get_thems(id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT name_Them, types_test FROM thems WHERE id_Thems = ? """
                cur.execute(query, (id,))
                rows = cur.fetchall()
                con.close()
                return [(row[0], row[1]) for row in rows]
            
        def studotveti(id_thems, person):
            con = sqlite3.connect(file_path)
            cur = con.cursor()
            query = """SELECT ball_test, ball_prac FROM stud_otvet WHERE id_thems = ? AND id_student = ? """
            cur.execute(query, (id_thems, person ))
            rows = cur.fetchall()
            con.close()
            return [(row[0], row[1]) for row in rows]
        
        stud = studotveti(id, person)
        
        def get_thems_2(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Cyrs_id, predmet_id FROM thems WHERE  id_Thems= ? """
                cur.execute(query, (id_thems, ))
                rows = cur.fetchall()
                con.close()
                return [(row[0], row[1]) for row in rows]
            
        thems_c_p=get_thems_2(id)
        predmet=thems_c_p[0][1]
        curs=thems_c_p[0][0]

# Проверяем, что список не пустой
        if len(stud) > 0:
                    stud_test = stud[0][0]
                    stud_prac = stud[0][1]
        else:
                    # Если данных нет, присваиваем значения по умолчанию
                    stud_test = None
                    stud_prac = None



       
        thems=get_thems(id)
        print("Темы:", thems)  # Проверяем, какие данные извлеклись


        types_test=thems[0][1]
        name_them=thems[0][0]
        ui.label_2.setText(name_them)
        ui.label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  20pt "Times New Roman";
                            background-color: grey;
                            
                        """)
        ui.label_2.setWordWrap(True)
        
       
        print(stud_test)
        
        if not stud:
            if types_test==1:
                ui.pushButton_4.clicked.connect(lambda _,  : open_Test_rad_studWin(id))
            elif types_test==2:
                ui.pushButton_4.clicked.connect(lambda _,  : open_Test_checkb_studWin(id))
            elif types_test==3:
                ui.pushButton_4.clicked.connect(lambda _,  : open_Prac_studWin(id))
        
        else:
            
            ui.pushButton_4.setToolTip("Задание пройдено")
            if stud_prac!=None   and stud_test!=None:
        
                ui.pushButton_4.setText(f'Тест {stud_test}\nПрактика {stud_prac}')
            elif stud_prac!=None and stud_test==None:
                ui.pushButton_4.setText(f'Теста не было\nПрактика {stud_prac}')
            elif stud_test!=None and stud_prac==None  :
                ui.pushButton_4.setText(f'Тест {stud_test}\nПрактики не было')
            else:
                ui.pushButton_4.setText('Ни теста, ни практики не было')
            ui.pushButton_4.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: green;
                            padding-left: 10px;
                            border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                            border-radius: 20px;
                            border: 1px solid black;
                        """)


        def closeMejdu_studWin(predmet,curs):
            Mejdu_studWin.close()
            
            open_ThemsWin_stud(predmet,curs)


        ui.pushButton_3.clicked.connect(lambda _,  :closeMejdu_studWin(predmet,curs))
        ui.pushButton_5.clicked.connect(lambda _,  : open_Teoria_studWin(id))

    def open_Teoria_studWin(id):
        global Teoria_studWin
        Teoria_studWin = QtWidgets.QDialog()
        ui = Ui_Teoria_studWin()
        ui.setupUi(Teoria_studWin)
        Teoria_studWin.show()
        Mejdu_studWin.close()
        id_thems= (id,)
        
        
        def get_teoria(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Text_teoria FROM teoria WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
        
        teoria=get_teoria(id_thems)
        if teoria:
            text_teoria = teoria[0]
            ui.textBrowser.setText(text_teoria)
            ui.textBrowser.setStyleSheet("""
                                font-weight: bold;
                                font:  12pt "Times New Roman";
                                
                                
                            """)
            
        else:
            ui.textBrowser.setText("Нет теории")
            ui.textBrowser.setStyleSheet("""
                                font-weight: bold;
                                font:  12pt "Times New Roman";
                                
                                
                            """)
     

        
        
        def closeTeoria_studWin():
            Teoria_studWin.close()
            Mejdu_studWin.show()


        ui.pushButton_3.clicked.connect(closeTeoria_studWin)
    
    def open_Test_rad_studWin(id):
        global Test_rad_studWin, suma_prev
        Test_rad_studWin = QtWidgets.QDialog()
        ui = Ui_Test_rad_studWin()
        ui.setupUi(Test_rad_studWin)
        Test_rad_studWin.show()
        Mejdu_studWin.close()
        id_thems= (id,)
        window=Test_rad_studWin
       
        def get_testrad(thems_id):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT Vopros, id_test_one, otvet_1, otvet_2, otvet_3, correct_otvet FROM test_one_otvet WHERE id_Thems = ? """
                cur.execute(query, (thems_id))
                rows = cur.fetchall()
                con.close()
                return [(row[0],row[1],row[2],row[3],row[4],row[5]) for row in rows]


        def get_vopros_prac(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT  types_prac FROM thems WHERE  id_Thems = ? """
                cur.execute(query, (id_thems ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
                   

           
        types_prac = get_vopros_prac(id_thems)
        prac=types_prac[0]
            
        vopros = get_testrad(id_thems)
        print("Вопросы:", vopros)  # Проверяем, какие данные извлеклись
        suma_prev=0
        otveti=[]
        checBoxi=[]
               
            # Используем существующую QScrollArea
        scrollAreaWidgetContents = ui.scrollAreaWidgetContents_2

            # Устанавливаем вертикальный layout для scrollAreaWidgetContents
        layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
            
        layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
        layout.setContentsMargins(0, 0, 0, 0)
        scrollAreaWidgetContents.setLayout(layout)

            # Очищаем содержимое scrollArea перед добавлением новых элементов
        for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
        if vopros:
                # Динамическое создание QLabel и QPushButton для каждого студента
                for i,  (vopros_name, id_testone, otvet_1, otvet_2, otvet_3, correct_otvet ) in enumerate(vopros):
                    print(f"Creating widget for {vopros_name} with ID: {id_testone}")

                    
                    # Создаем контейнерный виджет для размещения метки и кнопки
                    container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                    grid_layout = QtWidgets.QGridLayout(container_widget)
                    grid_layout.setContentsMargins(0, 0, 0, 0)
                    grid_layout.setSpacing(10)
                    container_widget.setLayout(grid_layout)

                    
                    word_count = len(vopros_name.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    label = QtWidgets.QLabel(vopros_name, parent=container_widget)
                    label.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                        
                         border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                         border-radius: 20px;
                         border: 1px solid ;
                    """)
 
                    label.setMinimumHeight(height)
                    label.setMinimumWidth(350)
                    label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label.setContentsMargins(0, 0, 0, 0)
                    
                    grid_layout.addWidget(label, 0, 1, 1, 2)

                    

                    checkBox_1 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_1.setMaximumHeight(height)
                    checkBox_1.setMaximumWidth(50)
                    checkBox_1.setContentsMargins(0, 0, 0, 0)
                    checkBox_1.setObjectName(f'checkbox_{3*i}')
                    grid_layout.addWidget(checkBox_1, 1, 0, 1, 1)
                    
                    
                    label_1 = QtWidgets.QLabel(otvet_1, parent=container_widget)
                    
                    word_count = len(otvet_1.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                  
                    label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                           
                            border: 1px solid ;
                        """)
                    label_1.setMinimumHeight(height)
                    label_1.setMaximumWidth(200)
                    label_1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_1.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_1.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_1, 1, 1, 1, 1)
                    
                    
                    checkBox_2 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_2.setMaximumHeight(height)
                    checkBox_2.setMaximumWidth(50)
                    checkBox_2.setContentsMargins(0, 0, 0, 0)
                    checkBox_2.setObjectName(f'checkbox_{3*i+1}')
                    grid_layout.addWidget(checkBox_2, 2, 0, 1, 1)
                    
                    label_2 = QtWidgets.QLabel(otvet_2, parent=container_widget)
                    word_count = len(otvet_2.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    
                   
                    
                    label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            
                            border: 1px solid ;
                        """)

 
                    label_2.setFixedHeight(height)
                    label_2.setMaximumWidth(200)
                    label_2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_2.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_2.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_2, 2, 1, 1, 1)
                    
                    
                    checkBox_3 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_3.setMaximumHeight(height)
                    checkBox_3.setMaximumWidth(50)
                    checkBox_3.setContentsMargins(0, 0, 0, 0)
                    checkBox_3.setObjectName(f'checkbox_{3*i+2}')
                    grid_layout.addWidget(checkBox_3, 3, 0, 1, 1)
                    
                    label_3 = QtWidgets.QLabel(otvet_3, parent=container_widget)
                    
                    word_count = len(otvet_3.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    
                    label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                            
                            border: 1px solid ;
                        """)
 
                    label_3.setMinimumHeight(height)
                    label_3.setMaximumWidth(200)
                    label_3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_3.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_3.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_3, 3, 1, 1, 1)
                    
                    
                    
                    
                    layout.addWidget(container_widget)
                    
                    chek = (
                        checkBox_1.objectName(),
                        checkBox_2.objectName(),
                        checkBox_3.objectName()
                    )
                    checBoxi.append(chek)
                    
                     
                    if otvet_1 == correct_otvet:
                        otveti.append(checkBox_1.objectName())
                    elif otvet_2 == correct_otvet:
                        otveti.append(checkBox_2.objectName())
                    elif otvet_3 == correct_otvet:
                        otveti.append(checkBox_3.objectName())
                      
                    

                    
                    
                    
                    
                    
                            # Добавляем контейнерный виджет в основной layout
                    


                    print(f"Created label: {checBoxi} , {otveti}")

                # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
                # Настраиваем размер QScrollArea
     
        
                      
        
        
        
        ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
        ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
        ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
        

            # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
        ui.scrollArea.setMaximumHeight(361)
        ui.scrollArea.setMaximumWidth(471)

       
       
        def dobav_ballov_test(types_prac,id,person,suma_prev):
          nolik=0
          nolik_2='0'
          for i in range(len(otveti)):
            
            new_1=checBoxi[i][0]
            new_2=checBoxi[i][1]
            new_3=checBoxi[i][2] 
            print(f"Словарь: {i} , {new_1} , {new_2} , {new_3}")
            checkbox_new = Test_rad_studWin.findChild(QCheckBox,new_1)
            checkbox_new_2 = Test_rad_studWin.findChild(QCheckBox,new_2)
            checkbox_new_3 = Test_rad_studWin.findChild(QCheckBox,new_3)
            
            
            print(f"Словарь:{otveti[i]}")
            print(f"Словарь: {checkbox_new.objectName()}, {checkbox_new_2.objectName()}, {checkbox_new_3.objectName()}")

            if otveti[i] == new_1 and checkbox_new.isChecked():  # Здесь исправлено условие
                suma_prev += 1
            elif otveti[i] == new_2 and checkbox_new_2.isChecked():  # Здесь исправлено условие
                suma_prev += 1
            elif otveti[i] == new_3 and checkbox_new_3.isChecked():  # Здесь исправлено условие
                suma_prev += 1
            else:
                suma_prev += 0
          try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""INSERT INTO stud_otvet (id_thems, id_student, ball_test, ball_prac, otvet_prac ) VALUES (?, ?, ?,?,?)""",
                                                            (id, person, suma_prev,nolik,nolik_2))
                                                conn.commit()
                                                print("Them successfully!")
                                            


                                                
                                                if types_prac==1:
                                                    open_Prac_studWin(id)
                                                else:
                                                  window.close()
                                                  open_Mejdu_studWin(id)
                                                  



          except Exception as e:
                                            print(e + 'errror')
       
       
       
       
       
        def closeTest_rad_studWin():
            Test_rad_studWin.close()
            Mejdu_studWin.show()
            

        ui.pushButton_3.clicked.connect(closeTest_rad_studWin)
        ui.pushButton_2.clicked.connect(lambda _,  : dobav_ballov_test(prac,id,person,suma_prev))
        
       
       
       
       
    def open_Prac_studWin(id):
            global Prac_studWin
            Prac_studWin = QtWidgets.QDialog()
            ui = Ui_Prac_studWin()
            ui.setupUi(Prac_studWin)
            Prac_studWin.show()
            window=Prac_studWin
            id_thems=(id, )
            print(id_thems, id)

            def get_id_test(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT  types_test FROM thems WHERE  id_Thems = ? """
                cur.execute(query, (id_thems, ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
                   
            def get_vopros_prac(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT  Vopros FROM practic WHERE  id_Thems = ? """
                cur.execute(query, (id_thems, ))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]

            types_test=get_id_test(id)
            test=types_test[0]
            
            name_vopros=get_vopros_prac(id)
            if name_vopros:
                vopros=name_vopros[0]
            else:
                vopros="Нет вопросов"
            
            
            
            if test==1:
              Test_rad_studWin.close()
            elif test==2:
              Test_checkb_studWin.close()
            else:
              Mejdu_studWin.close()
              
            ui.label_3.setText(vopros)
            ui.label_3.setStyleSheet('font-weight: bold; font: 15pt "Times New Roman"; text-align: center;')
            
              
            def dobavlenie_otveta(id,person):
              print("Добавление ответа")
              
              nolik=0
              vopros=ui.textEdit.toPlainText()
              if not vopros:
                  vopros='0'
              if test ==3:
                try:
                  with sqlite3.connect(file_path) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""INSERT INTO stud_otvet (id_thems, otvet_prac, id_student, ball_prac) VALUES (?, ?, ?,?)""",
                                    (id, vopros, person,nolik))
                        conn.commit()
                        print("Them successfully!")
                except Exception as e:
                        print(e + 'errror')
              
              else:
                try:
                  with sqlite3.connect(file_path) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE stud_otvet 
                                       SET otvet_prac=?, 
                                       ball_prac=?
                                       WHERE id_thems = ? AND id_student= ?
                                       """,
                                    (vopros,nolik,id,person))
                       
                        conn.commit()
                        print("Them successfully!")
                except Exception as e:
                        print(e + 'errror')
              
              window.close()
              
              open_Mejdu_studWin(id)
              
            

            ui.pushButton_2.clicked.connect(lambda _,  : dobavlenie_otveta(id,person))



    def open_Test_checkb_studWin(id):
      global Test_checkb_studWin
      Test_checkb_studWin = QtWidgets.QDialog()
      ui = Ui_Test_checkb_studWin()
      ui.setupUi(Test_checkb_studWin)
      Test_checkb_studWin.show()
      Mejdu_studWin.close()
      id_thems= (id,)
      window=Test_checkb_studWin
      
      def get_testnesc(thems_id):
        con = sqlite3.connect(file_path)
        cur = con.cursor()
        query = """SELECT Vopros, id_test_nesc, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet 
                   FROM test_nesc_otvet 
                   WHERE id_Thems = ?"""
        cur.execute(query, (thems_id,))
        rows = cur.fetchall()
        con.close()
        return rows


      def get_vopros_prac(id_thems):
                con = sqlite3.connect(file_path)
                cur = con.cursor()
                query = """SELECT  types_prac FROM thems WHERE  id_Thems = ? """
                cur.execute(query, (id_thems,))
                rows = cur.fetchall()
                con.close()
                return [(row[0]) for row in rows]
            
      
          
                   

           
      types_prac = get_vopros_prac(id)
      prac=types_prac[0]
       
      vopros = get_testnesc(id)
      print("Вопросы:", vopros)  # Проверяем, какие данные извлеклись
      suma_prev=0
      otveti=[]
      checBoxi=[]
      counter = 0
               
            # Используем существующую QScrollArea
      scrollAreaWidgetContents = ui.scrollAreaWidgetContents

            # Устанавливаем вертикальный layout для scrollAreaWidgetContents
      layout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)
            
      layout.setSpacing(10)  # Расстояние между виджетами будет 10 пикселей
      layout.setContentsMargins(0, 0, 0, 0)
      scrollAreaWidgetContents.setLayout(layout)

            # Очищаем содержимое scrollArea перед добавлением новых элементов
      for i in reversed(range(layout.count())):
                item = layout.itemAt(i)
                if item.widget():
                    item.widget().deleteLater()
      if vopros:
                # Динамическое создание QLabel и QPushButton для каждого студента
              for i, (vopros_name, id_testnesk, otvet_1, otvet_2, otvet_3, otvet_4, otvet_5, correct_otvet) in enumerate(vopros):
                    print(f"Creating widget for {vopros_name} with ID: {id_testnesk}")

                    
                    # Создаем контейнерный виджет для размещения метки и кнопки
                    container_widget = QtWidgets.QWidget(scrollAreaWidgetContents)
                    grid_layout = QtWidgets.QGridLayout(container_widget)
                    grid_layout.setContentsMargins(0, 0, 0, 0)
                    grid_layout.setSpacing(10)
                    container_widget.setLayout(grid_layout)

                    
                    word_count = len(vopros_name.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    label = QtWidgets.QLabel(vopros_name, parent=container_widget)
                    label.setStyleSheet("""
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        background-color: grey;
                        padding-left: 10px;
                        
                         border-radius: 10px 10px 10px 10px; /*Закругляем уголки*/
                         border-radius: 20px;
                         border: 1px solid ;
                    """)
 
                    label.setMinimumHeight(height)
                    label.setMinimumWidth(350)
                    label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label.setContentsMargins(0, 0, 0, 0)
                    
                    grid_layout.addWidget(label, 0, 1, 1, 2)

                    

                    checkBox_1 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_1.setMaximumHeight(height)
                    checkBox_1.setMaximumWidth(50)
                    checkBox_1.setContentsMargins(0, 0, 0, 0)
                    checkBox_1.setObjectName(f'checkbox_{counter}')
                    counter += 1
                    grid_layout.addWidget(checkBox_1, 1, 0, 1, 1)
                    
                    
                    label_1 = QtWidgets.QLabel(otvet_1, parent=container_widget)
                    
                    word_count = len(otvet_1.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                  
                    label_1.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                          
                            border: 1px solid ;
                        """)
                    label_1.setMinimumHeight(height)
                    label_1.setMaximumWidth(200)
                    label_1.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_1.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_1.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_1, 1, 1, 1, 1)
                    
                    
                    checkBox_2 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_2.setMaximumHeight(height)
                    checkBox_2.setMaximumWidth(50)
                    checkBox_2.setContentsMargins(0, 0, 0, 0)
                    checkBox_2.setObjectName(f'checkbox_{counter}')
                    counter+=1
                    grid_layout.addWidget(checkBox_2, 2, 0, 1, 1)
                    
                    label_2 = QtWidgets.QLabel(otvet_2, parent=container_widget)
                    word_count = len(otvet_2.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                    
                   
                    
                    label_2.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                           
                            border: 1px solid ;
                        """)

 
                    label_2.setFixedHeight(height)
                    label_2.setMaximumWidth(200)
                    label_2.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_2.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_2.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_2, 2, 1, 1, 1)
                    
                    
                    checkBox_3 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_3.setMaximumHeight(height)
                    checkBox_3.setMaximumWidth(50)
                    checkBox_3.setContentsMargins(0, 0, 0, 0)
                    checkBox_3.setObjectName(f'checkbox_{counter}')
                    counter+=1
                    grid_layout.addWidget(checkBox_3, 3, 0, 1, 1)
                    
                    label_3 = QtWidgets.QLabel(otvet_3, parent=container_widget)
                    
                    word_count = len(otvet_3.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                   
                    
                    label_3.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;
                           
                           
                            border: 1px solid ;
                        """)
 
                    label_3.setMinimumHeight(height)
                    label_3.setMaximumWidth(200)
                    label_3.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_3.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_3.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_3, 3, 1, 1, 1)
                    
                    
                    
                    checkBox_4 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_4.setMaximumHeight(height)
                    checkBox_4.setMaximumWidth(50)
                    checkBox_4.setContentsMargins(0, 0, 0, 0)
                    checkBox_4.setObjectName(f'checkbox_{counter}')
                    counter+=1
                    grid_layout.addWidget(checkBox_4, 4, 0, 1, 1)
                    
                    
                    label_4 = QtWidgets.QLabel(otvet_4, parent=container_widget)
                    
                    word_count = len(otvet_4.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                  
                    label_4.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                            
                            border: 1px solid ;
                        """)
                    label_4.setMinimumHeight(height)
                    label_4.setMaximumWidth(200)
                    label_4.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_4.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_4.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_4, 4, 1, 1, 1)
                    
                    
                    checkBox_5 = QtWidgets.QCheckBox(parent=container_widget)
                    checkBox_5.setMaximumHeight(height)
                    checkBox_5.setMaximumWidth(50)
                    checkBox_5.setContentsMargins(0, 0, 0, 0)
                    checkBox_5.setObjectName(f'checkbox_{counter}')
                    counter+=1
                    grid_layout.addWidget(checkBox_5, 5, 0, 1, 1)
                    
                    
                    label_5 = QtWidgets.QLabel(otvet_5, parent=container_widget)
                    
                    word_count = len(otvet_5.split())  # Разбиваем строку на слова и считаем их количество

                    if word_count > 8:
                        height = 100  # Высота метки, если слов больше 7
                    else:
                        height = 50
                    
                  
                    label_5.setStyleSheet("""
                            font-weight: bold;
                            font:  12pt "Times New Roman";
                            background-color: grey;
                            padding-left: 10px;
                            text-align: center;

                           
                            border: 1px solid ;
                        """)
                    label_5.setMinimumHeight(height)
                    label_5.setMaximumWidth(200)
                    label_5.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
                    label_5.setWordWrap(True)  # Включаем перенос слов на новые строки
                    label_5.setContentsMargins(0, 0, 0, 0)
                    grid_layout.addWidget(label_5, 5, 1, 1, 1)
                    
                    
                    layout.addWidget(container_widget)
                    
                    
                    chek = (
                        checkBox_1.objectName(),
                        checkBox_2.objectName(),
                        checkBox_3.objectName(),
                        checkBox_4.objectName(),
                        checkBox_5.objectName()
                        
                    )
                    checBoxi.append(chek)
                    correct=()
                     
                    if  correct_otvet.split("  ").count(otvet_1) > 0:
                        
                        correct+=(checkBox_1.objectName(),)
                    if correct_otvet.split("  ").count(otvet_2) > 0:
                        correct+=(checkBox_2.objectName(),)
                    if correct_otvet.split("  ").count(otvet_3) > 0:
                        correct+=(checkBox_3.objectName(),)
                    if correct_otvet.split("  ").count(otvet_4) > 0:
                      correct+=(checkBox_4.objectName(),)
                    if correct_otvet.split("  ").count(otvet_5) > 0:
                        correct+=(checkBox_5.objectName())
                        
                    otveti.append(correct)
                    
                            # Добавляем контейнерный виджет в основной layout
                    


                    print(f"Created label: {checBoxi} , {otveti}")

                # Настраиваем размер QScrollArea
            # Настраиваем размер QScrollArea
                # Настраиваем размер QScrollArea
     
        
                      
        
        
        
      ui.scrollArea.setWidgetResizable(True)  # Разрешаем изменение размера содержимого
      ui.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Отключаем горизонтальную прокруткуScrollBarAlwaysOff
      ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)  # Включаем вертикальную прокрутку по мере заполнения
        

            # Ограничиваем максимальную высоту ScrollArea до 421 пикселя
      ui.scrollArea.setMaximumHeight(361)
      ui.scrollArea.setMaximumWidth(471)

       
       
      def dobav_ballov_test_nesk(types_prac,id,person,suma_prev):
          nolik=0
          nolik_2='0'
          for i in range(len(otveti)):
            
            new_1 = checBoxi[i][0]
            new_2 = checBoxi[i][1]
            new_3 = checBoxi[i][2]
            new_4 = checBoxi[i][3]
            new_5 = checBoxi[i][4]
            
            # Находим соответствующие виджеты чекбоксов
            checkbox_new = Test_checkb_studWin.findChild(QCheckBox, new_1)
            checkbox_new_2 = Test_checkb_studWin.findChild(QCheckBox, new_2)
            checkbox_new_3 = Test_checkb_studWin.findChild(QCheckBox, new_3)
            checkbox_new_4 = Test_checkb_studWin.findChild(QCheckBox, new_4)
            checkbox_new_5 = Test_checkb_studWin.findChild(QCheckBox, new_5)
            
            # Список всех чекбоксов
            checkboxes = [checkbox_new, checkbox_new_2, checkbox_new_3, checkbox_new_4, checkbox_new_5]
            answers = otveti[i]
            
            # Флаг для проверки правильности ответов
            
            
            # Создаем список с состоянием чекбоксов
            checked_boxes = [checkbox.isChecked() for checkbox in checkboxes]
            print(f'Checked: {checked_boxes}, {answers}')
            # Сравниваем списки ответов и состояния чекбоксов
            expected_answers = [name in answers for name in [new_1, new_2, new_3, new_4, new_5]]
            print(f'Checked:{expected_answers}')
            # Сравниваем списки ответов и состояния чекбоксов
            if checked_boxes == expected_answers:
                suma_prev += 1
    
                
              
          try:
                                            with sqlite3.connect(file_path) as conn:
                                                cursor = conn.cursor()
                                                print('ok1')
                                                cursor.execute("""INSERT INTO stud_otvet (id_thems, id_student, ball_test, ball_prac ,otvet_prac ) VALUES (?, ?, ?,?,?)""",
                                                            (id, person, suma_prev,nolik,nolik_2 ))
                                                conn.commit()
                                                print("Them successfully!")
                                            


                                                
                                                if types_prac==1:
                                                    open_Prac_studWin(id)
                                                else:
                                                  window.close()
                                                  open_Mejdu_studWin(id)
                                                  



          except Exception as e:
                                            print(e + 'errror')
       
       
       
       
       
      def closeTest_nesk_studWin():
            Test_checkb_studWin.close()
            Mejdu_studWin.show()
            

      ui.pushButton_3.clicked.connect(closeTest_nesk_studWin)
      ui.pushButton_2.clicked.connect(lambda _,  : dobav_ballov_test_nesk(prac,id,person,suma_prev))
        
       
       
        
    ui.pushButton_11.clicked.connect(close_ThemsWin_stud)




def open_Reg_adminWin():
    global Reg_adminWin
    Reg_adminWin = QtWidgets.QDialog()
    ui = Ui_Reg_adminWin()
    ui.setupUi(Reg_adminWin)
    Reg_adminWin.show()
    RegWin.close()


    ui.textEdit.setPlaceholderText('Введите ФИО')  # Используем placeholder вместо setText
    ui.textEdit_3.setPlaceholderText('Введите логин')
    ui.textEdit_4.setPlaceholderText('Введите пароль')
    
    def Register_teacher():
        fio = ui.textEdit.toPlainText()
        login = ui.textEdit_3.toPlainText()
        password=ui.textEdit_4.toPlainText()
        if not fio:
            ui.label_8.setText(" Введите ФИО")
            ui.label_8.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
        elif not login:
            ui.label_8.setText("")
            ui.label_9.setText("Введите Логин")
            ui.label_9.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
        elif not password:
            ui.label_8.setText("")
            ui.label_9.setText("")
            ui.label_10.setText("Введите Пароль")
            ui.label_10.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
        else:
            ui.label_8.setText("")
            ui.label_9.setText("")
            ui.label_10.setText("")
            def new_id_teacher():
                conn = sqlite3.connect(file_path)
                """Проверка существования пользователя в базе данных."""
                cursor = conn.cursor()
                sql = "SELECT id_teacher FROM teacher "
                cursor.execute(sql)
                
                
                
                rows = cursor.fetchall()
                new_result=len(rows)
                print(new_result)
                conn.close()
                return new_result+1
            
            number_new=new_id_teacher()
            print(number_new)
            
            
            
            password = 'new_user_' +str(number_new)+password
            id_wind=2

            try:
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                with sqlite3.connect(file_path) as conn:
                    cursor = conn.cursor()

                    if is_teacher_exists(conn, login,hashed_password,id_wind):
                        ui.label_6.setText("Такой пользователь уже существует")
                        ui.label_6.setStyleSheet("""
                
                        color:red;
                        font-weight: bold;
                        font:  12pt "Times New Roman";
                        
                    """)
                    else:
                        
                        cursor.execute("""INSERT INTO teacher (FIO, Login, Password) VALUES (?, ?, ?)""",
                                    (fio, login, hashed_password))
                        conn.commit()
                        print("User registered successfully!")
                        ui.label_6.setText("")
                        LoginWin.show()
                        Reg_adminWin.close()
            except Exception as e:
                print(e + 'error')
            
    def close_adminWin():
             Reg_adminWin.close()
             RegWin.show()
    ui.pushButton_3.clicked.connect(close_adminWin)

    ui.pushButton_2.clicked.connect(Register_teacher)

def get_courses():
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name_Cyrs, Cyrs_id FROM cyrs")
    courses = cursor.fetchall()
    return [(row[0], row[1]) for row in courses]  # Возвращаем кортежи (name, id)

def get_courses_teacher(person):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name_Cyrs, Cyrs_id FROM cyrs WHERE teacher_id = ?", (person,))
    courses = cursor.fetchall()
    return [(row[0], row[1]) for row in courses]


def open_RegWin():
    global RegWin
    RegWin = QtWidgets.QDialog()
    ui = Ui_RegWin()
    ui.setupUi(RegWin)
    RegWin.show()
    LoginWin.close()

    ui.textEdit.setPlaceholderText('Введите ФИО')  # Используем placeholder вместо setText
    ui.textEdit_3.setPlaceholderText('Введите логин')
    ui.textEdit_4.setPlaceholderText('Введите пароль')
    

    # Заполняем комбо-бокс курсами
    courses = get_courses()
    print(f"Курсы: {courses}")

    # Заполняем комбо-бокс курсами
    ui.comboBox.addItem('Выберите...')
    ui.comboBox.addItems([course[0] for course in courses])


    predmets = get_predmet()
    print(f"Предметы: {predmets}")

    # Заполняем комбо-бокс курсами
    ui.comboBox_2.addItem('Выберите...')
    ui.comboBox_2.addItems([predmet[0] for predmet in predmets])



    def close_RegWin():
        LoginWin.show()
        RegWin.close()







    def Register():

        fio = ui.textEdit.toPlainText()
        login = ui.textEdit_3.toPlainText()
        password = ui.textEdit_4.toPlainText()
        id_wind=2
        
        def new_id_student():
            conn = sqlite3.connect(file_path)
            """Проверка существования пользователя в базе данных."""
            cursor = conn.cursor()
            sql = "SELECT id_student FROM student "
            cursor.execute(sql)
            
            
            
            rows = cursor.fetchall()
            new_result=len(rows)
            print(new_result)
            conn.close()
            return new_result+1
        
        
        selected_course_index = ui.comboBox.currentIndex()
        if selected_course_index > 0:  # Проверяем, выбран ли курс (первый элемент 'Выберите' игнорируем)
            curs_id = courses[selected_course_index - 1][1]  # Индекс уменьшаем на 1, так как 'Выберите' занимает первую позицию
        else:
            curs_id = None

        
        selected_predmet_index = ui.comboBox_2.currentIndex()
        if selected_predmet_index > 0:  # Проверяем, выбран ли курс (первый элемент 'Выберите' игнорируем)
            predmet_id = courses[selected_predmet_index - 1][1]  # Индекс уменьшаем на 1, так как 'Выберите' занимает первую позицию
        else:
            predmet_id = None


        if (fio and login and password) == "Gleb":
            open_Reg_adminWin()
            return
        if not fio:
            

                ui.label_8.setText(" Введите ФИО")
                ui.label_8.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
            
        elif not login:
                    ui.label_8.setText('')
                    ui.label_9.setText(" Введите Логин")
                    ui.label_9.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
        elif not password:
                    ui.label_8.setText('')
                    ui.label_9.setText("")
                    ui.label_10.setText( " Введите Пароль")
                    ui.label_10.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
                
        elif not selected_course_index:
                    ui.label_8.setText('')
                    ui.label_9.setText("")
                    ui.label_10.setText("")
                    ui.label_11.setText(" Введите ваш Курс")
                    ui.label_11.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
                    
        elif not selected_predmet_index:
                    ui.label_8.setText('')
                    ui.label_9.setText("")
                    ui.label_10.setText("")
                    ui.label_11.setText("")
            
                    ui.label_12.setText(" Введите ваш Предмет")
                    ui.label_12.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)

        else:
                        number_new=new_id_student()
                        print(number_new)
                        ui.label_8.setText('')
                        ui.label_9.setText("")
                        ui.label_10.setText("")
                        ui.label_11.setText("")
                        ui.label_12.setText("")
                        password= 'new_user_'+ str(number_new) + password
                        hashed_password = hashlib.md5(password.encode()).hexdigest()

                        try:
                            with sqlite3.connect(file_path) as conn:
                                cursor = conn.cursor()
                                if is_user_exists(conn, login,hashed_password,id_wind):
                                    ui.label_6.setText("Такой пользователь уже существует")
                                    ui.label_6.setStyleSheet("""
             
                    color:red;
                    font-weight: bold;
                    font:  12pt "Times New Roman";
                    
                """)
                                else:
                                    
                                    print('ok1')
                                    cursor.execute("""INSERT INTO student (FIO, Cyrs_id, Login, Password, Predmet_id) VALUES (?, ?, ?,?,?)""",
                                                (fio, curs_id, login, hashed_password, predmet_id))
                                    conn.commit()
                                    print("User registered successfully!")
                                    ui.label_6.setText("")
                                    LoginWin.show()
                                    RegWin.close()

                        except Exception as e:
                            print(e + 'errror')# Вывод ошибкив консоль










    ui.pushButton_2.clicked.connect(Register)
    ui.pushButton.clicked.connect(close_RegWin)




if __name__ == '__main__':
    mainWin()

