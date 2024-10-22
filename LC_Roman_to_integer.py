# Input: s = "III"
# Output: 3
# Explanation: III = 3.
ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romantoint(s):
    total = 0
    for i in range(len(s) - 1):
        # Если текущий символ меньше следующего, то вычитаем его
        if ROMAN[s[i]] < ROMAN[s[i + 1]]:
            total -= ROMAN[s[i]]
        else:
            total += ROMAN[s[i]]
    # Не забудь добавить последний символ
    total += ROMAN[s[-1]]
    return total


s = 'MCMXCIV'

print(romantoint(s))
