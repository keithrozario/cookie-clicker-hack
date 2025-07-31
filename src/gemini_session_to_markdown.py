"""
Converts a Gemini saved session into a simple markdown file of the format

## <ROLE>

<TEXT>

## <ROLE>

<TEXT>

Where <ROLE> is either user or system, and <TEXT> is what was outputted to terminal. Will not include other system info, only what the user saw.
And a little bit of what they didn't see -- hidden prompts hidden inside gemini-cli. e.g. please continue

"""


import json
with open('checkpoint-v1.json','r') as checkpoint_file:
    checkpoint = checkpoint_file.read()
    data = json.loads(checkpoint)

with open("conversation.md", 'w') as conversation_file:
    conversation_file.write("# Conversation\n")
    for datum in data:
        for part in datum['parts']:
            if 'text' in part.keys():
                conversation_file.write(f"## {datum['role']}\n{part['text']}\n\n")
