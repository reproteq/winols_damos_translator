from googletrans import Translator
import operator

print(" Winols Damos Translator by Reproteq  2020-07-09 ".center(83, "#"))


print("Path to file.a2l")
path = input(">").replace('/', r'\'')

with open(path, 'r+' ,encoding='latin1') as f:
         
    translate = Translator().translate       
    lines = f.readlines()
    f.seek(0)	
	
    for i in range(0, len(lines)):
        text = lines[i]

        if operator.contains(text, "/"):

            lines[i] = text + '\n'

        if operator.contains(text, '"'):
            text = translate(text, src='en', dest='es').text
           #text = translate(text, src='de', dest='es').text
	   #text = translate(text, src='de', dest='en').text	
	
            lines[i] = text + '\n'			


        print(lines[i])

    f.writelines(lines)
