from typing import Optional
from uuid import uuid4 as uuid

from fastapi import FastAPI, HTTPException
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
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        return resultado[0]
    
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado.')


@app.delete('/producto/{producto_id}')
def eliminar_producto_por_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        producto = resultado[0]
        productos.remove(producto)

        return {'mensaje': f'El producto con ID {producto_id} fue eliminado.'}
    
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado.')


@app.put('/producto/{producto_id}')
def actualizar_producto(producto_id: str, producto: Producto):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    if len(resultado):
        producto_encontrado = resultado[0]
        producto_encontrado.nombre = producto.nombre
        producto_encontrado.precio_compra = producto.precio_compra
        producto_encontrado.precio_venta = producto.precio_venta
        producto_encontrado.proveedor = producto.proveedor

        return producto_encontrado

    
    raise HTTPException(status_code=404, detail=f'El producto con el ID {producto_id} no fue encontrado.')
