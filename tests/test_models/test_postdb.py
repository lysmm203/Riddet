from app.models.posts import Post, PostDB
from app.models.users import User, UserDB

# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_post_insert(db_test_client):
    # The test fixture only setups the 
    conn, cursor = db_test_client
    postdb = PostDB(conn, cursor)

    title = "Test Title"
    content = "Test Content"

    userdb = UserDB(conn, cursor)

    user = User("test_acc", "test_acc")
    userdb.insert_user(user)
    user_id = cursor.lastrowid 

    test_post = Post(title, content, user_id)

    postdb.insert_post(test_post)
    
    result = postdb.select_post_by_id(1)
    
    assert result['title'] == title
    assert result['content'] == content
    assert result['user_id'] == user_id
    conn.commit()


def test_post_delete(db_test_client):
    
    conn, cursor = db_test_client
    postdb = PostDB(conn, cursor)

    title = "Delete Post Title"
    content = "Delete Post Content"

    userdb = UserDB(conn, cursor)

    user = User("test_acc2", "test_acc2")
    userdb.insert_user(user)
    user_id = cursor.lastrowid 

    test_post = Post(title, content, user_id)

    result = postdb.select_post_by_id(2)

    assert result is None 

    postdb.insert_post(test_post)
    
    result = postdb.select_post_by_id(2)
    
    assert result['title'] == title
    assert result['content'] == content 
    assert result['user_id'] == user_id
    conn.commit()

    postdb.delete_post_by_id(2)
    result = postdb.select_post_by_id(2)
    assert result is None
    conn.commit()