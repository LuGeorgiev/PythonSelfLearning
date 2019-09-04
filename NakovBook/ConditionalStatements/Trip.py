budget = float(input())
season = input()
if budget <= 100:
    destination = 'Bulgaria'
    money_spent = budget * 0.7
    info = f'Hotel - {money_spent:.2f}'
    if season == 'summer':
        money_spent = budget * 0.3
        info = f'Camp - {money_spent:.2f}'
elif budget <= 1000:
    destination = 'Balkans'
    money_spent = budget * 0.8
    info = f'Hotel - {money_spent:.2f}'
    if season == 'summer':
        money_spent = budget * 0.4
        info = f'Camp - {money_spent:.2f}'
else:
    destination = 'Europe'
    money_spent = budget * 0.9
    info = f'Hotel - {money_spent:.2f}'

print('Somewhere in ' + destination)
print(info)
