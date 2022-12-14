from chatterbot import ChatBot
from treinamento import treinar


#correção de bug (incompatibilidade chatterbot e spacy)
from spacy.cli import download
download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("ChatBot", read_only=True ,tagger_language=ENGSM)



R1 = "Você encontrarar essa informação na secretária"
P1 = ["Preciso do meu histórico", "Onde consigo meu histórico", "Quero meu Histórico"]

treinar(R1, P1, chatbot)



R2 = "funcionou"
P2 = ["Preciso do meu RDM", "Onde consigo a minha declaração de RDM", "Quero meu RDM", "RDM", "rdm"]

treinar(R2, P2, chatbot)



while True:
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)

    if(pergunta == "sair"):
        break

    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta')


