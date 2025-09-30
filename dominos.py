import random
class Dominos:
    menu={
        "veg":{"margerita":129,"cheese_and_corn":169,"peppi_paneer":260,"veg loaded":210,"tomato_tangi":170},
        "non_veg":{"pepper barbeque":199,
                  "non_veg_loaded":169,
                  "chicken_sausage":200},
        "snacks":{'garlic_bread':120,
                  'zingy':59,
                  'chicken_cheese_balls':170},
        "desserts":{'choco_lava':100,
                    'mousse cake':169},
        "drinks":{'coke':90,'pepsi':78,'sprite':50}
    }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #to validate login status
        self.cart={} #to store orders
        #main program
        while True:
            if not self.login_status:
                print("---------------WELCOME TO DOMINOS APP---------------------")
                print("Login")
                ch=input("Do you want to Login?(y/n):").lower()
                if  ch=='y':
                    self.login()
            if self.login_status:        
                print("user:",self.name)    
                print("enter 1: Order")  
                print("enter 2: show cart")  
                print("enter 3: logout")
                choice=int(input("enter choice:"))
                if choice==1:
                    self.order()
                elif choice==2:
                    self.show_cart()
                elif choice==3:
                    self.logout()
                else:
                    print("invalid choice")
    @staticmethod
    def validate_otp(value):
        while True:  
            print('------------------------------------------')
            og_otp=random.randint(1000,9999)
            print(f"An otp has benn sent to {value}")
            print(f"your dominos otp is:{og_otp}")
            otp=int(input("enter otp:"))
            if  otp==og_otp:
                print("login successful")
                return  True
            print("incorrect otp enter correct otp")




    def login(self):
        print("Enter 1: Login with Phone")
        print("Enter 2: Login with email")
        ch=int(input("enter a choice:"))
        if ch==1:
            #phno validation
            phno=int(input("enter phno:"))
            if phno==self.phno:
                state=self.validate_otp(phno)
                self.login_status=state
                
            else:
                print("incorrect phno")
        elif ch==2:
            email=input("enter email:")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_state=state
            else:
                print("incorrect Email")
                        

        else:
            print("invalid choice")
    def order(self):
        print("------Dominos menu------------")
        for category in Dominos.menu:  #display categories
            print(category)
        cat=input("enter category:")
        if cat in Dominos.menu:
            d=Dominos.menu[cat]
            for item in d:  #display items of respective category
                print(item,'           Rs.',d[item])
            item=input("enter item:")
            if item in d:
                q=int(input("enter quantity:"))
                if item in self.cart:
                    self.cart[item]+=d[item]*q
                else:    
                    self.cart[item]=d[item]*q
                print(f"{item} added to the cart")
                print(self.cart)
            else:
                print(f"{item} not present")
        else:                      
            print(f'{cat} not available')

    def show_cart(self):
        print("-------Dominos Cart------")
        if self.cart!={}:
            total_bill=0
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,'----------Rs.',self.cart[item])
            print("total bill:...............Rs.",total_bill)
        else:
            print("cart is empty please order")
        if self.cart!={}:
            ch=input("do you want to place order?(y/n):").lower()
            if ch=='y':
                print('thank you for placing the order')
                print('your order is on the way')
                self.cart={}
        
    def logout(self) :
        ch=input("do you want to Logout?(y/n):").lower()      
        if ch=='y':
            self.login_status=False
            print("logged out") 

        

    
        
ob= Dominos("devadharshan",'deva117@gmail.com',6385743727)



