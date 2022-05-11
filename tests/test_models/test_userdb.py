from app.models.users import User, UserDB

# By using the parameter db_test_client, we automatically get access to our test
#   database provided by the pytest fixture in conftest.py
#   (note the parameter name matches the name of the fixture function).
def test_user_insert(db_test_client):
    # The test fixture only setups the 
    conn, cursor = db_test_client
    userdb = UserDB(conn, cursor)

    test_user = User("test_username", "test_password")

    userdb.insert_user(test_user)

    result = userdb.select_user_by_id(1)[0]

    assert result['username'] == "test_username"
    assert result['password'] == "test_password"

    conn.commit()


def test_task_delete(db_test_client):
    conn, cursor = db_test_client
    userdb = UserDB(conn, cursor)
    
    test_user = User("delete_username", "delete_password")

    userdb.insert_user(test_user)

    result = userdb.select_user_by_id(2)[0]
    assert result['username'] == "delete_username"
    assert result['password'] == "delete_password"

    userdb.delete_user_by_id(2)
    result = userdb.select_user_by_id(2)
    assert len(result) == 0
    
    conn.commit()
