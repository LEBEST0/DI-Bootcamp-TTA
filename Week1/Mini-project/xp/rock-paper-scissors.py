from game import Game
def get_user_menu_choice():
    print(f"""Choice an option using letters like this :
          (P) for Play a new game
          (S) to Show scores
          (X) - to Quit the program
          """)
    return input("Choice an option: ").lower()

def print_results(results):
    print(f"Number of game won: {results['win']}\n")
    print(f"Number of game lost: {results['loss']}")
    print(f"Number of game drew: {results['draw']}")


def main():
    results={
        "win":0,
        "loss":0,
        "draw":0
    }
    rep=get_user_menu_choice()
    while True:
        
        while rep not in ["p", "s", "x"]:

            rep = input(
                "Invalid choice. Enter p, s or x: "
            ).lower()

        if rep=="p":
            game=Game()
            result=game.play()
            results[result]+=1

        elif rep=="s":
            print_results(results)
        
        else:
            print_results(results)
            break

        rep=get_user_menu_choice()
    

main()



       
