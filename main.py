import os
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
GITHUB_CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]


class CallbackRequest(BaseModel):
    code: str


@app.post("/oauth/callback")
async def oauth_callback(payload: CallbackRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": payload.code,
            },
        )

    data = response.json()
    if "access_token" not in data:
        raise HTTPException(
            status_code=400,
            detail=data.get("error_description", "Đổi token thất bại"),
        )

    return {"access_token": data["access_token"]}


@app.get("/")
async def health():
    return {"status": "ok"}
