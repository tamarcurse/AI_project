from model import CModel
from data_mgr.Data_mgr import CDataMgr
class CSreachar:
    def __init__(self):
        self._data = CDataMgr()
        self._model = CModel()
    def answer(self, question:str) ->str:
        prompt = f"Given the following data:\n{self._data.get_data()}\nAnswer the question: {question}"
        response = self._model.get_response(prompt)
        return response
    