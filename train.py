from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot =  ChatBot("Training Example")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train([ "Hi there!", "Hello", "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.", ])

trainer.train([ "Greetings!",  "Hello", ])
trainer.train("chatterbot.corpus.english")
