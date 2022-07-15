def lyrics_generator(arr):
    lyric = ''
    unos=0
    for item in arr:
        if item == 0:
            lyric+= "Boom "
        elif item == 1:
            lyric+= "Drop the base "
            unos +=1
            if unos ==3:
                lyric+= "!!!Break the base!!! " 
                unos=0
    return lyric
        

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))