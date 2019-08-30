working_days = int(input())
money_daily = float(input())
used_bgn = float(input())

year_income = working_days * money_daily * 14.5
tolls = year_income * 0.25

print(round(((year_income + tolls) / 365), 2))
