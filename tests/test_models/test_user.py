import pytest
from datetime import datetime

from app.models.users import User

def test_user_constructor():
    username = "test_username"
    password = "test_password"

    u = User(username, password)
    assert u.username == username 
    assert u.password == password 

def test_user_properties():
    username = "test_username"
    password = "test_password"
    desc = "Test task properties"

    u = User(username, password)

    assert u.username == username 
    assert u.password == password 
    
    new_username = "new_test_username"

    u.username = new_username

    assert u.username == new_username