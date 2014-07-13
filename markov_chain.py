import nltk
import random
raw=open("war_and_peace.txt","r").read()
tokens=nltk.word_tokenize(raw)
trigrams=nltk.trigrams(tokens)
fdist = nltk.FreqDist(trigrams)

    
    
def next_random_word(bigram):
    b=nltk.word_tokenize(bigram)
    candidate=[]
    for trigram in fdist.items():
        if trigram[0][0]==b[0] and trigram[0][1]==b[1]:
            candidate.append(trigram[0][2])
    return random.choice(candidate)
    
         
def markov_based_sentence():
    random_sent=""
    l=int(raw_input("enter the length of the sentences: "))
    bigram=raw_input("enter the starting two words to get the random sentence: ")
    random_sent=bigram+random_sent
    while(len(nltk.word_tokenize(random_sent))!=l):
        word3=next_random_word(bigram)
        random_sent=random_sent+" "+word3
        bigram=nltk.word_tokenize(bigram)[1]+" "+word3
    print random_sent
print "usage:\n press q to quit\n else press any key to continue\n"
while(1):
    i=raw_input("press enter to continue")
    if(i=="q"):
        break
    else:
        markov_based_sentence()
    

