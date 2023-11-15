import os
import dotenv

# Load envirnment variables from .env file upon module start.
dotenv.load_dotenv(verbose=True)


def getenv(variable: str) -> str:
    value = os.getenv(variable)
    if value is not None:
        return value
    else:
        raise NameError(f"Error: {variable} Environment Variable not Defined")
