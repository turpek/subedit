from loguru import logger
from pathlib import Path

SRC = (Path(__file__).parent / '..' / '..').resolve()
PATH_LOG = SRC / 'log'
SUFFIX = ['.mkv']

logger.add(f"{PATH_LOG}/subedit.log", rotation="10 MB")

def check_output(path: str|Path):
    output_dir = Path(path) / 'output'
    if not output_dir.exists():
        logger.info("creating the output directory")
        output_dir.mkdir()
    return output_dir

class PrettyMsg:
    def __init__(self, index, size, digits):
        self.__index = index
        self.__size = size
        self.__digits = digits
    def __repr__(self):
        return f'PrettyMsg(index="{self.__index}", size="{self.__size}", digits="{self.__digits}")'
    def __str__(self):
        return f'[{self.__index:>{self.__digits}}/{self.__size}]'
    def __len__(self):
        return self.__size
    def index(self):
        return self.__index
    def digits(self):
        return self.__digits

class PrettyCount:
    def __init__(self, list_: list, start=1):
        self.__size = len(list_)
        self.__digits = len(str(self.__size))
        self.__list = list_
        self.__start = start

    def __iter__(self):
        for i, el in enumerate(self.__list, start=self.__start):
            yield PrettyMsg(i, self.__size, self.__digits), el

