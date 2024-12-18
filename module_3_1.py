calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a

def is_contains(string, listik):
    count_calls()
    is_con = False
    for i in range(len(listik)):
        temp = listik[i]
        if temp.lower() == string.lower():
            is_con = True
            break
    return is_con


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
