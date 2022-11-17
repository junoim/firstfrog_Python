#create a dictionary and take input from the user and return the meaning of the word from the dictionary

d1 = {
          "serendipity" :"the faculty or phenomenon of finding valuable or agreeable things not sought for",
          "euphoria" : "a feeling or state of intense excitement and happiness",
          "epiphany": "a moment of sudden and great revelation or realization.",
          "ordeal" : "a very unpleasant and prolonged experience."
}
name= input("what meaning are you searching for?")
print(d1[name])

