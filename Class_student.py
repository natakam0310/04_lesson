from sqlalchemy import create_engine, text

class Class_student:
    __scripts = {
        "delete_user_id": text("DELETE FROM users WHERE user_id = :user_id"),
        "insert_new": text(
            "INSERT INTO users (user_email, subject_id, user_id) "
            "VALUES (:new_user_email, :new_subject_id, :new_user_id)"
        ),
        "update_user_id": text(
            "UPDATE users SET user_id = :new_user_id WHERE user_id = :old_user_id"
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def check_connection(self):
        try:
            with self.__db.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                for row in result:
                    print("Соединение с БД успешно, ответ:", row[0])
                return True
        except Exception as e:
            print("Ошибка соединения с БД:", e)
            return False

    def create(self, user_email, subject_id, user_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["insert_new"], {
                    "new_user_email": user_email,
                    "new_subject_id": subject_id,
                    "new_user_id": user_id
                })
        print("Пользователь создан")

    def delete(self, user_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["delete_user_id"], {"user_id": user_id})
        print("Пользователь удалён") 

    def update_user_id(self, old_user_id, new_user_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(self.__scripts["update_user_id"], {
                    "old_user_id": old_user_id,
                    "new_user_id": new_user_id
                })
        print(f"user_id изменён с {old_user_id} на {new_user_id}")