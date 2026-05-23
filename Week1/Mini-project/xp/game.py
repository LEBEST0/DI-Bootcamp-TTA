import random
class Game():
    def __init__(self):
        self.possibility=["Rock","Paper","Scissors"]
        
    def get_user_item(self):
        rep=""
        while rep.lower()!=self.possibility[0].lower() and rep.lower()!=self.possibility[1].lower() and rep.lower() !=self.possibility[2].lower():
             rep=input("Enter your choice please: ")
        return rep
    
    def get_computer_item(self):

        return random.choice(self.possibility)
    
    def get_game_result(self, user_item, computer_item):
        if user_item==computer_item:
            
            return "draw"
        elif user_item==self.possibility[1] and computer_item==self.possibility[0] or user_item==self.possibility[2] and computer_item==self.possibility[1] or user_item==self.possibility[0] and computer_item==self.possibility[2]:
            return "win"
        else:
            return "loss"
        

    def play(self):
        user=self.get_user_item()
        ordi=self.get_computer_item()
        result=self.get_game_result(user,ordi)
        if result=="win":
            
            print(f"""
                You chose {user}.
                Computer chose {ordi}.
                You win 🤩
            """)
        elif result=="loss":
            print(f"""
                You chose {user}.
                Computer chose {ordi}.
                You Lost 💔
            """)
             
        else:
            print(f"""
                You chose {user}.
                Computer chose {ordi}.
                It's a draw 😂😊
            """)
        
        
        return result
    
