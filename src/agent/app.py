from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Sentinel Agent",
    description="Secure enterprise AI agent laboratory",
    version="0.1.0"
)


class EmailRequest(BaseModel):
    """
    Defines the structure of an incoming email.

    All email content is considered untrusted input.
    """

    sender: str = Field(
        min_length=3,
        max_length=320
    )

    subject: str = Field(
        default="",
        max_length=300
    )

    body: str = Field(
        min_length=1,
        max_length=20000
    )


class EmailPreviewResponse(BaseModel):
    """
    Defines the response returned by the email intake endpoint.
    """

    email_id: str

    source_trust: Literal["untrusted_external"]

    status: Literal["received_not_processed"]

    body_character_count: int

    model_invoked: bool

    actions_taken: list[str]

    received_at: datetime


@app.get("/health")
def health_check():
    """
    Confirms that the API is running.
    """

    return {
        "status": "healthy",
        "application": "Sentinel Agent",
        "llm_connected": False
    }


@app.post(
    "/emails/preview",
    response_model=EmailPreviewResponse
)
def preview_email(email: EmailRequest):
    """
    Accepts an email and returns safe intake metadata.

    This endpoint does not call an LLM,
    store the email or execute CRM actions.
    """

    response = EmailPreviewResponse(
        email_id=str(uuid4()),

        source_trust="untrusted_external",

        status="received_not_processed",

        body_character_count=len(email.body),

        model_invoked=False,

        actions_taken=[],

        received_at=datetime.now(timezone.utc)
    )

    return response
