from goose3 import Goose
import pickle
from transformers import T5Tokenizer # Tokenizer
from transformers import T5Model, T5ForConditionalGeneration # PyTorch model
import spacy
nlp = spacy.load('pt_core_news_sm')

def load_tokenizer_summary():
    # Tokenizer PTT5 pré-treinado no Hugging Face.
    tokenizer_summary = T5Tokenizer.from_pretrained('unicamp-dl/ptt5-base-portuguese-vocab')
    return tokenizer_summary

def load_model_summary():
    # Modelo PTT5 pré-treinado no Hugging Face.
    model_summary = T5ForConditionalGeneration.from_pretrained('phpaiola/ptt5-base-summ-xlsum')
    return model_summary

def load_vectorizer_classification():
    vectorizer_classification = pickle.load(open('models/bow_vectorizer.pkl', "rb"))
    return vectorizer_classification

def load_model_classification():
    model_classification = pickle.load(open('models/model_mnb_bow.pkl', "rb"))
    return model_classification

# Funções para normalização do título.
def sentence_tokenizer(sentence):
    return [token.lemma_ for token in nlp(sentence.lower()) if (token.is_alpha & ~token.is_stop)]

def normalizer(sentence):
    tokenized_sentence = sentence_tokenizer(sentence)
    return ' '.join(tokenized_sentence)

def extract_news(url):
    g = Goose()
    article = g.extract(url=url)
    titulo = article.title
    texto_limpo = article.cleaned_text
    g.close()
    return titulo, texto_limpo
