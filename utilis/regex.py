import re

def find_word(word,para):
    """
    This function takes a paragraph and a word as input , and returns 
    all occurences of the word in the paragraph 
    
    """
    matches=re.findall(word,para,re.IGNORECASE)
    return matches 

def search_word(word,para):
    """ 
    This function takes a paragraph and a word as input , and returns True 
    if the word is found in the paragraph, ignoring case sensitivity. Otherwise , it returns False.
    
    """
    return bool (re.search(word,para,re.IGNORECASE))

def replace_word(word,para,replacement_word ):
    """  
    This function takes a paragraph , a word , and a replacement word as a input ,
    and returns the modified paragraph with all occurences of the given word replaced
    by the replacement word, ignoring case sensitivity 
    """

    return re.sub(word,replacement_word,para,flags=re.IGNORECASE)



def get_hastag_words(status):
   pattern=r'#\w+'
   hashtag_words=re.findall(pattern,status,re.IGNORECASE)
   return hashtag_words







if __name__=='__main__':
    paragraph="The rain in Spain falls mainly on the plain and the valley"
    word="rain"
    print(search_word(word,paragraph))




# Example of replacement of word 
"""" 
if __name__=='__main__'
    paragraph='The rain in spain falls mainly on the plain and valleys '
    word='spain'
    replacement_word='Nepal'

    after_para=replace_word(word,replacement_word,paragraph)
    print(f"before replacement :{paragraph}")
    print(f"after replacement : {after_para}")


"""



#Example of hashtag_words
""" 
If __name__=='__main__'
    paragraph="The #rain #Spain falls mainly on the plain and valleys
    hastag_words=get_hastag_words(word,replacemnt_word,pargraph)
    print(f"Hashtag words in the paragraph :",hastag_words)
    
"""