import requests
from fastapi import FastAPI, Request
from pydantic import BaseModel


class Item(BaseModel):
    function: str


app = FastAPI()


@app.post("/Datalore/")
async def handel_webhook(item: Item):
    data = item.function
    
    try:
        function = TaskFunction.run(data)
        result = function()
    except ValueError:
        result = {'error': 'Invalid function name'}
    return result

@app.get("/")
async def read_root():
    return {"Hello": "World"}

def task_1():
    return {'result': 'Done task 1!'}

def task_2():
    return {'result': 'Done task 2!'}

class TaskFunction:
    fun_task = {
        'task_1': task_1,
        'task_2': task_2
    }
    @classmethod
    def run(self, fun_name):
        function = self.fun_task.get(fun_name)
        if function:
            return function
        raise ValueError('Что-то пошло не так')
