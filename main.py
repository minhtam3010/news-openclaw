import loadenv # noqa: F401
from openclaw_platform.slack.slack import handler as slack_handler
import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum
from pydantic import BaseModel
from test import testGetMessage

class MessageRequest(BaseModel):
    text: str

api = FastAPI()
lambda_handler = Mangum(api)

@api.get("/")
def read_root():
    return {"status": "ok", "message": "Lambda is live"}

@api.post("/slack/events")
async def slack_events(request: Request):
    return await slack_handler.handle(request)

@api.post("/message")
def getMessage(request: MessageRequest):
    testGetMessage(request.text)
    
def main():
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )

if __name__ == "__main__":
    main()
