# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.training.trainers import ListTrainer

chatterbot = ChatBot("Terminal",
    #storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="./chatterbotdatabase.db"
)

chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "你好。 你好吗?",
    "Hello",
])

chatterbot.train([
    "我很好太感谢",
    "我很好你呢",
])

print("Type something to begin...")

while True:
    try:
        bot_input = chatterbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
