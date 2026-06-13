def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    if hey_bob == "": 
        say = "Fine. Be that way!"

    elif hey_bob.isupper() and hey_bob.endswith("?"):
        say = "Calm down, I know what I'm doing!"
        
    elif hey_bob.endswith("?"): 
        say = "Sure."

    elif hey_bob.isupper(): 
        say = "Whoa, chill out!"

    else: 
        say = "Whatever."

    return say