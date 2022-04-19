import itertools
import string
from typing import List


def get_letter_counts(letter_sequence):
    letter_counts = {}
    for c in letter_sequence:
        if c not in letter_counts:
            letter_counts[c] = 0
        letter_counts[c] += 1
    return letter_counts


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_counts = get_letter_counts(letters)
        score_map = dict(zip(string.ascii_lowercase, score))

        max_score = 0
        for i in range(len(words)):
            for combo in itertools.combinations(words, i+1):
                combo_word = "".join(combo)

                word_letter_counts = get_letter_counts(combo_word)
                if [c for c, cc in word_letter_counts.items() if cc > letter_counts.get(c, 0)]:
                    continue

                cs = sum(score_map[c] for c in combo_word)
                max_score = max(max_score, cs)

        return max_score
