# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/hidden
password, message = input().split()


def pass_fail(password: String, message: String):
    """
    Takes in a password and message, and returns if each character in the password's first appearance
    is in order in the message.
    :param password: Password given to use for searching.
    :param message: Message to search using password for correct character ordering.
    :return: String 'FAIL' if characters do not appear in order, 'PASS' otherwise
    """
    # first check to make sure all characters from password appear in message
    contains_char = [True if char in message else False for char in password]
    # if they don't all appear, automatically return fail
    if contains_char.count(False) > 0:
        return 'FAIL'
    
    # for each character's index in the password
    for char_i in range(len(password)):
        # extract the character to look for
        char_val = password[0]
        # record all of the first indices of the characters in the password
        first_indices = [message.index(key) for key in password]
        
        # if the first index isn't the smallest, return fail
        if first_indices[0] != min(first_indices):
            return 'FAIL'
        # else, the password can move on to the next characters and the message can be truncated
        else:
            password = password[1:]
            message = message[first_indices[0]+1:]
    # if all characters have been validated, return pass
    return 'PASS'

print(pass_fail(password, message))