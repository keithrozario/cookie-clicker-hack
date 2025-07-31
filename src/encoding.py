import base64
import urllib.parse

# Correctly ordered and validated functions from encoding.py
def utf8_to_b64(string: str) -> str:
    return base64.b64encode(string.encode("utf-8")).decode("utf-8")


def b64_to_utf8(encoded_str: str) -> str:
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        return ""


def encode_final_save_string(final_string: str) -> str:
    """
    Generates the final save string to file.

    Args:
        final_string: The Final deserialized string from the parser
    returns:
        encoded_final_string: The encoded string to save to file
    """

    b64_save_string = utf8_to_b64(final_string)
    encoded_final_string = urllib.parse.quote(b64_save_string) + "%21END%21"

    return encoded_final_string


def decode_raw_string(string_from_file: str) -> list:

    # 1. URL Decode the entire raw string FIRST
    save_string = urllib.parse.unquote(string_from_file)

    # 2. Remove the terminator
    terminator = "%21END%21"
    if terminator in save_string:
        unterminated_save_string = save_string.split(terminator)[0]
    else:
        unterminated_save_string = save_string

    # 3. Now, decode the valid Base64 string
    decoded_string = b64_to_utf8(unterminated_save_string)
    spl = decoded_string.split("|")

    return spl
