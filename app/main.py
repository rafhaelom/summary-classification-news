from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .functions import extract_news, load_tokenizer_summary, load_model_summary, load_vectorizer_classification, load_model_classification, limpa_frases_texto, limpa_frases_titulo, rouge_metrica, normalizer
from .schemas import ClassificacaoTextoInput, ResumoUrlInput, ClassificacaoUrlInput

app = FastAPI()

@app.get("/")
async def home():
    return JSONResponse(
        status_code=200,
        content={"message": "Summarization Abstractive and Classified Headline Service"}
    )

@app.post("/resumo/")
async def ResumoTexto(url_noticia_request: ResumoUrlInput):
    url = url_noticia_request.url_noticia
    titulo, texto = extract_news(url)
    texto = limpa_frases_texto(texto)
    titulo = limpa_frases_titulo(titulo)

    tokenizer_summary = load_tokenizer_summary()
    model_summary = load_model_summary()

    inputs = tokenizer_summary.encode(texto, max_length=3000, truncation=True, return_tensors='pt')
    summary_ids = model_summary.generate(inputs, max_length=100, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer_summary.decode(summary_ids[0])

    manchete = summary.replace('<pad> ', '').replace('</s>','')

    rouge_metrica_score = rouge_metrica()
    score = rouge_metrica_score.score(titulo, manchete)
    
    return JSONResponse(
        status_code=200,
        content={'manchete_original': titulo,
                'manchete_gerada': manchete,
                'score': score}
    )

@app.post("/classificacao/texto")
async def ClassificacaoTexto(texto_manchete_request: ClassificacaoTextoInput):
    titulo_noticia = texto_manchete_request.manchete_noticia

    vectorizer_classification = load_vectorizer_classification() 
    model_classification = load_model_classification()

    tema_pred = model_classification.predict(vectorizer_classification.transform([normalizer(titulo_noticia)]))[0]
    tema_pred_proba = model_classification.predict(vectorizer_classification.transform([normalizer(titulo_noticia)]))
    tema_model = model_classification.classes_

    return JSONResponse(
        status_code=200,
        content={'titulo': titulo_noticia,
                'tema_predito': tema_pred,
                'score': tema_pred_proba,
                'score_class': tema_model}
    )

@app.post("/classificacao/url/")
async def ClassificacaoUrl(classificacaourl_request: ClassificacaoUrlInput):
    url = classificacaourl_request.url_noticia
    titulo, texto = extract_news(url)
    texto = limpa_frases_texto(texto)
    titulo_noticia = limpa_frases_titulo(titulo)

    vectorizer_classification = load_vectorizer_classification() 
    model_classification = load_model_classification()

    tema_pred = model_classification.predict(vectorizer_classification.transform([normalizer(titulo_noticia)]))[0]
    tema_pred_proba = model_classification.predict(vectorizer_classification.transform([normalizer(titulo_noticia)]))
    tema_model = model_classification.classes_

    return JSONResponse(
        status_code=200,
        content={'titulo': titulo_noticia,
                'tema_predito': tema_pred,
                'score': tema_pred_proba,
                'score_class': tema_model}
    )