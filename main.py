#API REST: Interfaz de programacion de apps para compartir recursos
from typing import List
from typing import Optional
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int 

#simular db 
db = []

#CRUD

#READ
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return db

#CREATE
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso:Curso):
    curso.id = str(uuid.uuid4()) #se crea un UUID para generar un ID unico e irepetible
    db.append(curso)
    return curso 

#READ
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id:str):
    curso = next((curso for curso in db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail = "Curso No Encontrado")
    return curso    

#UPDATE    
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id:str, curso_actualizado:Curso):
    curso = next((curso for curso in db if curso.id == curso_id), None)
    if curso is None:
         raise HTTPException(status_code=404, detail = "Curso No Encontrado")
    curso_actualizado.id = curso_id
    index = db.index(curso)
    db[index] = curso_actualizado
    return curso_actualizado

#DELETE
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id:str):
    curso = next((curso for curso in db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail = "Curso No Encontrado")
    db.remove(curso)
    return curso