def are_ships_destroyed(ships_map, hits_map):
    ships = list(ships_map)
    hits = list(hits_map)
    for x in range(len(ships)):
        if ships[x] == 'B' and hits[x] != 'X':
            return False
            break
    return True
