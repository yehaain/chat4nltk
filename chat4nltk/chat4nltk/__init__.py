from __future__ import print_function
from nltk.chat.util import reflections

from chat4nltk.lib import AIML, myChat

cheliza = '/home/yehaain/Documentos/UMinho/2018/aulas/trabalhoPratico/Relatorio/workingFiles/ok/chat4nltk/chat4nltk/data/CHELIZA.aiml'    
def chatto(bot):

    if bot == 'cheliza': bot = cheliza
    else: print("Not known bot. You'll taltk to Cheliza")
    
    p = AIML.Parser()
    myPairs = p.parse(cheliza)
    myBot = myChat.myChat(myPairs, reflections)
    myBot.converse()

