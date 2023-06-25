from itertools import cycle

from rich import print


def xor_encrypt(text: bytes, key: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(text, cycle(key)))


if __name__ == "__main__":
    INPUT_DATA = (
        "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    )
    EXPECTED_OUTPUT = bytes.fromhex(
        "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
        "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    )

    encrypted_output = xor_encrypt(INPUT_DATA.encode(), b"ICE")
    assert encrypted_output == EXPECTED_OUTPUT

    print(f"[red]Encrypted Output: {repr(encrypted_output.hex())}")
