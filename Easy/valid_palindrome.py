class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = False
        s = s.replace(' ', '')
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for i in punctuation:
            s = s.replace(i, '')

        if s.lower() == s[::-1].lower():
            is_palindrome = True

        return is_palindrome