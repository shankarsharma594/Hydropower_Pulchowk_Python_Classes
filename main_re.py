from utilis.regex import replace_word

if __name__=='__main__':
    sentence=" This is just a test sentence"
    word=" test"
    replacement="example"
    result=replace_word(word=word,replacement_word=replacement,para=sentence)
    print(result)
