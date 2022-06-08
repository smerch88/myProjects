def chinese_stick_game():
    sticks_quantity = int(input('Enter number of sticks: '))
    while int(sticks_quantity) > 0:
        print('I ' * sticks_quantity)
        first_player_remove = int(input('First player, enter number of sticks to remove: '))
        sticks_quantity -= first_player_remove
        print('I ' * sticks_quantity)
        second_player_remove = int(input('Second player, enter number of sticks to remove: '))
        sticks_quantity -= second_player_remove
    else:
        return print('You lost')


chinese_stick_game()
