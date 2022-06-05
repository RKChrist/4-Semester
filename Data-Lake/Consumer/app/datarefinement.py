import base64
import nltk
from pathlib import Path


#download if run for the first time
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# def refinement(pdfFileinBase64):

# Decode the Base64 string, making sure that it contains only valid characters
text = base64.b64decode(base64.b64encode(b'data'), validate=True)
base_path = Path(__file__).parent
files_path = (base_path / "../../pdf/Percy Jackson & the Olympians 01 - The Lightning Thief.pdf").resolve()
print(files_path)
print(open(files_path, 'rb').read().decode("uft-8"))

# tokens = nltk.word_tokenize()
# print(tokens)
# tagged = nltk.pos_tag(tokens)
# print(tagged)

