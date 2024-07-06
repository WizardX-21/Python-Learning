players=['charles','martina','michael','flora','eli']
print(players[1:])
print(players[-3:])
print(f'Here are the first three players of my team:')
for player in players[:3]:
  print(player.title())