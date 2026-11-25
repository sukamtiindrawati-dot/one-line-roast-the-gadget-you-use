#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Scores six original roast candidates against the judge's five criteria
(weights 5/4/3/2/1, most important first) and writes the winner to
/output/entry.txt. Python 3.13, standard library only.
"""

import os

# Judge criteria, most important first (weights from the brief's order).
WEIGHTS = {
    "daily_gadget": 5,   # roasts a gadget/app people use every day
    "funny": 4,          # joke lands on first read, sting of recognition
    "fresh": 3,          # angle not seen before, not the obvious complaint
    "neat": 2,           # tight wording, no wasted words, inside the limit
    "specific": 1,       # one person's specific gripe, concrete detail
}

CANDIDATES = [
    "My earbuds die at 4% battery, not zero, four, like they want a little "
    "dignity left when they quit on me.",
    "My Wi-Fi router restarts itself at 2 a.m. every night, like it needs "
    "a nap more than I do.",
    "My phone charger only works if I hold the cable at exactly 37 degrees, "
    "like it is a safe combination.",
    "My laptop fan sounds like a jet taking off just because I opened a "
    "spreadsheet.",
    "My smart TV takes longer to load Netflix than the movie I am about "
    "to watch.",
    "My printer only jams when the document is urgent, like it can smell "
    "the deadline.",
]

# Hand-scored against the five criteria (0-5 each). The winner is the
# line with the sharpest concrete detail and the freshest angle.
SCORES = {
    CANDIDATES[0]: {"daily_gadget": 5, "funny": 5, "fresh": 5, "neat": 4,
                    "specific": 5},
    CANDIDATES[1]: {"daily_gadget": 5, "funny": 4, "fresh": 3, "neat": 5,
                    "specific": 4},
    CANDIDATES[2]: {"daily_gadget": 5, "funny": 4, "fresh": 4, "neat": 4,
                    "specific": 5},
    CANDIDATES[3]: {"daily_gadget": 5, "funny": 3, "fresh": 2, "neat": 5,
                    "specific": 3},
    CANDIDATES[4]: {"daily_gadget": 5, "funny": 3, "fresh": 3, "neat": 4,
                    "specific": 3},
    CANDIDATES[5]: {"daily_gadget": 5, "funny": 4, "fresh": 3, "neat": 4,
                    "specific": 4},
}


def total(text):
    """Weighted score for one candidate line."""
    return sum(WEIGHTS[k] * v for k, v in SCORES[text].items())


def valid(text):
    """Gate: 1-200 UTF-8 characters, not only whitespace."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def main():
    pool = [c for c in CANDIDATES if valid(c)]
    assert pool, "no candidate passes the gate"
    # Highest weighted score wins; ties break toward the shorter line,
    # since the judge rewards tight wording and the tie-break favours
    # fewer bytes.
    ranked = sorted(pool, key=lambda c: (total(c), -len(c)), reverse=True)
    winner = ranked[0]
    assert 1 <= len(winner) <= 200, "winner must be 1-200 characters"
    assert winner.strip(), "winner must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"winner ({len(winner)} chars, score {total(winner)}): {winner}")
    for line in ranked[1:]:
        print(f"  {total(line)}: {line}")


if __name__ == "__main__":
    main()
