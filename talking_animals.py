def speak_v1(animal="dog"):
   if animal=="pig":
      return "oink"
   elif animal=="duck":
      return "quack"
   elif animal=="cat":
      return "meow"
   elif animal=="dog":
      return "woof"
   else:
      return "?"


def speak_v2(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal) #dict.get(key) returns the corresponding value
    if noise:
        return noise
    return "?"


def speak_v3(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')  #passing a default value to .get



        
