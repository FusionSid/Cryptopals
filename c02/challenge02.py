from base64 import b16decode, b16encode

from rich import print


def fixed_xor(data1: bytes, data2: bytes) -> bytes:
    decoded_data = b16decode(data1, casefold=True)
    decoded_xor_against = b16decode(data2, casefold=True)

    return bytes(x ^ y for x, y in zip(decoded_data, decoded_xor_against))


if __name__ == "__main__":
    DATA_INPUT = "1c0111001f010100061a024b53535009181c"
    XOR_AGAINST = "686974207468652062756c6c277320657965"
    EXPECTED_OUTPUT = "746865206b696420646f6e277420706c6179"

    result = b16encode(fixed_xor(DATA_INPUT.encode(), XOR_AGAINST.encode())).decode()
    assert result.lower() == EXPECTED_OUTPUT

    print(f"{result=}")
