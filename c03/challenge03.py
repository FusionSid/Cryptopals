from base64 import b16decode
from collections import Counter
from string import ascii_lowercase

from rich import print


def fixed_xor(data1: bytes, data2: bytes) -> bytes:
    decoded_data = b16decode(data1, casefold=True)
    key = data2 * int(len(decoded_data) / len(data2) + 1)
    return bytes(x ^ y for x, y in zip(decoded_data, key))


def get_char_freq(text: str, characters: str) -> dict[str, float]:
    counts = Counter(text)
    return {char: counts.get(char, 0) / sum(counts.values()) for char in characters}


def calculate_score(text: bytes) -> float:
    score = 0
    for key, value in frequencies.items():
        error = abs(value - text.count(ord(key)) / len(text))
        score += error
    return score


if __name__ == "__main__":
    DATA_INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    with open("text.txt") as f:
        text = f.read()

    # using just lowercase since it pops up the most
    frequencies = get_char_freq(text, ascii_lowercase)

    options = [
        fixed_xor(DATA_INPUT.encode(), chr(char).encode()) for char in range(128)
    ]

    scores = {option: calculate_score(option) for option in options}
    top5 = sorted(scores.items(), key=lambda x: x[1])[:5]

    print(
        "Character Frequencies (%):",
        {
            key: f"{round(value * 100, 4)}%"
            for key, value in sorted(
                frequencies.items(), key=lambda x: x[1], reverse=True
            )
        },
    )
    print("Possible Options:", [option.decode() for option in options])
    print(
        "Top 5 (Acording to frequency map):",
        top5,
    )
    print(f'[red]Answer: "{top5[0][0].decode()}"')
