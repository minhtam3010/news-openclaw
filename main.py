import loadenv # noqa: F401
from openclaw_platform.slack.slack import handler
import uvicorn
from fastapi import FastAPI, Request
from mangum import Mangum

api = FastAPI()
lambda_handler = Mangum(api)

@api.get("/")
def read_root():
    return {"status": "ok", "message": "Lambda is live"}
    
@api.post("/slack/events")
async def slack_events(request: Request):
    return await handler.handle(request)

def main():
    uvicorn.run(
        "main:api",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )

if __name__ == "__main__":
    main()
