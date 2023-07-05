from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas import ResumoTextoInput, ClassificacaoTextoInput, ResumoUrlInput, ClassificacaoUrlInput

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse(
        status_code=200,
        content={"message": "Summarization Abstractive and Classified Headline Service"}
    )

@app.post("/resumo/texto/")
async def resumotexto(texto_noticia_request: ResumoTextoInput):
    manchete = texto_noticia_request.texto_noticia
    score = texto_noticia_request.score
    return JSONResponse(
        status_code=200,
        content={'manchete': manchete,
                 'score': score}
    )

@app.post("/classificacao/texto/")
async def classificacaotexto(texto_manchete_request: ClassificacaoTextoInput):
    tema = texto_manchete_request.manchete_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'tema': tema,
                 'score': score}
    )

@app.post("/resumo/url/")
async def resumourl(url_noticia_request: ResumoUrlInput):
    url = url_noticia_request.url_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'url_noticia': url,
                 'score': score}
    )

@app.post("/classificacao/url/")
async def classificacaourl(url_manchete_request: ClassificacaoUrlInput):
    url = url_manchete_request.url_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'url_noticia': url,
                 'score': score}
    )