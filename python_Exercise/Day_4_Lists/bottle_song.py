NUMBERS = [
    "no", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine", "ten"
]


def verse(n):
    current = "bottle" if n == 1 else "bottles"
    remaining = "bottle" if n - 1 == 1 else "bottles"

    return [
        f"{NUMBERS[n].capitalize()} green {current} hanging on the wall,",
        f"{NUMBERS[n].capitalize()} green {current} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {NUMBERS[n - 1]} green {remaining} hanging on the wall.",
    ]


def recite(start, take=1):
    lyrics = []

    for n in range(start, start - take, -1):
        lyrics.extend(verse(n))

        if n != start - take + 1:
            lyrics.append("")

    return lyrics