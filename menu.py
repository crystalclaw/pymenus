import curses


# Makes cell the correct length
def format_cell(cell, cell_length):
    cell = str(cell)
    # Shorten cell if it is too long, and add '...'
    if len(cell) > cell_length:
        cell = cell[:(cell_length - 3)] + '...'
    # Add spaces if cell is to short
    elif len(cell) < cell_length:
        cell += ((cell_length - len(cell)) * ' ')
    return cell


# Prints out a non-interactive table
# This takes an array of arrays. The top level array represents rows.
def table(contents, cell_length):
    # Initilize curses
    screen = curses.initscr()
    # Generate the row seperator
    seperator = ""
    for _ in range(len(contents[0])):
        seperator += '+' + ('-' * cell_length)
    seperator += "+\n"

    # place the first seperator
    screen.addstr(seperator)

    # Iterate through each row
    for row in contents:
        # Define/reset the string, and put in the first sidewall
        running_string = "|"
        # Iterate through each column
        for i in row:
            running_string += (format_cell(i, cell_length)) + '|'
        screen.addstr(running_string + "\n")
        screen.addstr(seperator)
    screen.refresh()
    screen.getch()
    curses.endwin()
