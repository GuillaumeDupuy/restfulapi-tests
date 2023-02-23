from server.routes.student import router as StudentRouter
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException

# Custom 404 & 500 Error Pages

# async def not_found_error(request: Request, exc: HTTPException):
#     return templates.TemplateResponse('404.html', {'request': request}, status_code=404)

# async def internal_error(request: Request, exc: HTTPException):
#     return templates.TemplateResponse('500.html', {'request': request}, status_code=500)

# exception_handlers = {
#     404: not_found_error,
#     500: internal_error
# }

# app = FastAPI(exception_handlers=exception_handlers)

app = FastAPI()

# Mount Static Files
app.mount("/static", StaticFiles(directory="public"), name="public")

# Mount Templates
templates = Jinja2Templates(directory="app/server/templates")

# Mount Routes
app.include_router(StudentRouter, tags=["Student"], prefix="/student")

# Home Page
@app.get("/", tags=["HomePage"])
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Redirect to Home Page if 404 Error Occurs
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse(url="/")

# Redirect to Home Page if 500 Error Occurs
@app.exception_handler(500)
async def internal_exception_handler(request: Request, exc: HTTPException):
    return RedirectResponse(url="/")