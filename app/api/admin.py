from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/login")
async def login(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@router.post("/login")
async def login_post(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    if username == "admin" and password == "admin123":
        request.session["admin"] = username
        return RedirectResponse("/dashboard", status_code=302)

    return HTMLResponse(
        "<h2>Usuario o contraseña incorrectos</h2>",
        status_code=401
    )

@router.get("/dashboard")
async def dashboard(request: Request):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "admin": request.session["admin"]
        }
    )

@router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse("/login", status_code=302)