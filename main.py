
 
from functions import to_do_create, delete_task_function, print_to_do

def main():

    # creating a to do list
    to_do_create()
    print_to_do(to_do)

    #deleting items
    delete_task_function()
    print_to_do(to_do)

    #printing the final list
    print_to_do(to_do)


if __name__ == "__main__":
    main()


