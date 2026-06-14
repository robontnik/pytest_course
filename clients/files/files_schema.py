from pydantic import BaseModel, HttpUrl

class FileSchema(BaseModel):

    id : str
    filename : str
    directory : str
    url : HttpUrl

class CreateFileRequestSchema(BaseModel):

    filename : str
    directory : str
    upload_file : str

class CreateFileResponseSchema(BaseModel) : 

    file : FileSchema
