from get_all_questions import show_all_questions
from post_a_question import post_a_question
import pytest
import os

def test_get(client):
    rv = client.get('/')
    assert b'data read' in rv.data
def test_post(client):
    rs = client.post('/')
    assert b 'entries made' in rv.data