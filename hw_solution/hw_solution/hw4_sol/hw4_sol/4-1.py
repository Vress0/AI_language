status = input('Please enter your status: ')
income = eval(input('Please enter your income: '))

if status == '0':
    if income >=0 and income <= 8350:
        tax = income * 0.10
    elif income >= 8351 and income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income >= 33951 and income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income >= 82251 and income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income >= 171551 and income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (income - 171550) * 0.33
    elif income >= 372951:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + (372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == '1':
    if income >= 0 and income <= 16700:
        tax = income * 0.10
    elif income >= 16701 and income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    elif income >= 67901 and income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25
    elif income >= 137051 and income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (income - 137050) * 0.28
    elif income >= 208851 and income <= 372950:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (income - 208850 * 0.33)
    elif income >= 372951:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + (372950 - 208850) * 0.33 + (income - 372950) * 0.35
elif status == '2':
    if income >= 0 and income <= 8350:
        tax = income * 0.10
    elif income >= 8351 and income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income >= 33951 and income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income >= 68526 and income <= 104425:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income >= 104426 and income <= 186475:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + (income - 104425) * 0.33
    elif income >= 186476:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + (186475 - 104425) * 0.33 + (income - 186475) * 0.35
elif status == '3':
    if income >= 0 and income <= 11950:
        tax = income * 0.10
    elif income >= 11951 and income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    elif income >= 45501 and income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
    elif income >= 117451 and income <= 190200:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (income - 117450) * 0.28
    elif income >= 190201 and income <= 372950:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (income - 190200) * 0.33
    elif income >= 372951:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + (190200 - 117450) * 0.28 + (372950 - 190200) * 0.33 + (income - 372950) * 0.35
else:
    print('illegal status')

print('The tax is ${:.2f}'.format(tax))