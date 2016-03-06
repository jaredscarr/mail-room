# -*- coding: utf-8 -*-
import pdb
import pytest


VAL_MAIN = [
    ('S', 'S'),
    ('C', 'C'),
]

VAL_NAMES = [
    ('jared', 'jared'),
    ('alex', 'alex'),
    ('fred', 'fred'),
    ('phil', 'phil'),
    (878, False),
    # ({'jared': [5, 445, 500]}),
    # ({'alex': [1000, 2, 10]}),
]

VAL_DON = [
    (333, 333),
    (356, 356),
    (234, 234),
]


@pytest.mark.parametrize('string, result', VAL_MAIN)
def test_validate_main_menu(string, result):
    """Test if main menu function takes you to main."""
    from mail_room import validate_main_menu
    assert validate_main_menu(string) == result


@pytest.mark.parametrize('name, result', VAL_NAMES)
def test_validate_name(name, result):
    """Test if names is a string."""
    from mail_room import validate_name
    assert validate_name(name) == result


@pytest.mark.parametrize('amount, result', VAL_DON)
def test_validate_donation(amount, result):
    """Test if amount can be an integer."""
    from mail_room import validate_donation
    assert validate_donation(amount) == result
