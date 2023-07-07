from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .functions import extract_news, load_tokenizer_summary, load_model_summary, load_vectorizer_classification, load_model_classification
from .schemas import ResumoTextoInput, ClassificacaoTextoInput, ResumoUrlInput, ClassificacaoUrlInput

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse(
        status_code=200,
        content={"message": "Summarization Abstractive and Classified Headline Service"}
    )

@app.post("/resumo/texto/")
async def ResumoTexto(texto_noticia_request: ResumoTextoInput):
    text = texto_noticia_request.texto_noticia
    inputs = tokenizer.encode(text, max_length=3000, truncation=True, return_tensors='pt')
    summary_ids = model.generate(inputs, max_length=100, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0])

    manchete = summary.replace('<pad> ', '').replace('</s>','')
    score = texto_noticia_request.score
    return JSONResponse(
        status_code=200,
        content={'manchete': manchete,
                 'score': score}
    )

@app.post("/classificacao/texto/")
async def ClassificacaoTexto(texto_manchete_request: ClassificacaoTextoInput):
    tema = texto_manchete_request.manchete_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'tema': tema,
                 'score': score}
    )

@app.post("/resumo/url/")
async def ResumoUrl(url_noticia_request: ResumoUrlInput):
    url = url_noticia_request.url_noticia
    score = 100
    return JSONResponse(
        status_code=200,
        content={'url_noticia': url,
                 'score': score}
    )

@app.post("/classificacao/url/")
async def ClassificacaoUrl(classificacaourl_request: ClassificacaoUrlInput):
    url = classificacaourl_request.url_noticia
    titulo = extract_news(url)
    score = 100
    return JSONResponse(
        status_code=200,
        content={'url_noticia': url,
                 'titulo_noticia': titulo,
                 'score': score}
    )