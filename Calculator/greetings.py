# Day 6 maa explain garnu hola yo 
def greet (name:str=None)->None:
    if not name:
        return ("Hello,welcome to python and data science class.")
    return (f"Welcome {name} to python and data science class.")



def welcome_msg(name:str=None)-> None:
    print(f"You are welcome to the course:{name}")