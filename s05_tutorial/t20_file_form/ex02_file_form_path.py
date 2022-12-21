from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/{id}")
async def create_file(id: int, file: bytes = File(), file_b: UploadFile = File(), token: str = Form()):
    return {
        "id": id,
        "file_size": len(file),
        "token": token,
        "file_b_content_type": file_b.content_type,
    }
