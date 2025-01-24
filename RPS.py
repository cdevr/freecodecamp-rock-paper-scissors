# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
outcome = {
    'RR': 'tie',
    'RP': 'loss',
    'RS': 'win',
    'PR': 'win',
    'PP': 'tie',
    'PS': 'loss',
    'SR': 'loss',
    'SP': 'win',
    'SS': 'tie',
}

# Just some random first things to play to recognize the opponents.
firstPlays = 'RPSRRPSS'
my_last_play = ''

def player(prev_play, opponent_history=[], my_history=[]):
    global my_last_play
    if prev_play:
        opponent_history.append(prev_play)
        my_history.append(my_last_play)
    else:
        opponent_history.clear()
        my_history.clear()
        my_last_play = ''

    if opponent_history:
        opp = opponent_history[-1]
        me = my_history[-1]
        # print(f'last play opponent: {opp} me: {me} result: {outcome[me + opp]}')
    result = innerplayer(prev_play, opponent_history, my_history)
    my_last_play = result
    
    return result

def innerplayer(prev_play, opponent_history, my_history):
    # first play our first plays
    # print(f'Opponent history {len(opponent_history)} prev_play is {prev_play}')
    if len(opponent_history) < len(firstPlays):
        return firstPlays[len(opponent_history)]

    if ''.join(opponent_history).startswith('RPPSRRPP'):
        # print('quincy')
        return 'PPSSR'[(len(opponent_history) + 1) % 5]

    if ''.join(opponent_history).startswith('PPPPPPRP'):
        # print('abbey')
        if len(opponent_history) == len('PPPPPPRP'):
            for x in ['']+my_history[:-1]:
                _ = abbey(x)
        tobeat = abbey(my_history[-1])
        return ideal_response[tobeat]
    if ''.join(opponent_history).startswith('PPSRPPSR'):
        # print('kris')
        return ideal_response[ideal_response[my_history[-1]]]
    if ''.join(opponent_history).startswith('RRRRPPPP'):
        # print('mrugesh')

        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)

        if most_frequent == '':
            most_frequent = "S"

        return ideal_response[ideal_response[most_frequent]]

    # if len(opponent_history) == len(firstPlays):
    #     print(''.join(opponent_history))

    return random.choice('RPS')

# Copy of abbey
def abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
