from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import get_db
from app.models.category import Category



from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/login")
async def login(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "request": request
        }
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
            "request": request,
            "admin": request.session["admin"]
        }
    )

@router.get("/categories")
async def categories(
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    categories = (
        db.query(Category)
        .order_by(Category.id)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="categories.html",
        context={
            "request": request,
            "categories": categories,
        }
    )

@router.get("/categories/new")
async def new_category(request: Request):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse(
        request=request,
        name="category_form.html",
        context={
            "request": request,
            "title": "Nueva Categoría",
            "category": None
        }
    )

@router.post("/categories/new")
async def create_category(
    request: Request,
    name: str = Form(...),
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    category = Category(
        name=name
    )

    db.add(category)
    db.commit()

    return RedirectResponse(
        "/categories",
        status_code=302
    )

@router.get("/categories/{category_id}/edit")
async def edit_category(
    category_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    category = db.get(Category, category_id)

    if category is None:
        return RedirectResponse("/categories", status_code=302)

    return templates.TemplateResponse(
        request=request,
        name="category_form.html",
        context={
            "request": request,
            "title": "Editar Categoría",
            "category": category,
        }
    )

@router.post("/categories/{category_id}/edit")
async def update_category(
    category_id: int,
    request: Request,
    name: str = Form(...),
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    category = db.get(Category, category_id)

    if category is None:
        return RedirectResponse("/categories", status_code=302)

    category.name = name

    db.commit()

    return RedirectResponse(
        "/categories",
        status_code=302
    )

@router.post("/categories/{category_id}/delete")
async def delete_category(
    category_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    category = db.get(Category, category_id)

    if category is None:
        return RedirectResponse("/categories", status_code=302)

    db.delete(category)
    db.commit()

    return RedirectResponse(
        "/categories",
        status_code=302
    )

@router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse("/login", status_code=302)
