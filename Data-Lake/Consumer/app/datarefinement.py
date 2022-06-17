
from h11 import Data
import nltk 
from pathlib import Path
import PyPDF2
import pandas as pd
from nltk.corpus import stopwords
import numpy as np 
import base64

def ExtractKeyWords(text):
    allstopwords = stopwords.words('english')
    sw_list = ['I','i', '.',"''","'",",","...","!","``","-","?","ll","|",":","'s","'f'","'wo'", "'se'","n't", "'m", "f","'ll", "'ne'", "se"]
    allstopwords.extend(sw_list)

    stopword = set(allstopwords)

    def generator(x, count):
        for pages in range(x-1):
            pageobj = pdfreader.getPage((count))
            yield nltk.word_tokenize(pageobj.extract_text())
            count=count + 1

    #download if run for the first time
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('stopwords')

    
    # Decode the Base64 string, making sure that it contains only valid characters
    text = base64.b64decode(base64.b64encode(Data), validate=True)
    # Find the path to the file
    base_path = Path(__file__).parent
    files_path = (base_path / "../../pdf/Percy Jackson & the Olympians 01 - The Lightning Thief.pdf").resolve()

    pdffileobj=open(files_path,'rb')

    #create reader variable that will read the pdffileobj
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)

    #This will store the number of pages of this pdf file
    x=pdfreader.numPages


    #create a variable that will select the selected number of pages
    pageobj = pdfreader.getPage(0)
    txt = pageobj.extractText()
    pagetoken = nltk.word_tokenize(txt)
    for d in generator(x, 1):
        pagetoken.extend(d)

    filtered_token = []
    filtered_token.extend([w for w in pagetoken if not w.lower() in stopword])
    return filtered_token
