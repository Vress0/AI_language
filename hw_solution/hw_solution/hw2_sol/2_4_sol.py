letter = '''Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.

Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests, 
is {percent}% less likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}
'''
salutation = 'Dr.'
name = 'Ma'
product = 'carpet'
verbed = 'broken'
room = 'kitchen'
animals = 'cat'
amount = '10'
percent = '90'
spokesman = 'John Wick'
job_title = 'Customer Manager'

print(letter.format(salutation = 'Dr.', name = 'Ma', product = 'carpet', verbed = 'broken', room = 'kitchen', animals = 'cat', amount = '10', percent = '90', spokesman = 'John Wick', job_title = 'Customer Manager'))