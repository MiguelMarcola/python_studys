from datetime import datetime, timedelta


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

    def registration_time(self):
        registration_time = (datetime.today() +
                             timedelta(days=30, hours=19, minutes=23, seconds=23)) - self.created_at
        return registration_time

    def __str__(self):
        return f"Created at -> {self.format_date()}"
