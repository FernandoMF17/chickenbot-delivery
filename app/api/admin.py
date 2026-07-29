from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from sqlalchemy.orm import Session
from fastapi import Depends

from app.db.session import get_db
from app.models.category import Category

from app.models.product import Product

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

@router.get("/products/new")
async def new_product(
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    categories = (
        db.query(Category)
        .order_by(Category.name)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="product_form.html",
        context={
            "request": request,
            "title": "Nuevo Producto",
            "product": None,
            "categories": categories,
        }
    )

@router.get("/products/{product_id}/edit")
async def edit_product(
    product_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    product = db.get(Product, product_id)

    if product is None:
        return RedirectResponse("/dashboard", status_code=302)

    categories = (
        db.query(Category)
        .order_by(Category.name)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="product_form.html",
        context={
            "request": request,
            "title": "Editar Producto",
            "product": product,
            "categories": categories,
        }
    )

@router.post("/products/{product_id}/edit")
async def update_product(
    product_id: int,
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...),
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    product = db.get(Product, product_id)

    if product is None:
        return RedirectResponse("/dashboard", status_code=302)

    # Validaciones
    if price < 0:
        return HTMLResponse(
            "<h2>El precio no puede ser negativo</h2>",
            status_code=400
        )

    if stock < 0:
        return HTMLResponse(
            "<h2>El stock no puede ser negativo</h2>",
            status_code=400
        )

    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    product.category_id = category_id

    db.commit()
    db.refresh(product)

    return RedirectResponse(
        "/products",
        status_code=302
    )

@router.post("/products/new")
async def create_product(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    price: float = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...),
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    # Validaciones básicas
    if price < 0:
        return HTMLResponse(
            "<h2>El precio no puede ser negativo</h2>",
            status_code=400
        )

    if stock < 0:
        return HTMLResponse(
            "<h2>El stock no puede ser negativo</h2>",
            status_code=400
        )

    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return RedirectResponse(
        "/products",
        status_code=302
    )

@router.get("/products")
async def products(
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    products = (
        db.query(Product)
        .order_by(Product.id)
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="products.html",
        context={
            "request": request,
            "products": products,
        }
    )

@router.post("/products/{product_id}/delete")
async def delete_product(
    product_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    if "admin" not in request.session:
        return RedirectResponse("/login", status_code=302)

    product = db.get(Product, product_id)

    if product is None:
        return RedirectResponse("/products", status_code=302)

    db.delete(product)
    db.commit()

    return RedirectResponse(
        "/products",
        status_code=302
    )

@router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse("/login", status_code=302)
