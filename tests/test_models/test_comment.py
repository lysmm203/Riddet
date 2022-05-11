import pytest
from datetime import datetime

from app.models.comments import Comment

def test_comment_constructor():

    text = "Test Comment"
    post_id = "Test Post ID"
    user_id = "Test User ID"

    c = Comment(text, post_id, user_id)
    assert c.text == text
    assert c.post_id == post_id
    assert c.user_id == user_id

def test_comment_properties():
    text = "Test Comment"
    post_id = "Test Post ID"
    user_id = "Test User ID"

    c = Comment(text, post_id, user_id)
    assert c.text == text
    assert c.post_id == post_id
    assert c.user_id == user_id

    new_text = "New Test Comment"

    c.text = new_text
    assert c.text == new_text