import deserialize
import encoding
import serialize

INPUT_GAME_FILE = "example_save_game.txt"

def test_no_changes():
    """
    Test by opening the INPUT GAME FILE, decoding and serializing.
    Then deserialize and encode beck to the string.
    Because we perform no changes, the input and output must be same.
    If they're different there's a bug in our code.
    """

    with open(INPUT_GAME_FILE, "r") as f:
        string_from_file = f.read()

    spl = encoding.decode_raw_string(string_from_file)
    parsed_data = deserialize.parse(spl)
    parsed_data['version'] = spl[0]
    parsed_data['placeholder'] = spl[1]

    serialized_string = serialize.serialize_parsed_data(parsed_data)
    encoded_final_string = encoding.encode_final_save_string(serialized_string)

    assert encoded_final_string == string_from_file