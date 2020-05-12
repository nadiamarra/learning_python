def copy_entire_file(story,story_copy):  #simple copy of a file
    with open("story.txt") as story:
        for line in story:
            with open("story_copy.txt","a") as story_copy:
                story_copy.write(line)

def copy_entire_file_solution(file_name, new_file_name):   #Udemy solution
    with open(file_name) as file:
        text = file.read()
    with open(new_file_name, "w") as new_file:
        new_file.write(text)                
    
def copy_and_reverse_words(story,story_reversed): #reverses single words but maintains word order
    with open("story.txt") as story:
        for line in story:
           with open("story_reversed.txt","a") as story_reversed:
                story_reversed.write(line[::-1])

def copy_and_reverse_strings(story,lines_reversed): #reverses string order
    with open("story.txt") as story:
        text=story.read() #getting a single string
    with open("lines_reversed.txt","a") as lines_reversed:
        new_text=text.split("\n")  #getting a list of strings (each string is up to a \n)
        new_text.reverse()
        reversed_text="\n".join(new_text)
        lines_reversed.write(reversed_text)  
            
def copy_and_reverse(file_name, new_file_name): #inverts word order and letters
    with open(file_name) as file: 
        text = file.read()
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])




