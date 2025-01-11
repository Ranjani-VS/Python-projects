print('''____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    --/ |
 \_/________________________________________________________________\ |
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     //    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    // " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \ /      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -----/ |
 \_/________________________________________________________________\ |''')
print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")
r_l=input("You are at the crossroad.Which direction you want to go? Right or Left?")
if r_l =="Right" or r_l =="right":
    print("Fall into a hole\nGAME OVER")
elif r_l =="Left" or r_l =="left":
    action=input("You have come to the lake.There is an island in the middle of the lake."
                 "What do you want to do? Wait or Swim?")
    if action == "Swim" or action == "swim":
        print("Attacked by alligator\nGAME OVER")
    elif action == "Wait" or action == "wait":
        door=input("You arrived at the island unharmed. There is house with 3 doors."
                   "Which colour door you want to pass through? red,yellow or blue?")
        if door =="Red" or door =="red":
            print("You are burned by fire.\nGAME OVER")
        elif door =="Blue" or door =="blue":
            print("You are eaten by beasts.\nGAME OVER")
        elif door=="Yellow" or door=="yellow":
            print("You found the treasure.You Win")
        else:
            print("No such colour exists.\nGAME OVER")
else:
    print("Wrong input")