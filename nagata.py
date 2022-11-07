from deep_translator import GoogleTranslator
to_translate = ['leg', 'arm', 'head', 'cat', 'dog', 'nose', 'egg', 'apple', 'pig', 'hear', 'hair', 'need', 'want']
    
for i in to_translate:
    translated = GoogleTranslator(source='english', target='german').translate(i)
    print(translated)