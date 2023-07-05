from pydantic import BaseModel

class ResumoInput(BaseModel):
    texto_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "texto_noticia": "texto teste"
            }
        }

class ClassificacaoInput(BaseModel):
    manchete_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "manchete_noticia": "manchete teste"
            }
        }