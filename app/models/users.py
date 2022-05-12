class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    
    @property
    def username(self):
        return self._username


    @username.setter
    def username(self, new_username):
        self._username = new_username


    @property
    def password(self):
        return self._password


class UserDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor


    def select_all_users(self):
        select_all_query = """
            SELECT * from users;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()

    
    def select_user_by_username(self, username):
        select_user_by_username = """
            SELECT * from users WHERE username = %s;
        """
        self._cursor.execute(select_user_by_username, (username,))
        return self._cursor.fetchone()

    
    def select_user_by_password(self, password):
        select_user_by_password = """
            SELECT * from users WHERE username = %s;
        """
        self._cursor.execute(select_user_by_password, (password,))
        return self._cursor.fetchone()

    
    def select_user_by_id(self, user_id):
        select_user_by_id = """
            SELECT * from users WHERE user_id = %s;
            """
        self._cursor.execute(select_user_by_id, (user_id,))
        return self._cursor.fetchone()


    def insert_user(self, user):
        insert_query = """
            INSERT INTO users (username, password)
            VALUES (%s, %s);
            """
        
        self._cursor.execute(insert_query, (user.username, user.password))
        self._cursor.execute("SELECT LAST_INSERT_ID() user_id")
        user_id = self._cursor.fetchone()
        self._db_conn.commit()
        return user_id


    def update_user(self, user_id, new_user):
        update_query = """
            UPDATE users
            SET username = %s
            WHERE user_id = %s;
        """

        self._cursor.execute(update_query, (new_user.username, user_id))
        self._db_conn.commit()


    def delete_user_by_id(self, user_id):
        delete_query = """
            DELETE from users
            WHERE user_id = %s;
        """

        self._cursor.execute(delete_query, (user_id,))
        self._db_conn.commit()
