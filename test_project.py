import pytest
import os
from project import is_valid_email, is_strong_password, encrypt, decrypt

def test_is_valid_email():
    # Valid emails
    assert is_valid_email("david_j.malan@example.com") is not None
    assert is_valid_email("sankar.addala2004@example.co.in") is not None
    assert is_valid_email("cs50p@example.edu") is not None
    # Invalid emails
    assert is_valid_email(".doeexample.com") is None
    assert is_valid_email("john@depp123@in.co.uk") is None
    assert is_valid_email("kim+smith@example.") is None


def test_is_strong_password():
    #Valid passwords
    assert is_strong_password("John@5272") is not None
    assert is_strong_password("24%J_2sfa7g") is not None
    #Invalid passwords
    assert is_strong_password("StrongPassword") is None
    assert is_strong_password("2*96a1987") is None
    assert is_strong_password("D2$a") is None


def test_encrypt():
    key = 8
    #Valid outputs
    assert encrypt("CS50 Final Project", key) == "KA50 Nqvit Xzwrmkb"
    assert encrypt("How are you?", key) == "Pwe izm gwc?"
    assert encrypt("This is my project", key) == "Bpqa qa ug xzwrmkb"
    #Invalid outputs
    assert encrypt("hello", key) != "hello"
    assert encrypt("My project", key) != "ab cdefghi"
    assert encrypt("Encrypt", key) != "Decrypt"


def test_decrypt():
    key = 8
    #Valid outputs
    assert decrypt("KA50 Nqvit Xzwrmkb", key) == "CS50 Final Project"
    assert decrypt("Pwe izm gwc?", key) == "How are you?"
    assert decrypt("Bpqa qa ug xzwrmkb", key) == "This is my project"
    #Invalid outputs
    assert decrypt("hello", key) != "hello"
    assert decrypt("ab cdefghi", key) != "My project"
    assert decrypt("yn asdf", key) != "hello guys"