from goose3 import Goose
import pickle
from transformers import T5Tokenizer # Tokenizer
from transformers import T5Model, T5ForConditionalGeneration # PyTorch model
from rouge_score import rouge_scorer
import sklearn

import spacy
nlp = spacy.load('pt_core_news_sm')


# ---------- Funções para carregar os modelos pré-treinados ----------
def load_tokenizer_summary():
    # Tokenizer PTT5 pré-treinado no Hugging Face.
    tokenizer_summary = T5Tokenizer.from_pretrained('unicamp-dl/ptt5-base-portuguese-vocab')
    return tokenizer_summary

def load_model_summary():
    # Modelo PTT5 pré-treinado no Hugging Face.
    model_summary = T5ForConditionalGeneration.from_pretrained('phpaiola/ptt5-base-summ-xlsum')
    return model_summary

def load_vectorizer_classification():
    vectorizer_classification = pickle.load(open('./models/bow_vectorizer.pkl', "rb"))
    return vectorizer_classification

def load_model_classification():
    model_classification = pickle.load(open('./models/model_mnb_bow.pkl', "rb"))
    return model_classification

# ---------- Função para extrair título e texto da notícia ----------
def extract_news(url):
    config = {}
    config['strict'] = False  # turn of strict exception handling
    config['browser_user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'  # set the browser agent string
    config['http_timeout'] = 5.05  # set http timeout in seconds

    g = Goose(config)
    article = g.extract(url=url)
    titulo = article.title
    texto_limpo = article.cleaned_text
    g.close()
    return titulo, texto_limpo

# ---------- Funções para normalização do título e do texto ----------
def limpa_frases_texto(texto):
    '''
    Função para remover frases/parágrafos contidos no texto.
    '''
    frase_1 = 'O formato de distribuição de notícias do Correio Braziliense pelo celular mudou. A partir de agora, as notícias chegarão diretamente pelo formato Comunidades, uma das inovações lançadas pelo WhatsApp. Não é preciso ser assinante para receber o serviço. Assim, o internauta pode ter, na palma da mão, matérias verificadas e com credibilidade. Para passar a receber as notícias do Correio, clique no link abaixo e entre na comunidade:'
    frase_2 = 'Apenas os administradores do grupo poderão mandar mensagens e saber quem são os integrantes da comunidade. Dessa forma, evitamos qualquer tipo de interação indevida. Caso tenha alguma dificuldade ao acessar o link, basta adicionar o número (61) 99666-2581 na sua lista de contatos.'
    frase_3 = 'Quer ficar por dentro sobre as principais notícias do Brasil e do mundo? Siga o Correio Braziliense nas redes sociais. Estamos no Twitter, no Facebook, no Instagram, no TikTok e no YouTube. Acompanhe!'
    frase_4 = 'As informações são do jornal O Estado de S. Paulo.'
    frase_5 = '• Blogs Redirect Novas temporadas de Outer banks, As five e Você se destacam no streaming em fevereiro'
    frase_6 = 'Receba direto no celular as notícias mais recentes publicadas pelo Correio Braziliense. É de graça. Clique aqui e participe da comunidade do Correio, uma das inovações lançadas pelo WhatsApp.'
    frase_7 = 'O Correio tem um espaço na edição impressa para publicar a opinião dos leitores. As mensagens devem ter, no máximo, 10 linhas e incluir nome, endereço e telefone para o e-mail sredat.df@dabr.com.br.'


    texto = texto.split("¶")
    texto = [frase.strip() for frase in texto if frase not in '']
    texto = [frase.replace(frase_1, '') for frase in texto]
    texto = [frase.replace(frase_2, '') for frase in texto]
    texto = [frase.replace(frase_3, '') for frase in texto]
    texto = [frase.replace(frase_4, '') for frase in texto]
    texto = [frase.replace(frase_5, '') for frase in texto]
    texto = [frase.replace(frase_6, '') for frase in texto]
    texto = [frase.replace(frase_7, '') for frase in texto]
    texto = [frase for frase in texto if frase not in '']
    texto = ' '.join(texto)
    texto = texto.split('•')
    texto = [frase.strip() for frase in texto if frase not in '']
    return ' '.join(texto)

def limpa_frases_titulo(titulo):
    '''
    Função para remover caracteres especias no título.
    '''
    titulo = titulo.split("¶")
    titulo = [frase.strip() for frase in titulo if frase not in '']
    return ' '.join(titulo)

# Funções para normalizar título para o modelo de classificação
def sentence_tokenizer(sentence):
    return [token.lemma_ for token in nlp(sentence.lower()) if (token.is_alpha & ~token.is_stop)]

def normalizer(sentence):
    tokenized_sentence = sentence_tokenizer(sentence)
    return ' '.join(tokenized_sentence)


# ---------- Funções para carregar as métricas do resultado dos modelos ----------
def rouge_metrica():
    rouge_metrica_score = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    return rouge_metrica_score