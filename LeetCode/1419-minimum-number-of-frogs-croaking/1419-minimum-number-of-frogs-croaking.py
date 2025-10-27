class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cache = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        number = 0
        topology = {
            'c': 'r',
            'r': 'o',
            'o': 'a',
            'a': 'k',
        }
        
        for string in croakOfFrogs:
            if string == 'c':
                if cache.get('k') != 0:
                    cache['k'] -= 1
                cache[string] += 1
                number += 1
                continue
            for state in cache:
                if state != 'k' and cache[state] > 0 and topology[state] == string:
                    cache[state] -= 1
                    cache[string] += 1
                    number += 1
            # print(cache)
        print(number)
        if number != len(croakOfFrogs) or cache['k'] == 0:
            return -1
        for key in cache:
            if key == 'k':
                continue
            if cache[key] > 0:
                return -1
        return cache['k']