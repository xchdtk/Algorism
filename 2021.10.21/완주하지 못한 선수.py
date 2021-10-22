def solution(participant, completion):
    players = {}
    for player in participant:
        if player in players:
            players[player] += 1
            continue
        players[player] = 1

    for player in completion:
        if player in players:
            if players[player] == 1:
                del players[player]
                continue
            players[player] -= 1

    return list(players.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))

