# given an amount of money to distribute, a list of recipients and how much money each is owed, 
# you should return the list of recipients and how much each would be paid after following the business logic below:

# no recipient is paid more than they are owed
# the amount is divided as evenly as possible between the recipients

# input: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 40
# output: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 }

# input: { 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 20
# output: { 'ryan': 5, 'stephanie': 5, 'quentin': 5, 'upeka': 5 }

# input: { 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 21
# output: { 'ryan': 2, 'stephanie': 6, 'quentin': 7, 'upeka': 6 }

# input: { 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 22
# output: { 'ryan': 2, 'stephanie': 7, 'quentin': 7, 'upeka': 6 }

# Input: { c: 10, b: 10, a: 10, d: 10 } , 38
# Output: { c: 9, b: 10, a: 10, d: 9

# Input: {a: 10, b: 20, c: 30, d: 40}, 90
# Output: {a:10, b:20, c:30, d:30}



import math


def distribute(recipients, pool):
    # sort dict
    sorted_recipients = dict(sorted(recipients.items(), key = lambda x: (x[1], x[0])))

    n = len(sorted_recipients)

    # iterate thru dict, distribute based on certain conditions
    for recipient, amt_owed in sorted_recipients.items():
        try_give = pool / n

        if amt_owed > try_give:
            sorted_recipients[recipient] = math.ceil(try_give)

        pool -= sorted_recipients[recipient]
        n -= 1

    return sorted_recipients


print(distribute({ 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 40))
print(distribute({ 'ryan': 10, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 20))
print(distribute({ 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 21))
print(distribute({ 'ryan': 2, 'stephanie': 10, 'quentin': 10, 'upeka': 10 } , 22))