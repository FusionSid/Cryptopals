from typing import overload
from base64 import b64encode, b16decode

from rich import print


@overload
def hex_to_base64(hex_data: bytes) -> bytes:
    ...


@overload
def hex_to_base64(hex_data: str) -> str:
    ...


def hex_to_base64(hex_data: bytes | str) -> bytes | str:
    if isinstance(hex_data, bytes):
        return b64encode(b16decode(hex_data, casefold=True))
    elif isinstance(hex_data, str):
        return b64encode(b16decode(hex_data, casefold=True)).decode()
    else:
        raise TypeError("Invalid Argument Type Provided!")


if __name__ == "__main__":
    DATA_INPUT = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    EXPECTED_OUTPUT = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    result = hex_to_base64(DATA_INPUT)
    assert result == EXPECTED_OUTPUT

    print(f"{result=}")
