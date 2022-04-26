from calendar import month
from datetime import datetime


class Dates:
    def __init__(self):
        self.created_at = datetime.today()

    def format_date(self):
        date_format = self.created_at.strftime("%d/%m/%Y %H:%M")
        return date_format

    def month_created(self):
        months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        month_created = months[self.created_at.month - 1]
        return month_created

    def day_week(self):
        days = ["Segunda-feira", "Terça-feira", "Quarta-feira",
                "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        day_of_week = days[self.created_at.weekday()]
        return day_of_week

    def __str__(self):
        return f"{self.format_date()}"
