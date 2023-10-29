wage_rate = 51.45
rate_wage_over = 88.9
currency = '$'

while True:
    hour = input("What is your weekly working hours?")

    if hour.upper() == 'X':
        print("Exit the Program.")
        break
    try:
        float_value = float(hour)
        #print("Input is a valid number.")
        if float(hour) <= 35:
            wage = float(hour) * wage_rate
            print('Your wage is {}{}.'.format(currency, wage))
            break
        elif float(hour) > 35:
            wage = 35 * wage_rate + (float(hour) - 35) * rate_wage_over
            print('Your wage is {}{}.'.format(currency, wage))
            break
    except ValueError:
        print("Input is not a valid number.")
        break





import yfinance

start = '2020-01-01'
end = None

tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]

max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)


the_sum = 0
for i in range(0,101):
    the_sum += i
print(the_sum)

the_sum = 0
while i <101:
    the_sum += i
print(the_sum)

for i in range(1,4):
    for j in range(1,4):
        if i<= j:
            print(i,j)


for even in range(0,10,2):
    if even >2:
        continue
print(even)


for odd in range(1,10,2):
    for even in range(0,10,2):
        if even >2:
            break
    print(even,odd)