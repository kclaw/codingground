# Hello World program in Python
def count_words(sentence):
    split_sentence = sentence.split(' ')
    #result_list = [0] * len(split_sentence)
    result_dict = {}
    result = []
    
    for w in split_sentence:
        #for i in range(len(split_sentence)):
            #if w == split_sentence[i]:
            if result_dict.has_key(w):
               result_dict[w] += 1
            else:
                result_dict.update({w:1})
    
    # generate tuple of result in list
    #for i in range(len(split_sentence)):
            #result += [(split_sentence[i],result_list[i])]
            
    for key, value in result_dict.iteritems():
        result.append((key,value))      
    
    return sorted(result,key=lambda item:item[1], reverse=True)[:3]
    
print count_words('betty bought a bit of butter but the butter was bitter')
    
