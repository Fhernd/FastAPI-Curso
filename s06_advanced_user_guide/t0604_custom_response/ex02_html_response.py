from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/items/', response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />
            
            <table border="1">
                <tbody>
                    <tr>
                        <td>Foo</td>
                        <td>Bar</td>
                    </tr>
                    <tr>
                        <td>Foo</td>
                        <td>Bar</td>
                    </tr>
            </table>
        </body>
    </html>
    """
