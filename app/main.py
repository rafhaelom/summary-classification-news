from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas import ResumoInput, ClassificacaoInput

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse(
        status_code=200,
        content={"message": "Summarization Abstractive and Classified Headline Service"}
    )

@app.post("/resumo/")
async def resumo(texto_noticia_request: ResumoInput):
    manchete = texto_noticia_request.texto_noticia
    score = texto_noticia_request.score
    return JSONResponse(
        status_code=200,
        content={'manchete': manchete,
                 'score': score}
    )

@app.post("/classificacao/")
async def classificacao(texto_manchete_request: ClassificacaoInput):
    tema = texto_manchete_request.manchete_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'tema': tema,
                 'score': score}
    )