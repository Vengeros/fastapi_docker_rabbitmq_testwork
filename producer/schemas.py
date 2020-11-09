from pydantic import BaseModel, Field
from typing import Dict, Optional


class Task(BaseModel):
    taskid: str = Field(..., title='TaskID')
    title: str = Field(..., title='Title')
    params: Optional[Dict[str, str]] = Field(None, title='Params')
