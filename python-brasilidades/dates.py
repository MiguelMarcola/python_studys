from datetime import datetime


class Dates:
    def __init__(self):
        self.created_at = datetime.today()

    def __str__(self):
        return f"{self.created_at}"
