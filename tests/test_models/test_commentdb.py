from app.models.comments import Comment, CommentDB
from app.models.posts import Post, PostDB
from app.models.users import User, UserDB

# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_comment_insert(db_test_client):
    # The test fixture only setups the 
    conn, cursor = db_test_client
    commentdb = CommentDB(conn, cursor)
    postdb = PostDB(conn, cursor)
    userdb = UserDB(conn, cursor)

    userdb.insert_user(User("test_username", "test_password"))
    user_id = cursor.lastrowid

    postdb.insert_post(Post("test title", "test content", user_id))
    post_id = cursor.lastrowid

    test_comment = Comment("Test Text", post_id)

    commentdb.insert_comment(test_comment)

    result = commentdb.select_comment_by_id(1)

    assert result['text'] == "Test Text"
    assert result['post_id'] == post_id

    conn.commit()


def test_comment_delete(db_test_client):
    conn, cursor = db_test_client
    commentdb = CommentDB(conn, cursor)
    postdb = PostDB(conn, cursor)
    userdb = UserDB(conn, cursor)

    userdb.insert_user(User("test_username_delete", "test_password_delete"))
    user_id = cursor.lastrowid

    postdb.insert_post(Post("test title_delete", "test content_delete", user_id))
    post_id = cursor.lastrowid

    test_comment = Comment("Delete Test Text", post_id)

    commentdb.insert_comment(test_comment)

    result = commentdb.select_comment_by_id(2)

    assert result['text'] == "Delete Test Text"
    assert result['post_id'] == post_id

    commentdb.delete_comment_by_id(2)

    result = commentdb.select_comment_by_id(2)
    assert result is None
    conn.commit()
