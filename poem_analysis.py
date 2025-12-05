"""
Problem Statement:
Write a Python program that analyzes one or more poem text files and reports
various statistics using Natural Language Processing (NLP).

Requirements:
1. The program should take a list of poem file names (e.g., "poem_1.txt",
   "poem_2.txt", "poem_3.txt") and process each file one by one.

2. For each poem:
   - Read the full text from the file.
   - Count how many sentences are in the poem.
   - Count how many words are in the poem.

3. Remove English stopwords (such as "the", "and", etc.) and:
   - Find the 5 most common remaining words.
   - Display each of these words and how many times they appear.

4. Use sentiment analysis on the entire poem:
   - Print the overall sentiment scores (positive, negative, neutral, compound).
   - Identify and print the most positive sentence in the poem.
   - Identify and print the most negative sentence in the poem.

5. Using part-of-speech (POS) tagging:
   - Count how many nouns are present (tags NN or NNP).
   - Count how many adjectives are present (tag JJ).
   - Print the counts for nouns and adjectives.

Tools / Libraries:
- textblob for sentence, word, and POS tagging.
- nltk stopwords for removing common words.
- nltk.sentiment.SentimentIntensityAnalyzer (VADER) for sentiment analysis.

Input:
- One or more text files containing poems (e.g., poem_1.txt, poem_2.txt, poem_3.txt).

Output:
- For each poem, print:
  - Number of sentences
  - Number of words
  - Top 5 most common non-stop words
  - Overall sentiment scores
  - Most positive sentence
  - Most negative sentence
  - Counts of nouns and adjectives
"""
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk import FreqDist
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def iterate_poems(poems):
    if len(poems)!=0:
        do_operations(poems[0])
        return iterate_poems(poems[1::])


def do_operations(poem_file_name):
    file_obj=open(poem_file_name)
    lines=file_obj.read()
    file_obj.close()
    textBlobObj = TextBlob(lines)
    print("How many sentences are in the poem? "+str(len(textBlobObj.sentences)))
    text_words=textBlobObj.words
    print("How many words? "+str(len(text_words)))
    words_after_stopwords=[word_text for word_text in text_words if word_text.strip().lower() not in stopwords.words("english") and "’" !=word_text.strip() and "‘" !=word_text.strip()]
    counter=FreqDist(words_after_stopwords)
    print("If you remove the stop words what are the 5 most common words in the poems?")
    for word_text in counter.most_common(5):
        print(word_text[0]+" is repeated "+str(word_text[1])+" times")
    print("What is the sentiment measure for the entire poem? What is the most positive sentence? What is the most negative?")
    setimentalAnalaysisObj=SentimentIntensityAnalyzer()
    print(setimentalAnalaysisObj.polarity_scores(lines))
    postive_setences=str()
    postive_objecter=int()
    for setences in textBlobObj.sentences:
        setimentalAnalaysisObj=SentimentIntensityAnalyzer()
        if setimentalAnalaysisObj.polarity_scores(str(setences)).get("pos")>postive_objecter:
            postive_setences=str(setences)
            postive_objecter=setimentalAnalaysisObj.polarity_scores(str(setences)).get("pos")
    print("Postive Senetense are "+postive_setences)
    negative_setences=str()
    negative_object=0
    for setences in textBlobObj.sentences:
        sia=SentimentIntensityAnalyzer()
        if sia.polarity_scores(str(setences)).get("neg")>negative_object:
            negative_setences=str(setences)
            negative_object=sia.polarity_scores(str(setences)).get("neg")
    print("Negative Senetense are "+negative_setences)
    print("""Using parts-of-speech tagging, how many nouns (speech tags N or NNP) are present? How many adjectives (tag JJ?
3. Pick one of your poems and produce a word cloud (section 12.3.2), though you don't need to use a mask image.""")
    partsOfSpeechTags={"Nouns":0,"Adjectives":0}
    for part in textBlobObj.tags:
        if part[1] in ["NNP","NN"]:
            partsOfSpeechTags["Nouns"]+=1
        elif part[1]=="JJ":
            partsOfSpeechTags["Adjectives"]+=1
    print(partsOfSpeechTags)
    
iterate_poems(["poem_1.txt","poem_2.txt","poem_3.txt"])
