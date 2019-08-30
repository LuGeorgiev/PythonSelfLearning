bitcoins = int(input())
china = float(input())
commission = (100-float(input()))/100

bgn = bitcoins * 1168
bgn += china * 0.15 * 1.76
euro = bgn / 1.95

print(round(euro*commission, 2))
