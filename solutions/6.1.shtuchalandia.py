def find_special_state() -> ():
    """
    Out of the states.txt file, print the name of the only US state that can be spelled using letters from a single row
    of a QWERTY keyboard.

    Args:
        None.

    Returns:
        None.
    """
    top_row = set('qwertyuiop')
    middle_row = set('asdfghjkl')
    bottom_row = set('zxcvbnm')

    with open("states.txt", 'r') as file:
        for line in file:
            state_letters = set(line.rstrip('\n'))
            if any(row.issuperset(state_letters) for row in (top_row, middle_row, bottom_row)):
                print(line)


if __name__ == "__main__":
    find_special_state()
