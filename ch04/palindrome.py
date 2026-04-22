def palindrome(str):
    str = str.lower().replace(' ', '')
    if str == str[::-1]:
        return True
    else:
        return False

for x in ['anna', 'banana', 'Anna', 'My gym']:
    print(palindrome(x))
