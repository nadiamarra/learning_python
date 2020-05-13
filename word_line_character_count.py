def word_line_character_count_v1(file_name):  #my go
    '''(file)->dict

    Return a dictionary with the number of lines, words and characters in a given file.
        
    >>> statistics('story.txt')
    {'lines': 172, 'words': 2145, 'characters': 11227}
    '''

    with open("story.txt") as story:
        string=story.read()
        
        #characters
        dictionary=dict(characters=len(string))
        
        #words
        words=string.split()
        num_words=len(words)
        dictionary["words"]=num_words

        #lines
        lines=string.split("\n")
        num_lines=len(lines)
        dictionary["lines"]=num_lines

        return dictionary
        

def word_line_character_count_v2(file_name):   #Udemy solution
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }



