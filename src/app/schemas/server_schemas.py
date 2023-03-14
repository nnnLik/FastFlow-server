from pydantic import BaseModel


class ServerCreateSchemas(BaseModel):
    server_name: str
