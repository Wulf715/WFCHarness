# TODO: Platform agnostic agent harness, should be compatible with Axios before first public release
# CONFIG.json structure:
# "BASE_URL": "https://projectnahari.com/v1"
# "API_KEY": None
# "MODEL": "wulfcorp/axios"
# That's really all I need for the most basic of harnesses. ~ Wulf715

import os
import json
from openai import OpenAI

configFile = "CONFIG.json"

# The default config, Defaults to Wulfcorp Axios. ~ Wulf715
writeConfig = {"BASE_URL": "https://projectnahari.com/v1", "API_KEY": "0", "MODEL": "wulfcorp/axios"}

def loadConfig():
    if os.path.exists(configFile):
        with open(configFile, "r") as f:
            return json.load(f)
    else:
        with open(configFile, "w") as f:
            json.dump(writeConfig, f, indent=4)
        # Default to Axios. TODO: Proper config flow. ~ Wulf715
        return writeConfig

config = loadConfig()

client = OpenAI(
    base_url = config["BASE_URL"],
    api_key=config["API_KEY"],
    # Do we even need anything else here? ~ Wulf715
)

def sendCompletion(usercontent):
    response = client.chat.completions.create(
        model=config["MODEL"],
        messages=[
                {
                    "role": "user",
                    "content": usercontent,
                }
            ],
    )
    return response

def main():
    # Ladies and gentlemen: A harness.
    # This took too [REDACTED] long for such a simple thing.
    # FUN DEV FACT: This took approximately one listen-through of Meechy Darko's album Gothic Luxury! ~ Wulf715
    message = input("What do you want to send? ")
    response = sendCompletion(message)
    string = response.removeprefix("data: ")
    parsedString = json.loads(string)
    print()
    print(parsedString["choices"][0]["delta"]["content"])
    print()
    main()

if __name__ == "__main__":
    main()
