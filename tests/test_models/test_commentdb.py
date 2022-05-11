from app.models.comments import Comment, CommentDB

# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_comment_insert(db_test_client):
    # The test fixture only setups the 
    conn, cursor = db_test_client
    commentdb = CommentDB(conn, cursor)

    test_comment = Comment("Test Text", 1, 2)

    commentdb.insert_comment(test_comment)

    result = commentdb.select_comment_by_id(1)[0]

    assert result['text'] == "Test Text"
    assert result['post_id'] == 1
    assert result['user_id'] == 2

    conn.commit()


def test_comment_delete(db_test_client):
    conn, cursor = db_test_client
    commentdb = CommentDB(conn, cursor)

    test_comment = Comment("Delete Test Text", 3, 4)

    commentdb.insert_comment(test_comment)

    result = commentdb.select_comment_by_id(2)[0]

    assert result['text'] == "Delete Test Text"
    assert result['post_id'] == 3
    assert result['user_id'] == 4

    commentdb.delete_comment_by_id(2)

    result = commentdb.select_comment_by_id(2)[0]
    assert len(result) == 0
    conn.commit()
