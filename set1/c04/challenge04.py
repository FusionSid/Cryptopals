from rich import print
from base64 import b16decode


def fixed_xor(data1: bytes, data2: bytes) -> bytes:
    decoded_data = b16decode(data1, casefold=True)
    key = data2 * int(len(decoded_data) / len(data2) + 1)
    return bytes(x ^ y for x, y in zip(decoded_data, key))


def calculate_score(text: bytes) -> float:
    score = 0
    for key, value in frequencies.items():
        error = abs(value - text.count(ord(key)) / len(text))
        score += error
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")

    # more accurate frequency map from wikipedia
    frequencies = {
        "a": 8.2,
        "b": 1.5,
        "c": 2.8,
        "d": 4.3,
        "e": 12.7,
        "f": 2.2,
        "g": 2,
        "h": 6.1,
        "i": 7,
        "j": 0.15,
        "k": 0.77,
        "l": 4,
        "m": 2.4,
        "n": 6.7,
        "o": 7.5,
        "p": 1.9,
        "q": 0.095,
        "r": 6,
        "s": 6.3,
        "t": 9.1,
        "u": 2.8,
        "v": 0.98,
        "w": 2.4,
        "x": 0.15,
        "y": 2,
        "z": 0.074,
    }

    answer = [None, float("inf")]
    for string in input_data:
        options = [
            fixed_xor(string.encode(), chr(char).encode()) for char in range(128)
        ]
        scores = {option: calculate_score(option) for option in options}
        most_likely = sorted(scores.items(), key=lambda x: x[1])[0]
        if most_likely[1] < answer[1]:
            answer = most_likely

    print(f"[red]Most Likely Answer: {repr(answer[0].decode())}")
