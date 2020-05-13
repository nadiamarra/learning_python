def find_and_replace(file_name,search_word,replacement_word):  #my go
    with open(file_name,"r+") as file_name:
        text=file_name.read() 
        file_name.seek(0) 
        file_name.write(text.replace(search_word,replacement_word))
        

def find_and_replace_v2(file_name, old_word, new_word):   #Udemy solution
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
