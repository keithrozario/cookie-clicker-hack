import deserialize
import encoding
import serialize

INPUT_GAME_FILE = "example_save_game.txt"

with open(INPUT_GAME_FILE, "r") as f:
    string_from_file = f.read()

# Decode and Deserialize
spl = encoding.decode_raw_string(string_from_file)
parsed_data = deserialize.parse(spl)
parsed_data['version'] = spl[0]
parsed_data['placeholder'] = spl[1]

# Modify values in parsed_data here
print(parsed_data['main_stats']['cookies'])
print(parsed_data['main_stats']['cookies_earned'])

parsed_data['main_stats']['cookies']=92401719440.323624

# Serialize and Encode
serialized_string = serialize.serialize_parsed_data(parsed_data)
encoded_final_string = encoding.encode_final_save_string(serialized_string)
assert encoded_final_string != string_from_file

with open("output.txt", "w") as output_saved_game:
    output_saved_game.write(encoded_final_string)
