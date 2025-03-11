from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from model.chatboot_request_model import ChatBootRequestModel
from service.chatboot_service import chatboot_service
from util.common_util import logger

router = APIRouter()        
templates = Jinja2Templates(directory="templates")

@router.get("",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@router.post("/chat")
async def chatboot_controller(payload: ChatBootRequestModel):
    try:
        logger.info(f"chatboot(), Request - {payload.message}")
        response = await chatboot_service(payload.message)
        logger.info(f"chatboot(), Response - {response}")
        return JSONResponse(content={"response": response})    
    except Exception as e:
        logger.error(f"chatboot(), Error - {e}")
        raise HTTPException(status_code=500, detail=str(e).replace("'", ""))