from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


#correção de bug (incompatibilidade chatterbot e spacy)
from spacy.cli import download
download("en_core_web_sm")
class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("ChatBot", tagger_language=ENGSM)


def treinarBot(novoArray):
    trainer = ListTrainer(chatbot)
    trainer.train(novoArray)


def treinar(respostaEsperada, BancoDePerguntas):
    retorno = []
    indexArray = 0
    for index in range(len(BancoDePerguntas) * 2):
        if index % 2 == 0:
            retorno.append(BancoDePerguntas[indexArray])
            indexArray += 1
        else:
            retorno.append(respostaEsperada)

    return treinarBot(retorno)



R1 = "Você encontrarar essa informação na secretária"
P1 = ["Preciso do meu histórico", "Onde consigo meu histórico", "Quero meu Histórico"]

treinar(R1, P1)



R2 = "funcionou"
P2 = ["Preciso do meu RDM", "Onde consigo a minha declaração de RDM", "Quero meu RDM"]

treinar(R2, P2)




while True:
    pergunta = input("Usuário: ")
    resposta = chatbot.get_response(pergunta)

    if(pergunta == "sair"):
        break

    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta')


