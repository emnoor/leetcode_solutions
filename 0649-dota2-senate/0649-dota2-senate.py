class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_list = list(senate)
        r_rem = 0
        d_rem = 0
        r_ban = 0
        d_ban = 0

        for c in senate:
            if c == "R":
                r_rem += 1
            else:
                d_rem += 1

        while True:
            for i, c in enumerate(senate_list):
                if c == "R":
                    if r_ban > 0:
                        senate_list[i] = "."
                        r_ban -= 1
                        r_rem -= 1
                        continue
                    d_ban += 1
                    if d_rem == 0:
                        return "Radiant"
                elif c == "D":
                    if d_ban > 0:
                        senate_list[i] = "."
                        d_ban -= 1
                        d_rem -= 1
                        continue
                    r_ban += 1
                    if r_rem == 0:
                        return "Dire"
                    