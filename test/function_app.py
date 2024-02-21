import json  
import uuid
import logging

import azure.functions as func
from azure.functions.decorators.core import DataType

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
@app.generic_output_binding(arg_name="toDoItems", type="sql", CommandText="dbo.ToDo", ConnectionStringSetting="SqlConnectionString", data_type=DataType.STRING)
def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        toDoItems.set(func.SqlRow({"Id": str(uuid.uuid4()), "title": name, "completed": False, "url": ""}))
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
                    "Please pass a name on the query string or in the request body",
                    status_code=400
                )


@app.route(route="readServer", auth_level=func.AuthLevel.ANONYMOUS)
@app.generic_input_binding( arg_name="todoItems", type="sql", CommandText="select [Id], [order], [title], [url], [completed] from dbo.ToDo", CommandType="Text", ConnectionStringSetting="SqlConnectionString" )
def readServer(req: func.HttpRequest, todoItems: func.SqlRowList) -> func.HttpResponse:
    rows = list(map(lambda r: json.loads(r.to_json()), todoItems))

    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    ) 