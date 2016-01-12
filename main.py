
# Main function call

def tokenize(directory):
    flist = list_txt_files(directory)
    print len(flist)
    bag_of_sent = []
    for files in flist:
        content = read_file(files)
        bag_of_sent.append(sentence_maker(content))
    return lower_case_conversion(bag_of_sent)

# List all files in a particular directory and return a list with path to each file

def list_txt_files(directory):
    txt = []
    for filename in listdir(directory):
        if filename.endswith('.txt'):
            txt.append(directory + "/" + filename)
    return txt

# Read a file and extract its contents

def read_file(fname):
    infile = open(fname)
    contents = infile.read()
    infile.close()
    return contents
    
# Identify end of sentence

def eos_marker(character):
    markers = '.!?'
    for mark in markers:
        if character in markers:
            return True
        else:
            return False
    
# Split each file into sentences

def sentence_maker(text):
    sentence = []
    start = 0
    for index, character in enumerate(text):
        if eos_marker(character):
            sentence.append(text[start : index + 1])
            start = index + 1
        else:
            continue
    return sentence
    
def lower_case_conversion(text):
    lcase = []
    for word in text:
        for token in word:
            lcase.append(token.lower())
    return lcase
