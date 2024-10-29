from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
    html_content = "<h1>Welcome to my site</h1>"
    return HTMLResponse(content=html_content, status_code=200)

# http://127.0.0.1:8000/items/5?q=somequery
@app.get("/items/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# http://127.0.0.1:8000/products?id=1
@app.get("/products")
def get_product(id):
    html_content = f"<h1>Product {id}</h1>"
    return HTMLResponse(content=html_content, status_code=200)