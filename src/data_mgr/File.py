class CFile:
    def __init__(self):
        self._name = ""
        self._path = ""
        self._data = ""
    def set_path(self, path):
        self._path = path
        self._name = path.split("/")[-1] if '/' in path else path.split("\\")[-1]
    def get_data(self) ->str:
        if self._data == "":
            self.load_data()
        return self._data
    def get_name(self) ->str:
        return self._name
    def get_path(self) ->str:
        return self._path
    def load_data(self) -> bool:
        try:
            with open(self._path, 'r') as f:
                self._data = f.read()
            return True
        except Exception as e:
            print(f"Error loading file {self._path}: {e}")
            return False
