import pytest
from datetime import datetime

from app.models.posts import Post 

def test_post_constructor():
    title = "Test Title"
    content = "Test Content"
    user_id = 1
    p = Post(title, content, user_id)
    assert p.title == title
    assert p.content == content
    assert p.user_id == user_id 

def test_post_properties():
    title = "Property Test Title"
    content = "Property Test Content"
    user_id = 1

    p = Post(title, content, user_id)
    assert p.title == title
    assert p.content == content
    assert p.user_id == user_id 
    
    new_title = "New Property Test Title"
    new_content = "New Property Test Content"

    p.title = new_title
    p.content= new_content

    assert p.title == new_title    
    assert p.content == new_content
