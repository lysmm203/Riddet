import pytest
from datetime import datetime

from app.models.comments import Comment
from app.models.posts import Post

def test_comment_constructor():

    text = "Test Comment"
    post_id = "Test Post ID"

    c = Comment(text, post_id)
    assert c.text == text
    assert c.post_id == post_id

def test_comment_properties():
    text = "Test Comment"
    post_id = "Test Post ID"

    c = Comment(text, post_id)
    assert c.text == text
    assert c.post_id == post_id

    new_text = "New Test Comment"

    c.text = new_text
    assert c.text == new_text