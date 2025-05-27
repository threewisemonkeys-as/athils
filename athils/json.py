from pathlib import Path
import json

from athils.file import file_ends_with_newline

class JsonLinesFile:
    def __init__(self, file: Path | str):
        self._file_path = Path(file)

    @staticmethod
    def read_from(file: Path | str) -> list:
        return [json.loads(l) for l in Path(file).read_text().splitlines()]
    
    @staticmethod
    def write_to(file: Path | str, data: list):
        Path(file).write_text('\n'.join([json.dumps(l) for l in data]))

    @staticmethod
    def add_to(file: Path | str, datapoint):
        ends_with_nl =  file_ends_with_newline(file)
        empty = Path(file).read_text().strip() == ''
        with open(file, 'a') as f:
            if not empty and not ends_with_nl:
                f.write('\n')
            f.write(json.dumps(datapoint) + '\n')

    def write(self, data: list):
        JsonLinesFile.write_to(self._file_path, data)

    def add(self, datapoint):
        JsonLinesFile.add_to(self._file_path, datapoint)
