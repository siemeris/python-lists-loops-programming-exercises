spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }
# Your code here
keys = ["love", "code", "smart" ]
values = ["amor", "codigo", "inteligente" ]

for index in range(0,len(keys)):
    spanish_translations[keys[index]]=values[index]

# Don't touch the code below
print("Translation", spanish_translations["dog"])
print(spanish_translations)

