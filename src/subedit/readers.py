import json
from typing import Union, Dict
from subedit.interfaces import DataReader, DataWriter


class JSONReader(DataReader):
    @staticmethod
    def read(source: Union[str, bytes, Dict]):
        if isinstance(source, dict):
            return source
        elif isinstance(source, bytes):
            return json.loads(source.decode('utf-8'))
        elif isinstance(source, str):
            with open(source, 'r', encoding='utf-8') as f:
                return json.load(f)
        raise ValueError("Fonte de dados desconhecida")


class JSONWriter(DataWriter):
    @staticmethod
    def write(file_path: str, data: dict) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
