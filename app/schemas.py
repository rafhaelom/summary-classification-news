from pydantic import BaseModel

# class ResumoTextoInput(BaseModel):
#     texto_noticia: str
#     score: float

#     class Config:
#         schema_extra = {
#             "example": {
#                 "texto_noticia": "texto_teste",
#                 "score": 100
#             }
#         }

class ClassificacaoTextoInput(BaseModel):
    manchete_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "manchete_noticia": """O governador do Distrito Federal (DF), Ibaneis Rocha (MDB), foi afastado do cargo nesta sexta-feira por causa da invasão de manifestantes que protestavam contra a reeleição do presidente Luiz Inácio Lula da Silva."""
            }
        }

class ResumoUrlInput(BaseModel):
    url_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "url_noticia": "https://www.correiobraziliense.com.br/cidades-df/2023/07/5107500-ibaneis-viaja-de-ferias-para-grecia-e-celina-assume-gdf-por-15-dias.html"
            }
        }

class ClassificacaoUrlInput(BaseModel):
    url_noticia: str

    class Config:
        schema_extra = {
            "example": {
                "url_noticia": "https://www.correiobraziliense.com.br/cidades-df/2023/07/5107500-ibaneis-viaja-de-ferias-para-grecia-e-celina-assume-gdf-por-15-dias.html"
            }
        }