from fastapi import APIRouter, Request
from app.services.signalwire_service import handle_incoming_call

router = APIRouter()


@router.post("/signalwire/incoming")
async def signalwire_incoming(request: Request):
    body = await request.body()
    return await handle_incoming_call(body)


@router.get("/signalwire/incoming")
async def signalwire_get():
    return {"status": "This endpoint is live and reachable via GET."}
