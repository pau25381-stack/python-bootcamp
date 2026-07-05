def is_anagram(word1, word2):
    pass


def is_palindrome(word1, word2):
    rev1 = word1[::-1]
    rev2 = word2[::-1]

    if  rev1 == rev2:
        return True
    else:
        return False

def test_palindrome_same():
    assert is_palindrome('level', 'level') == True
def test_palindrome_different_1():
    assert is_palindrome('toy', 'yot') == False
def test_palindrome_different_2():
    assert is_palindrome('sun', 'moon' ) == False


def is_pangram(word):
    pass