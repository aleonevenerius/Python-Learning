# Import the library
import pyttsx3



poem = '''
Teus olhos são meus livros. Que livro há aí melhor, Em que melhor se leia A página do amor? Flores me são teus lábios. Onde há mais bela flor, Em que melhor se beba O bálsamo do amor?
'''
# SPEAKING TEXTS
engine = pyttsx3.init()

#1 Microsoft Zira Desktop - English (United States)
#2 Microsoft Hazel Desktop - English (Great Britain)

#engine.say(poem) # It speaks here

#engine.runAndWait() # Bloqueia enquanto processa todos os comandos atualmente enfileirados.

#engine.save_to_file(a, 'test.mp3') # 'a' is what it'll say and forward the file will
'''
def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
'''
def onWord(name, location, length):
   print('word', name, location, length)
   if location > 10:
      engine.stop()
engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices') #  # Obtém o valor atual de uma propriedade do motor.
engine.setProperty('voice', voices[1].id) # Define the voice
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait() # Blocks while processing all currently queued commands.