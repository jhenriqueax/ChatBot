
from chatterbot.trainers import ListTrainer

def treinarBot(novoArray,chatBot):
    trainer = ListTrainer(chatBot)
    trainer.train(novoArray)


def treinar(respostaEsperada, BancoDePerguntas, chatBot):

    retorno = []
    indexArray = 0
    for index in range(len(BancoDePerguntas) * 2):
        if index % 2 == 0:
            retorno.append(BancoDePerguntas[indexArray])
            indexArray += 1
        else:
            retorno.append(respostaEsperada)
   
    return treinarBot(retorno,chatBot)


    