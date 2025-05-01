today = int(input('Enter today\'s day (0 is Sunday, 1 is Monday, and so on): '))
num_days = int(input('Enter the number of days elapsed since today: '))

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
future = (days[today + num_days % 7])
print('Today is,', days[today], 'and the future day is', future)