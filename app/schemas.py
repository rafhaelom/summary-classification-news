from pydantic import BaseModel

class ResumoTextoInput(BaseModel):
    texto_noticia: str
    score: float

    class Config:
        schema_extra = {
            "example": {
                "texto_noticia": "texto_teste",
                "score": 100
            }
        }

class ClassificacaoTextoInput(BaseModel):
    manchete_noticia: str
    score: float

    class Config:
        schema_extra = {
            "example": {
                "manchete_noticia": "manchete_teste",
                "score": 100
            }
        }

class ResumoUrlInput(BaseModel):
    url_noticia: str
    score: float

    class Config:
        schema_extra = {
            "example": {
                "url_noticia": "https://www.<site>.com.br",
                "score": 100
            }
        }

class ClassificacaoUrlInput(BaseModel):
    url_noticia: str
    score: float

    class Config:
        schema_extra = {
            "example": {
                "url_noticia": "https://www.<site>.com.br",
                "score": 100
            }
        }