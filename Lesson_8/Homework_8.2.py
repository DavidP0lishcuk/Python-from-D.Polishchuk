
def is_palindrome(text: str) -> bool:

    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^ `{|}~"""
    string = text.lower()
    string = "".join(sym for sym in string if sym not in punctuation)

    return string == string[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'