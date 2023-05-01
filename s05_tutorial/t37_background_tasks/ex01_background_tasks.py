from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=''):
    """
    Write notification to a file
    
    :param email: email address
    :param message: message to be written
    """
    with open('log.txt', mode='w') as email_file:
        content = f'notification for {email}: {message}\n'
        email_file.write(content)

@app.post('/send-notification/{email}')
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    Send notification to a user
    
    :param email: email address
    :param background_tasks: background tasks
    
    :return: message
    """
    background_tasks.add_task(write_notification, email, message='some notification')
    
    return {'message': 'Notification sent in the background'}
