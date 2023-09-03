from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/")
async def index(name: str = Query(default=None)):
    if name:
        return {"message": f"Hello {name}!"}
    return {"message": "Hello NaviGo!"}
