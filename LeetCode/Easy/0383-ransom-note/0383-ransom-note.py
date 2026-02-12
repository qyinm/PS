class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        compo = {}
        for note in ransomNote:
            if note not in compo:
                compo[note] = 1
            else:
                compo[note] += 1
        
        compo_mag = {}
        for mag in magazine:
            if mag not in compo_mag:
                compo_mag[mag] = 1
            else:
                compo_mag[mag] += 1

        for k, v in compo.items():
            if k in compo_mag and compo_mag[k] >= v:
                continue
            else:
                return False
        return True