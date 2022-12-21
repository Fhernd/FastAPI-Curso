from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(), file_b: UploadFile = File(), token: str = Form()):
    return {
        "file_size": len(file),
        "token": token,
        "file_b_content_type": file_b.content_type,
    }
