class Comment:
    def __init__(self, text, post_id, user_id):
        self._text = text
        self._post_id = post_id
        self._user_id = user_id

    
    @property
    def text(self):
        return self._text

    
    @text.setter
    def text(self, new_text):
        self._text = new_text

    
    @property
    def post_id(self):
        return self._post_id


    @property
    def user_id(self):
        return self._user_id


class CommentDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor


    def select_all_comments(self):
        select_all_query = """
            SELECT * from comments;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()

    
    def select_comments_by_user_id(self, user_id):
        select_comments_by_user_id = """
            SELECT * from comments WHERE user_id = %s;
        """
        self._cursor.execute(select_comments_by_user_id, (user_id,))
        return self._cursor.fetchall()


    def select_comments_by_post_id(self, post_id):
        select_comments_by_post_id = """
            SELECT * from comments WHERE post_id = %s;
        """
        self._cursor.execute(select_comments_by_post_id, (post_id,))
        return self._cursor.fetchall()

    
    def select_comment_by_id(self, comment_id):
        select_post_by_id = """
            SELECT * from comments WHERE comment_id = %s;
            """
        self._cursor.execute(select_post_by_id, (comment_id,))
        return self._cursor.fetchone()


    def insert_comment(self, comment):
        insert_query = """
            INSERT INTO comments (text, post_id, user_id)
            VALUES (%s, %s, %s);
            """
        
        self._cursor.execute(insert_query, (comment.text, comment.post_id, comment.user_id))
        self._cursor.execute("SELECT LAST_INSERT_ID() comment_id")
        comment_id = self._cursor.fetchone()
        self._db_conn.commit()
        return comment_id


    def update_comment(self, comment_id, new_comment):
        update_query = """
            UPDATE comments
            SET text = %s
            WHERE comment_id = %s;
        """

        self._cursor.execute(update_query, (new_comment.text, comment_id))
        self._db_conn.commit()


    def delete_comment_by_id(self, comment_id):
        delete_query = """
            DELETE from comments
            WHERE comment_id = %s;
        """

        self._cursor.execute(delete_query, (comment_id,))
        self._db_conn.commit()
