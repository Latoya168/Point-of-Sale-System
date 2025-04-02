#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionary containing products and prices
import tabulate 

def main():
    products = {
        "Betty Milk": {"price": 500, "stock": 40},
        "Cheese": {"price": 1200, "stock": 20},
        "Pasta": {"price": 300, "stock": 20},
        "Dorritos": {"price": 150, "stock": 30},
        "Cranberry Juice": {"price": 700, "stock": 50},
        "Toothpaste": {"price": 450, "stock": 50},  
        "Bread": {"price": 500, "stock": 15},
        "Grace Franks": {"price": 800, "stock": 30},
        "Chiffon Butter": {"price": 500, "stock": 40}
    }
    
    cart = {}
    
    def display_products():
        print("\nAvailable Products:")
        headers = ["Product", "Price", "Stock", "Status"]
        table = [[product, f"${info['price']}", info["stock"], "Low Stock" if info['stock'] < 5 else "In stock"] for product, info in products.items()]
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        
    def add_to_cart():
        display_products()
        item = input("Enter product name (or 'exit' to cancel): ").title()
        if item.lower() == "exit":
            return
        if item not in products:
            print("Product not found.")
            return
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0 and products[item]["stock"] >= quantity:
                if item not in cart:
                    cart[item] = {"quantity": 0, "price": products[item]["price"]}
                cart[item]["quantity"] += quantity
                products[item]["stock"] -= quantity
                print(f"{quantity} {item}(s) added to cart.")
            else: 
                print("Invalid quantity or insufficient stock.")
        except ValueError:
            print("Please enter a valid number.")
    
    def remove_from_cart():
        if not cart:
            print("Cart is empty.")
            return
        
        item = input("Enter product name to remove (or 'exit' to cancel): ").title()
        if item.lower() == "exit":
            return
        if item not in cart:
            print("Item not found in cart.")
            return
        try:
            quantity = int(input("Enter quantity to remove: "))
            if quantity > 0 and cart[item]["quantity"] >= quantity:
                cart[item]["quantity"] -= quantity
                products[item]["stock"] += quantity
                if cart[item]["quantity"] == 0:
                    del cart[item]
                print(f"{quantity} {item}(s) removed from cart.")
            else:
                print("Invalid quantity.")
        except ValueError:
            print("Please enter a valid number.")
        
    def view_cart():
        if not cart:
            print("Cart is empty.")
            return
        
        print("\nShopping Cart:")
        headers = ["Product", "Quantity", "Unit Price", "Total"]
        table = [[product, details['quantity'], f"${details['price']}", f"${details['quantity'] * details['price']}"]
                 for product, details in cart.items()]
        print(tabulate.tabulate(table, headers, tablefmt="grid"))
        
    def checkout():
        if not cart:
            print("Cart is empty. Nothing to checkout.")
            return
        
        subtotal = sum(details["quantity"] * details["price"] for details in cart.values())
        tax_rate = 0.10
        discount_rate = 0.05 if subtotal > 5000 else 0
        
        tax = round(subtotal * tax_rate, 2)
        discount = round(subtotal * discount_rate, 2)
        total = subtotal + tax - discount
        
        print("\nCHECKOUT SUMMARY:")
        headers = ["Description", "Rate", "Amount"]
        summary_table = [
            ["Subtotal", "-", f"${subtotal}"],
            ["Sales Tax", f"{tax_rate * 100}%", f"${tax}"],
            ["Discount", f"{discount_rate * 100}%", f"-${discount}"],
            ["Total Due", "-", f"${total}"]
        ]
        print(tabulate.tabulate(summary_table, headers, tablefmt="grid"))
        
        try:
            payment = float(input("Enter payment amount: "))
            if payment >= total:
                change = round(payment - total, 2)
                generate_receipt(cart, subtotal, tax, discount, total, payment, change, tax_rate, discount_rate)
                cart.clear()
            else:
                print("Insufficient Payment. Please enter a valid amount.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
    def generate_receipt(cart, subtotal, tax, discount, total, payment, change, tax_rate, discount_rate):
        print("\n=====================RECEIPT=========================")
        print("BEST BUY RETAIL STORE\nMONEYVILLE ROAD\nKINGSTON")
        print("--------------------------------------------------------")
        
        for product, details in cart.items():
            print(f"{product:<20} {details['quantity']:>3} x ${details['price']:<5} = ${details['quantity'] * details['price']}")
        
        print("----------------------------------------------------")
        print(f"Subtotal:      ${subtotal}")
        print(f"Sales Tax ({tax_rate * 100}%):${tax}")
        print(f"Discount ({discount_rate * 100}%): -${discount}")
        print(f"Total Due:       ${total}")
        print(f"Amount Paid:     ${payment}")
        print(f"Change:          ${change}")
        print("====================================================")
        print("THANK YOU FOR SHOPPING WITH US!")
        print("BIG SAVINGS, NUFF CHOICES!")
    
    while True:
        print("\nBEST BUY RETAIL STORE - POS System")
        print("1. View Products")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_products()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                remove_from_cart()
            elif choice == 4:
                view_cart()
            elif choice == 5:
                checkout()
            elif choice == 6:
                print("Thank you for using the POS System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
        
if __name__ == "__main__":
    main()




        


        

     
             
    
    


            
                
            
                
        
        
        
                    
                    
                
        
                    
                
            


        


                




            
            
        
        
        



        





    


# In[ ]:





# In[ ]:




