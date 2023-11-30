import os
import csv
import pymysql
from menu_functions import* 
from database_functions import* 
from sql_script import*
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

connection, cursor = setup_db_connection()

products = []
load_data("original_products.csv", products)

couriers_list = []
load_data("original_couriers.csv", couriers_list)

status_list = []    
open_file('status_list.txt', status_list)

order_dict = []
load_data("original_orders.csv", order_dict)
    

is_running = True

while is_running:
    clear_screen()
    print(" ""\nWelcome to the Main Menu \n 0.Leave the app \n 1.Products menu \n 2.Couriers list \n 3.Ordering menu ")
    option = input(f" Which option would you like? ")  
    
    if option == "0":
        is_running = False
        os.system('cls')

        storing_data_p(products)
        
        storing_data_c(couriers_list)
        
        storing_data_o(order_dict)
        
        print("Exiting app")


    elif option =="1":
        clear_screen()
        keep_in_product_menu = True
        while keep_in_product_menu:
            product_menu_opt = (" ""\nThis is the Products Menu \n 0.Return to main menu \n 1.View product list \n 2.Add a product \n 3.Update product name \n 4.Delete a product")
            print(product_menu_opt)
            main_menu = input(f"What would you like to do? ")
             
            if main_menu == "0":
                print("Returning to main menu...")
                keep_in_product_menu = False
            elif main_menu == "1":
                database_p()
            elif main_menu == "2":
                new_product = input("What product would you like to add? ")
                while True:
                    try:
                        new_product_price = float(input("Please ensure you enter a price below 10.0 \nWhat would you like the price to be in pounds and pence? "))
                        assert type(new_product_price) is float 
                        assert new_product_price <= 10
                        db_p_add(new_product, new_product_price)
                        break
                    except AssertionError:
                        print("Invalid price, please try again")
                    except ValueError:
                        print("Invalid price, please try again")
            elif main_menu == "3":
                database_p()
                while True:
                    try:
                        ask_two = int(input("What is the Product ID for the product that you would like to update? "))
                        ask_name = input("What would you like to update the product name to? ")
                        if ask_name == "":
                            pass
                        else:
                            dbp_update_name(ask_name, ask_two)
                            print("Product name has been updated successfully!")
                        ask_price = (input("In pounds and pence, what would you like to update the price to be? "))
                        if ask_price == "":
                            print("No updates made \nReturning to Product Menu...")
                        else:
                            float(ask_price)
                            dbp_update_price(ask_price, ask_two)
                            print("Product price has been updated successfully!")
                    except ValueError:
                        print("\nCharacter entered is not a number \nPlease select 1 to view the Products available ")
                    except AssertionError:
                        print("\nNumber entered is out of range \nPlease select 1 to view the Products available ")
                    finally:
                        break     
            elif main_menu == "4":
                database_p()
                dbp_remove()
                
    elif option == "2":
        clear_screen()
        keep_in_courier_menu = True
        while keep_in_courier_menu:
            courier_menu = (" ""\nThis is the Couriers Menu \n 0.Return to Main Menu \n 1.View the courier list \n 2.Add a new courier \n 3.Update an existing courier \n 4.Delete a courier")
            print(courier_menu)
            courier_option = input(f"Which option would you like? ")
            if courier_option == "0":
                print("Returing to the Main Menu... ")
                keep_in_courier_menu = False
            elif courier_option == "1":
                database_c()
            elif courier_option == "2":
                additional_c = input(f"What is the name of the new courier that you would like to add? ")
                while True:  
                    additional_cnumber = input(f"What is the couriers contact number? ")
                    if len(additional_cnumber) != 11:
                        print("\nInvalid phone number. Please enter a 11-digit number")
                    elif not additional_cnumber.isnumeric():
                        print("\nInvalid phone number. Please enter only numbers.")
                    else:
                        break
                database_c_add(additional_c, additional_cnumber)
            elif courier_option == "3":
                database_c()
                while True:
                    try:
                        courier_position = int(input(f"Enter the Courier ID associated with your desired courier "))
                        update_request = input("Please enter 0 to update courier name or 1 to update the couriers number ")
                        if update_request == "0":
                            courier_name = input(f"What would you like to change the couriers name to? ")
                            database_c_update(courier_name, courier_position)
                        elif update_request == "1":
                            courier_num = input("What is the updated number for the courier? ")
                            dbc_update_num(courier_num, courier_position)
                        else:
                            print("No entry made \nReturning to Courier Menu...")
                    except ValueError:
                            print("\nCharacter entered is not a number \nPlease select 1 to view the Couriers available ")
                    except AssertionError:
                            print("\nNumber entered is out of range \nPlease select 1 to view the Couriers available ")
                    finally:
                            break
            elif courier_option == "4":
                database_c()
                dbc_remove()
                
                
    elif option == "3":
        clear_screen()
        keep_in_order_menu = True
        while keep_in_order_menu:       
                        
            ordering_menu = input(f" ""\nThis is the Orders Menu\n 0.Return to main menu \n 1.View Orders list \n 2.Input your details \n 3.Order status update \n 4.Update an exisiting order \n 5.Delete your order ")
            if ordering_menu == "0":
                print("Returning to the main menu")
                keep_in_order_menu = False
            elif ordering_menu == "1":
                print("The orders List: ")
                view_topic_o(order_dict)
            elif ordering_menu == "2":
                customer_name = input(f"Please enter your name ")
                customer_address = input(f"Please enter your address ")
                while True:
                    customer_number = input(f"Please provide a contact number ")
                    if len(customer_number) != 11:
                        print("\nInvalid phone number. Please enter a 11-digit number")
                    elif not customer_number.isnumeric():
                        print("\nInvalid phone number. Please enter only numbers.")
                    else:
                        break
                while True:
                    try:
                        view_topic_c(couriers_list)
                        customer_courier = int(input(f'Please enter the number assosiated with the courier you would like '))
                        assert customer_courier in ((range(len((couriers_list)))))
                        print(numbered_list(status_list))
                        customer_status = int(input(f"Please enter the number associated with the status update you would like "))
                        assert customer_status in ((range(len((status_list)))))
                        view_topic(products) 
                        items_question = input("Please enter the numbers associated with the products you would like ")
                        second_dict= {"customer name": customer_name , "customer address": customer_address , 
                        "customer number": customer_number , "courier": customer_courier, "status": status_list[customer_status], "items": items_question}
                        add_new_item(order_dict, second_dict)
                        print("Your order has been added successfully!")
                        break
                    except ValueError:
                            print("\nCharacter entered is not a number \nPlease try again ")
                    except AssertionError:
                            print("\nNumber(s) entered is out of range \nPlease try again ")
                    
            elif ordering_menu == "3":
                view_topic_o(order_dict)
                while True:
                    try:
                        status_update = int(input(f"what position is your order at within the queue? "))
                        assert status_update in ((range(len((order_dict)))))
                        print(numbered_list(status_list))
                        status_choice = int(input("Enter the number associated with the status update you would like "))
                        assert status_choice in ((range(len((status_list)))))
                        order_dict[status_update]["status"] = status_list[status_choice]
                        print("Status updated!")
                        break
                    except ValueError:
                        print("\nCharacter entered is not a number \nPlease try again ")
                    #if status_choice == "":
                    except AssertionError:
                        print("\nNumber entered is out of range \nPlease try again: ")
                    
            elif ordering_menu == "4":
                view_topic_o(order_dict)
                while True:
                    try:
                        update_deets = int(input(f"Please enter the position your order currently occupies within the queue? "))
                        assert update_deets in ((range(len((order_dict)))))
                        specific_order = order_dict[update_deets]
                        print("\nThis is your order: ")
                        print(specific_order)
                        order_breakdown = (tuple(enumerate(specific_order.keys())))
                        print("\nSections available to update:")
                        print(order_breakdown)
                        update_section = (int(input("Which section would you like to update? ")))
                        if update_section == 0:
                            name_updated = input(f"Enter the name you would like ")
                            order_dict[update_deets]["customer name"] = name_updated
                            print("Name Updated")
                        elif update_section == 1:
                            address_updated = input(f"Enter the new address ")
                            order_dict[update_deets]["customer address"] = address_updated
                            print("Address updated")
                        elif update_section == 2:
                            number_updated = input(f"What would you like to change your number to? ")
                            order_dict[update_deets]["customer number"] = number_updated
                            print("Contact number updated")
                        elif update_section == 3: 
                            view_topic_c(couriers_list)
                            courier_update = int(input(f"Enter the number associated with the courier that you would like? "))
                            order_dict[update_deets]["courier"] = courier_update  
                            print("Courier has been updated") 
                        elif update_section == 4:
                            print(numbered_list(status_list))
                            status_renewal = int(input("Enter the number associated with the status update you would like "))
                            order_dict[update_deets]["status"] = status_list[status_renewal]
                            print("Status has been updated")
                        elif update_section == 5:
                            view_topic(products)
                            item_renewal = input("Please use commas to seperate your choices \nPlease list the numbers associated with the products you would like ")
                            order_dict[update_deets]["items"] = item_renewal
                            print("Product selection has been updated")
                        else:
                            print("No updates made as you've not selected a section to edit \nReturnng to the the Orders Menu...")
                    except ValueError:
                        print("\nCharacter entered is not a number \nPlease select 1 to see the current Order List ")
                    except AssertionError:
                        print("\nNumber entered is out of range \nPlease select 1 to see the current Orders List")
                    finally:
                        break
            elif ordering_menu == "5":
                view_topic_o(order_dict)
                order_dict = list(order_dict)
                error_checking_delO(order_dict)
                