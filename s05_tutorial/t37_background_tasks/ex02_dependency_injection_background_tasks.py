import time
from typing import Annotated

from fastapi import BackgroundTasks, Depends, FastAPI

app = FastAPI()

def write_log(message: str):
    """
    Escribe un mensaje en el log
    
    :param message: mensaje a escribir
    """
    with open('log_registros.txt', mode='a') as log_file:
        time.sleep(10)
        log_file.write(f'{message}\n')
        time.sleep(2)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    """
    Obtiene el query y lo escribe en el log
    
    :param background_tasks: background tasks
    :param q: query
    """
    if q:
        message = f'Found query: {q}'
        background_tasks.add_task(write_log, message)
    
    return q


@app.post('/send-notification/{email}')
async def send_notification(
        email: str,
        background_tasks: BackgroundTasks,
        q: Annotated[str | None, Depends(get_query)] = None
):
    """
    Send notification to a user
    
    :param email: email address
    :param background_tasks: background tasks
    :param q: query
    
    :return: message
    """
    message = f'Message to {email}'
    background_tasks.add_task(write_log, message)
    
    return {'message': 'Message sent'}
