from fastapi import FastAPI, Response, status

app = FastAPI()

tasks = {
    'foo': 'Listen to the Bar Fighters',
}


@app.get('/get-or-create-task/{task_id}', status_code=200)
def get_or_create_task(task_id: str, response: Response):
    """
    If the task exists, return it.
    """
    
    if task_id not in tasks:
        response.status_code = status.HTTP_201_CREATED
        tasks[task_id] = 'This didn\'t exist before'
    
    return tasks[task_id]
