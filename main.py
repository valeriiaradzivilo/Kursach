import regular_game

# array to record replays
replay = ['y']
# array to record created task
create = []
# create an array for all presssed buttons and their color
all_coords = []
# level
amounts = []
# while user wants to replay
while replay and replay.pop() == 'y':
    regular_game.regular_game(create, replay, all_coords, amounts)
    if not replay or replay.pop() != 'n':
        replay.append('y')
