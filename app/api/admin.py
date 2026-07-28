from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login():

    return """
    <h2>Login Administrador</h2>

    <form method="POST">

        <input
            name="username"
            placeholder="Usuario"
        >

        <br><br>

        <input
            type="password"
            name="password"
            placeholder="Contraseña"
        >

        <br><br>

        <button type="submit">
            Ingresar
        </button>

    </form>
    """


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

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    return f"""
    <h1>Panel Administrativo</h1>

    <p>Bienvenido {request.session['admin']}</p>

    <a href="/logout">Cerrar sesión</a>
    """

@router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse("/login", status_code=302)