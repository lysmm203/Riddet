class Post:
    def __init__(self, title, content, user_id):
        self._title = title
        self._content = content
        self._user_id = user_id

    
    @property
    def title(self):
        return self._title

    
    @title.setter
    def title(self, new_title):
        self._title = new_title

    
    @property
    def content(self):
        return self._content


    @content.setter
    def content(self, new_content):
        self._content = new_content


    @property
    def user_id(self):
        return self._user_id


class PostDB:
    def __init__(self, db_conn, db_cursor):
        self._db_conn = db_conn
        self._cursor = db_cursor


    def select_all_posts(self):
        select_all_query = """
            SELECT * from posts;
        """
        self._cursor.execute(select_all_query)

        return self._cursor.fetchall()

    
    def select_posts_by_user_id(self, user_id):
        select_posts_by_user_id = """
            SELECT * from posts WHERE user_id = %s;
        """
        self._cursor.execute(select_posts_by_user_id, (user_id,))
        return self._cursor.fetchall()

    
    def select_post_by_title(self, title):
        select_post_by_title = """
            SELECT * from posts WHERE title = %s;
        """
        self._cursor.execute(select_post_by_title, (title,))
        return self._cursor.fetchone()

    
    def select_post_by_id(self, post_id):
        select_post_by_id = """
            SELECT * from posts WHERE post_id = %s;
            """
        self._cursor.execute(select_post_by_id, (post_id,))
        return self._cursor.fetchone()


    def insert_post(self, post):
        insert_query = """
            INSERT INTO posts (title, content, user_id)
            VALUES (%s, %s, %s);
            """
        
        self._cursor.execute(insert_query, (post.title, post.content, post.user_id))
        self._cursor.execute("SELECT LAST_INSERT_ID() post_id")
        post_id = self._cursor.fetchone()
        self._db_conn.commit()
        return post_id


    def update_post(self, post_id, new_post):
        update_query = """
            UPDATE posts
            SET content = %s
            WHERE post_id = %s;
        """

        self._cursor.execute(update_query, (new_post.content, post_id))
        self._db_conn.commit()


    def delete_post_by_id(self, post_id):
        delete_query = """
            DELETE from posts
            WHERE post_id = %s;
        """

        self._cursor.execute(delete_query, (post_id,))
        self._db_conn.commit()
