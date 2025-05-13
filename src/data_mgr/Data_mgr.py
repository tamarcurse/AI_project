from File import CFile

class CDataMgr:
    def __init__(self):
        self._files = []
        self._data = ""
        self._is_update_data = False
    def get_files(self):
        return self._files
    def get_data(self):
        if not self._is_update_data:
            self._update_data()
        return self._data
    def add_file(self, file):
        self._files.append(file)
        self._is_update_data = False
    def remove_file(self, file):
        if file in self._files:
            self._files.remove(file)
            self._is_update_data = False
    def _update_data(self):
        if self._is_update_data:
            return
        self._data = ""
        for file in self._files:
            if file.get_data():
                self._data += file.get_data()
        self._is_update_data = True