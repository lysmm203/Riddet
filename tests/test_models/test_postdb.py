from app.models.posts import Post, PostDB

# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_post_insert(db_test_client):
    # The test fixture only setups the 
    conn, cursor = db_test_client
    postdb = PostDB(conn, cursor)

    postdb.insert_post(Post("Test Title", "Test Content", 1))
    
    result = postdb.select_post_by_id(1)[0]
    
    assert result['title'] == "Test Title"
    assert result['content'] == "Test Content"
    assert result['user_id'] == 1
    conn.commit()


def test_task_delete(db_test_client):
    conn, cursor = db_test_client
    postdb = PostDB(conn, cursor)

    postdb.insert_post(Post("Test Title", "Test Content", 1))
    
    result = postdb.select_post_by_id(2)[0]
    
    assert result['title'] == "Test Title"
    assert result['content'] == "Test Content"
    assert result['user_id'] == 1
    conn.commit()

    postdb.delete_post_by_id(2)
    result = postdb.select_post_by_id(2)[0]
    assert len(result) == 0
    conn.commit()
