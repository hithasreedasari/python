from datetime import datetime


def _parse_time_input(time_text):
    if not time_text:
        return None
    time_text = time_text.strip()
    for fmt in ("%H:%M", "%H:%M:%S"):
        try:
            parsed = datetime.strptime(time_text, fmt)
            now = datetime.now()
            return now.replace(hour=parsed.hour, minute=parsed.minute, second=parsed.second, microsecond=0)
        except ValueError:
            continue
    raise ValueError("Time must be in HH:MM or HH:MM:SS format")


def greet_by_time(dt=None, time_text=None):
    if dt is None:
        if time_text is not None:
            dt = _parse_time_input(time_text)
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
    user_time = input("Enter time (HH:MM or HH:MM:SS) or press Enter for now: ").strip()
    if user_time:
        print(greet_by_time(time_text=user_time))
    else:
        print(greet_by_time())
