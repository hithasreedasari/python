from datetime import datetime

from greet_by_time import greet_by_time


def test_morning():
    dt = datetime(2026, 1, 1, 6, 0)
    assert greet_by_time(dt) == "Good morning"


def test_afternoon():
    dt = datetime(2026, 1, 1, 13, 30)
    assert greet_by_time(dt) == "Good afternoon"


def test_evening():
    dt = datetime(2026, 1, 1, 19, 45)
    assert greet_by_time(dt) == "Good evening"


def test_night():
    dt = datetime(2026, 1, 1, 23, 15)
    assert greet_by_time(dt) == "Good night"


def test_boundary_morning_start():
    dt = datetime(2026, 1, 1, 5, 0)
    assert greet_by_time(dt) == "Good morning"


def test_boundary_morning_end():
    dt = datetime(2026, 1, 1, 11, 59)
    assert greet_by_time(dt) == "Good morning"


def test_boundary_afternoon_start():
    dt = datetime(2026, 1, 1, 12, 0)
    assert greet_by_time(dt) == "Good afternoon"


def test_boundary_evening_start():
    dt = datetime(2026, 1, 1, 17, 0)
    assert greet_by_time(dt) == "Good evening"


def test_boundary_night_start():
    dt = datetime(2026, 1, 1, 22, 0)
    assert greet_by_time(dt) == "Good night"
