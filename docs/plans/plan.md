# Cookie Clicker Save Editor: Program Plan

## 1. Objective

The goal is to create a Python program that can read a Cookie Clicker save file (`example_save_game.txt`), decode it into a human-readable and editable format (a Python dictionary), allow for modifications, and then re-encode it back into a valid save string that can be imported into the game.

This will provide a structured and reliable way to edit game stats like cookie counts, upgrades, and building levels without manual and error-prone string manipulation.

## 2. High-Level Program Flow

The program will execute in the following sequence:

1.  **Read:** Open and read the raw save string from `example_save_game.txt`.
2.  **Decode:** Validate the string and decode it from its custom Base64 format into a plain text, delimited string.
3.  **Parse:** Convert the delimited string into a structured Python dictionary, mapping each data point to a descriptive key.
4.  **Modify (User Interaction):** Allow the user to programmatically change values within the Python dictionary.
5.  **Serialize:** Convert the modified dictionary back into the game's specific delimited string format.
6.  **Encode:** Encode the serialized string back into the custom Base64 format.
7.  **Output:** Present the final, valid save string to the user, ready for import.

## 3. Detailed Implementation Steps

### Step 1: Read the Save File

-   The program will start by opening `example_save_game.txt` in read mode.
-   It will read the entire content of the file into a single string variable.

### Step 2: Decode the Save String

This step reverses the game's `utf8_to_b64` and validation process.

-   **Validation:** Check for and remove the `!END!` terminator from the end of the string.
-   **Decoding Logic:** Implement a Python function that replicates the game's `b64_to_utf8` JavaScript function.
    -   First, use Python's standard `base64.b64decode()` to convert the string into a sequence of bytes.
    -   Then, correctly interpret these bytes as a UTF-8 string. This will handle any special characters used in the bakery name or other fields.

### Step 3: Parse to a Python Dictionary

This is the most critical step for making the data editable. The decoded string will be parsed into a nested dictionary.

-   **Primary Split:** Split the decoded string by the `|` (pipe) delimiter to separate the main sections (version, run details, prefs, main data, buildings, upgrades, achievements, buffs, mods).
-   **Dictionary Structure:** Create a dictionary with keys corresponding to these sections.
-   **Secondary Split:** For each section, split the substring by the appropriate secondary delimiter (`;` or `,`).
-   **Mapping:** Map each resulting value to a descriptive key within the dictionary. For example:

```python
# Proposed Dictionary Structure
save_dict = {
    "version": 2.052,
    "run_details": {
        "start_date": 1672531200000,
        "bakery_name": "Gemini's Bakery",
        "seed": "randomseed123",
        # ...etc.
    },
    "preferences": {
        "particles": True,
        "numbers": True,
        # ...etc.
    },
    "main_stats": {
        "cookies": 1.23e45,
        "cookies_earned": 2.34e45,
        "cookie_clicks": 1000,
        "golden_clicks": 100,
        # ... A key for every variable outlined in data_parsing_restoration.md
    },
    "buildings": [
        {"name": "Cursor", "amount": 500, "level": 10, "total_cookies": 1e30},
        {"name": "Grandma", "amount": 450, "level": 10, "total_cookies": 5e30},
        # ...etc. for all buildings
    ],
    "upgrades": {
        # Key-value pair for each upgrade ID and its status (unlocked, bought)
        "0": {"unlocked": 1, "bought": 1},
        "1": {"unlocked": 1, "bought": 1},
        # ...etc.
    },
    "achievements": {
        # Key-value pair for each achievement ID and its status (won)
        "0": {"won": 1},
        # ...etc.
    },
    "mod_data": {
        "mod_id_1": "mod_save_string_1"
    }
}
```

### Step 4: Modify the Data

-   With the data in a dictionary, modification becomes simple and clear. The plan will include examples of how a user could interact with the dictionary:
    -   `save_dict['main_stats']['cookies'] = 9.99e99`
    -   `save_dict['buildings'][0]['amount'] = 1000`
    -   `save_dict['upgrades']['7']['bought'] = 1`

### Step 5: Serialize to a String

This step reverses the parsing process.

-   The program will iterate through the dictionary in the exact original order.
-   It will pull the values for each key and join them together with the correct delimiters (`;` or `,`).
-   These substrings will then be joined by the primary `|` delimiter to reconstruct the full, plain-text save string.

### Step 6: Encode the String

This step reverses the decoding process.

-   **Encoding Logic:** Implement a Python function that replicates the game's `utf8_to_b64` JavaScript function.
    -   This will involve converting the string to bytes using UTF-8 encoding.
    -   Then, use Python's `base64.b64encode()` to get the final Base64 representation.
-   **Terminator:** Append the `!END!` terminator to the end of the newly encoded string.

### Step 7: Output

-   The final, valid save string will be printed to the console or written to a new file (e.g., `modified_save.txt`).
-   The user can then copy this string and import it directly into the game.
