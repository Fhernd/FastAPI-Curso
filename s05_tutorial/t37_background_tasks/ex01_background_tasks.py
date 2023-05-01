from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notiification(email: str, message=''):
    """
    Write notification to a file
    
    :param email: email address
    :param message: message to be written
    """
    with open('log.txt', mode='w') as email_file:
        content = f'notification for {email}: {message}\n'
        email_file.write(content)
