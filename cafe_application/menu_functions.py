# product_list = open("product_list.txt").read().split()
# print(product_list)
# import csv
# products = []
# with open ("product_list.txt", "r") as file:
#     product_list = csv.reader(file, delimiter='\n')
#     for row in product_list:
#        print(row)
#     #    products.append(product) 
#     # print(product_list)
        


# new_product = input("enter product name")


# couriers_list = open("couriers_list.txt").read().split()
# print(couriers_list)
# courier_index = list(couriers_list)
# new_courier_index = enumerate(couriers_list)
# print(list(new_courier_index))

# order_status_list = ["processing", "preparing", "ready", "out for deliver"]

#  products.pop(not_want_position)

def add_item_list(a, b):
    return a + b
    

# fruits = ("orange", "lemon", "strawberry")
# question = int(input(f"choose a number"))
# answer = add_item_list(5 , 8 )
# print(answer)

# def save_data(filename, data):     
#     try:        
#         with open(filename, 'w') as file:             
#             for item in data:                 
#                 file.write(str(item) + '\n')        
#                 print(f"Data saved to {filename} successfully.\n")     
#     except IOError:         
#         print(f"Error saving data to {filename}.\n")


# del topic[position]
    # topic.insert((position), (new_item))
import csv
import os

def numbered_list(order_type):
    order_index = list(order_type)
    new_order_index = enumerate(order_index)
    return (list(new_order_index))

def open_file(filename, topic):
    with open (filename) as file:
        p_lines = file.read().split("\n")
        for line in p_lines:
            topic.append(line) 
        file.close()
        return

def saving_data(filename, topics):
    try:
        file_a = open(filename, "w")
        for topic in topics:
            file_a.write(f"{topic}\n")
        file_a.close()
        print(f"Data saved to {filename} successfully.\n")
    except IOError:         
        print(f"Error saving data to {filename}.\n")

def add_new_item(topic, new_item):
    topic.append(new_item)
    
def update_item(topic, position, new_item):
    topic[position] = new_item
def delete_item(topic, position):
    del topic[position]

def view_topic(topic):
    for i in range(len(topic)):
        print(f'\nProduct no. {i}')
        for key, value in topic[i].items():
            print(''f'{key}: {value}')

def view_topic_c(topic):
    for i in range(len(topic)):
        print(f'\nCourier no. {i}')
        for key, value in topic[i].items():
            print(''f'{key}: {value}')

def view_topic_o(topic):
    for i in range(len(topic)):
        print(f'\nOrder no. {i}')
        for key, value in topic[i].items():
            print(''f'{key}: {value}')

def load_data(filename, topic):
    try:    
        with open(filename, 'r') as data:
            for line in csv.DictReader(data):
                topic.append(line)
        #data.close()
    except IOError:         
        print(f"Error loading data from {filename}.\n")

def storing_data_p(topics):
    try:    
        with open('products.csv','w', newline='') as file_1:
                writer = csv.writer(file_1, delimiter=',')
                writer.writerow(['name','price'])
                for topic in topics:
                    writer.writerow(topic.values())
    except IOError:         
        print(f"Error saving data to {topics}.\n")

def storing_data_c(topics):
    try:    
        with open('couriers.csv','w', newline='') as file_2:
                writer = csv.writer(file_2, delimiter=',')
                writer.writerow(['courier name','courier number'])
                for topic in topics:
                    writer.writerow(topic.values())
    except IOError:         
        print(f"Error saving data to {topics}.\n")                

def storing_data_o(topics):
    try:    
        with open('orders_1.csv','w', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(['customer name', 'customer address', 'customer number', 'courier', 'status'])
                for topic in topics:
                    writer.writerow(topic.values())
    except IOError:         
        print(f"Error saving data to {topics}.\n")                

def error_check_deletingC(topic):
   while True:
                    try:
                        remove_c = int(input("Enter the number associated with the item that you would you like to remove? "))
                        assert remove_c in ((range(len((topic)))))
                        delete_item(topic, remove_c)
                        print("Deletion Successful!")
                    except ValueError:
                            print("\nCharacter entered is not a number \nPlease try again ")
                        #if status_choice == "":
                    except AssertionError:
                            print("\nNumber entered is out of range \nPlease try again ")
                    finally:
                            break

def error_checking_deletingP(topic):
     while True:
                    try:
                        not_want = int(input("Enter the number associated with the item that you would you like to remove? "))
                        assert not_want in ((range(len((topic)))))
                        delete_item(topic, not_want)
                        print("The product has been deleted successfully!")
                    except ValueError:
                            print("\nCharacter entered is not a number \nPlease select 1 to view the Products available ")
                        #if status_choice == "":
                    except AssertionError:
                            print("\nNumber entered is out of range \nPlease select 1 to view the Products available ")
                    finally:
                            break

def error_checking_delO(topic):
     while True:
                    try:
                        del_order = int(input(f"Please enter the number of the position that your order is in the queue "))
                        assert del_order in ((range(len((topic)))))
                        del topic[del_order]
                        print("Your order has been removed successfully!")
                        break
                    except ValueError:
                        print("\nCharacter entered is not a number \nPlease see below for the current Order List: ")
                    #if status_choice == "":
                    except AssertionError:
                        print("\nNumber entered is out of range \nPlease see below for the current Orders List: ")


def clear_screen():
      os.system('cls')


