from Class_student import Class_student

def test_new_student():
    db_connection_string = "postgresql://postgres:Dimasik2401@localhost:5432/QA"
    db = Class_student(db_connection_string)

    if not db.check_connection():
        print("Подключение не удалось, проверьте строку подключения и БД")
        return

    user_email = "natak358@mail.ru"
    subject_id = 3
    user_id = 853

    # Создание пользователя
    db.create(user_email, subject_id, user_id)

    # нужно удалить пользователя
    db.delete(user_id)

def test_edit_student():
    db_connection_string = "postgresql://postgres:Dimasik2401@localhost:5432/QA"
    db = Class_student(db_connection_string)

    if not db.check_connection():
        print("Подключение не удалось, проверьте строку подключения и БД")
        return

    user_email = "natak358@mail.ru"
    subject_id = 3
    user_id = 853

    # Создание пользователя
    db.create(user_email, subject_id, user_id)

    # Изменение user_id
    new_user_id = 362
    db.update_user_id(old_user_id=user_id, new_user_id=new_user_id)

    # Удаление изменённого пользователя
    db.delete(new_user_id)





