class Phone:
    def __init__(self,phone_number):
        self.call_history=[]
        self.messages=[]
        self.phone_number=phone_number
    
    def call(self,other_phone:Phone):
        print(f"you are calling {other_phone.phone_number}")
        print(f"{other_phone.phone_number} is calling by {self.phone_number} (you)")
        self.call_history.append(f"you called {other_phone.phone_number}")
        other_phone.call_history.append(f"{self.phone_number} call {other_phone.phone_number}")

    def show_call_history(self):
        for e in self.call_history:
            print(f"{e} \n")
    
    def send_message(self,other_phone:Phone,content):
        self.messages.append({"to":other_phone.phone_number,"from":self.phone_number,"content":content})
        other_phone.messages.append({"to":other_phone.phone_number,"from":self.phone_number,"content":content})
    
    def show_outgoing_messages(self):
        for elt in self.messages:
            if elt["from"]==self.phone_number:
               print(f"{elt["content"]}")
    
    def show_incoming_messages(self):
        for elt in self.messages:
            if elt["to"]==self.phone_number:
               print(f"{elt["content"]}")
    def show_messages_from(self,other:Phone):
        for elt in self.messages:
            if elt["from"]==other.phone_number:
               print(f"{elt["content"]}")

phone2=Phone("joel")   
phone1=Phone("AKRE")
phone1.send_message(phone2,"salut Joel mon ami")
phone1.call(phone2)
print(phone1.call_history)
print(phone1.messages)

