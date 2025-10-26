import uuid
from google.adk.sessions import InMemorySessionService
import uvicorn
from .agent import root_agent
from google.adk.runners import Runner
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Header
from typing import Optional

load_dotenv()

app = FastAPI()

APP_NAME = "agents"
SESSION_SERVICE = InMemorySessionService()
RUNNER = Runner(
    agent=root_agent,
    session_service=SESSION_SERVICE,
    app_name=APP_NAME,
)


class SessionRequest(BaseModel):
    user_id: str

@app.post('/sessions')
async def create_session_controller(
    request: SessionRequest,
    authorization: Optional[str] = Header(None)
):
    session_token = authorization.replace("Bearer ", "") if authorization and authorization.startswith("Bearer ") else None
    
    if not session_token:
        raise HTTPException(status_code=401, detail="Session token missing or invalid")

    session_id = str(uuid.uuid4())
    user_id = request.user_id
    
    new_session = await SESSION_SERVICE.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
        state={"session_token": session_token}
    )

    return new_session


class ChatRequest(BaseModel):
    prompt: str
    user_id: str
    session_id: str

class SimpleChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=SimpleChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        session = await SESSION_SERVICE.get_session(
            session_id=request.session_id,
            user_id=request.user_id,
            app_name=APP_NAME,
        )
    except Exception as e:
        print(f"Error while trying to access session. ID: {request.session_id}, User: {request.user_id}")
        raise HTTPException(
            status_code=404,
            detail=f"Session not found or does not belong to user."
        )

    user_prompt = types.Content(
        role="user",
        parts=[types.Part(text=request.prompt)],
    )

    final_response_text = ""
    async for event in RUNNER.run_async(
        user_id=request.user_id,
        session_id=request.session_id,
        new_message=user_prompt,
    ):
        # final response is the whole content it generated
        # the events can be thought_signatures, function_call, etc.
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            else:
                final_response_text = "[Agent did not return content]"
    
    return SimpleChatResponse(response=final_response_text)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# from fastapi.responses import StreamingResponse

# @app.post("/chat/stream")
# async def chat_stream(request: ChatRequest):
#     async def event_generator():
#         async for event in RUNNER.run_async(
#             user_id=request.user_id,
#             session_id=request.session_id,
#             new_message=types.Content(role="user", parts=[types.Part(text=request.prompt)]),
#         ):
#             if event.content and event.content.parts:
#                 for part in event.content.parts:
#                     if part.text:
#                         yield f"data: {part.text}\n\n"
#     return StreamingResponse(event_generator(), media_type="text/event-stream")