from chatterbot import ChatBot

chatbot = ChatBot(
    'Newsbot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train('chatterbot.corpus.russian')
