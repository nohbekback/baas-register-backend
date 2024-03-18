from fastapi import FastAPI
from pydantic import BaseModel
#hacer atributos opcionales
from typing import Optional

# Definir modelos de Register
class Register(BaseModel):
    username: str
    name: str
    email: str
    alias: str
    phone: int
    address: Optional[str]

# Establecer datos de registro
register_data = {"username": "brendac123", "name": "Brenda Cuevas", "email": "brendac@gmail.com", "alias": "brendac", "phone": "123-456-7890",
                "address": "123 Main Street, City, State, 12345"}

# Inicializar la aplicación FastAPI
app = FastAPI()

# Definir rutas
@app.post("/register")
def user_register(register: Register):
    return register_data

#agregar perfiles
#@app.post("/register")
#def insertar_register(register: Register):
 #   return {"message": f"perfil {register.name} insertado"}
