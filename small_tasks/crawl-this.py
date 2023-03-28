from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def available_next_n_months(entered_date, months_ahead):
    date_ahead = date.today() + relativedelta(months=+months_ahead)
    av_date = datetime.strptime(entered_date, '%Y-%m-%d').date()
    if date.today() <= av_date <= date_ahead:
        print("in between")
    else:
        print("No!")


# av_date_string = '2023-03'
# available_next_n_months(av_date_string, 3)
