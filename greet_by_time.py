from datetime import datetime


def greet_by_time(dt=None):
    if dt is None:
        dt = datetime.now()
    hour = dt.hour
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 17:
        return "Good afternoon"
    if 17 <= hour < 22:
        return "Good evening"
    return "Good night"


if __name__ == "__main__":
    print(greet_by_time())
