from typing import Optional
from uuid import uuid4 as uuid

from fastapi import FastAPI
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str


app = FastAPI()

productos = []


@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la API de Productos'}


@app.get('/producto')
def obtener_productos():
    return productos


@app.post('/producto')
def crear_producto(producto: Producto):
    producto.id = str(uuid())
    productos.append(producto)
    return {'mensaje': 'Producto creado satisfactoriamente.'}


@app.get('/producto/{producto_id}')
def obtener_producto_por_id(producto_id: str):
    for p in productos:
        if p.id == producto_id:
            return p
    
    return {'mensaje': f'El producto con el ID {producto_id} no fue encontrado.'}

