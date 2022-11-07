from os import path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, "..", "..", "..", ".env"))


class Config(dict):
    def __repr__(self) -> str:
        return f"<{type(self).__name__} {dict.__repr__(self)}>"
