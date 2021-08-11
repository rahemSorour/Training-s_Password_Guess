mdp="freaking"
trie=3
pw=input("saiser pass word")
if mdp!=pw:
    while trie>0:
        pw=input("try again")
        if mdp==pw:
            ("correct")
            break
        else:
            trie-=1
            print(f" {trie} chance")
    else:
       print("your chance is over")
else:
 print("ur pass word is correct")          
            