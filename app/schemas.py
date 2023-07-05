from pydantic import BaseModel

class ResumoInput(BaseModel):
    texto_noticia: str
    score: str

    class Config:
        schema_extra = {
            "example": {
                "texto_noticia": "texto_teste",
                "score": "rouge"
            }
        }

class ClassificacaoInput(BaseModel):
    manchete_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "manchete_noticia": "manchete_teste"
            }
        }