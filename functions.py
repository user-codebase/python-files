def is_text_a_palindrome(text):
    """
        Description:
        This function checks if the 'text' is palindrome,
        it means if they are the same if we read them from left to right, 
        and from right to left.

        Arguments:
        text (string)

        Returns:
        This function returns boolean True if text is a palindrome otherwise False.
    """
    return text == text[::-1]


## test ##
print("Is 'hello' a palindrome?", is_text_a_palindrome("hello"))
print("Is 'kayak' a palindrome?", is_text_a_palindrome("kayak"))
print("Is 'potop' a palindrome?", is_text_a_palindrome("potop"))