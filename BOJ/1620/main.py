import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_map_key_name = {}
pokemon_map_key_index = {}

for idx in range(1, n + 1):
    pokemon_name = input().strip()
    pokemon_map_key_name[pokemon_name] = idx
    pokemon_map_key_index[idx] = pokemon_name

for _ in range(m):
    find_input = input().strip()
    if find_input.isdecimal():
        print(pokemon_map_key_index[int(find_input)])
    else:
        print(pokemon_map_key_name[find_input])