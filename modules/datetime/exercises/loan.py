from datetime import datetime
from dateutil.relativedelta import relativedelta

loan = 1_000_000
loan_years_time = 5

date_fmt = "%m/%d/%Y"

date_purchase = datetime(2022, 12, 20)
last_installment = date_purchase + relativedelta(years=loan_years_time)

installments = []
date_installment = date_purchase
while date_installment != last_installment:
    installments.append(date_installment)
    date_installment += relativedelta(months=1)

installment_value = loan / len(installments)
for installment in installments:
    print(f"{installment.strftime(date_fmt)}: ${installment_value:,.2f}")
