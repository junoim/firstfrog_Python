# *args


# def funargs(normal, *args,):
#     print(normal)
#     for items in args:
#         print(items)
# normal = "I am a normal argument and the students are:"
#har = ["Harry", "Rohan", "Skillif", "Hammad", "Shivam"]
# funargs(normal, *har)

#*kwargs

def funargs(normal, *args, **kwargs):
    print(normal)
    for items in args:
        print(items)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")
har = ["Harry", "Rohan", "Skillif", "Hammad", "Shivam"]
normal = "I am a normal argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness instructor", "The programmer":"coordinator", "Shivam":"cook"}
funargs(normal, *har, **kw)
