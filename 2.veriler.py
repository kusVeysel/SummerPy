
#? global/local variables
text = "metin" #* bu bir global değişkendir

def myFunction():
    a = 18 #* bu bir local değişkendir
    #! global kelimesi ile local değişken globale çevrilebilir
    global b
    b = 1
    print("bu bir",text)

print(text)
print(b)