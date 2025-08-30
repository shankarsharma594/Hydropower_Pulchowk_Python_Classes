def count_word(sentence):
    """ count the words in the given sentence
    """
    # remove leading and trailing whitespaces
    sentence=sentence.strip()      # Yo code le agaadi pachaadi vaako whitespaces laai hataai dinchha 
    
    #split the sentence into words 
    words=sentence.split()
    
    return len(words) 

    # remove leading whitespaces i.e the white space in left
    """ sentence=sentence.lstrip()
        print(sentence) 
        
    """


def is_sentence_okay(sentence_len:int):
    """
    Check if the sentence length is okay 
    
    """
    if sentence_len<=0:
        print("Sentence length isnot a positive number")
        return False

    
    if sentence_len<=5:
        return True 
    return False





 


""" 

if __name__== '__main__':
    sentence="This is just a test sentence"
    result=count_word(sentence)
    print(f"    Number of words in given sentence is : {result}")


""" # Yo yaha na rakhera sidhai main.py ma haalnu parchha 




# This is the example of modulein python with .py files 
# Day 9 videos of 2nd part 1st 9 minute videos 