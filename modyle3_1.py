calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    line = len(string)
    upper_line = string.upper()
    lower_line = string.lower()
    return (line, upper_line, lower_line)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        if string == i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
