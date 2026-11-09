# Project: Volleyball Practice Helper
# Purpose: This program guides a volleyball player through checking their gear and choosing a practice routine.

print("Welcome to volleyball")

# [DATA TYPE 1 & 2: Strings and Booleans]
shoe_check = str(input("Did you get shoes on? [y/n] ")).lower()
pad_check = str(input("Did you get knee pad on? [y/n] ")).lower()
is_ready = False # Added a Boolean data type to meet the 3 distinct data types requirement

if shoe_check == "y" and pad_check == "y":
    is_ready = True

# Function Purpose: Coordinates the volleyball gear check and manages the practice menu loop.
def main():
    # [DECISION STRUCTURE]
    if not is_ready:
        print("Get ready and grab your shoes or knee pads!")
        
        # [DATA TYPE 3: List] - Created and now properly iterated/accessed
        volleyball_sizes = ["Size 5 (Standard)", "Oversized (30 inches)"]
        print("Make sure you also grab the right ball size:")
        for size in volleyball_sizes:
            print(f"- {size}")
  
    elif is_ready:
        print("\n1. Do you want a practice regimen that is pre-made? \n2. Do you wanna warm up? \n3. Do you want to practice bumping  \n4. Do you want to practice setting \n5. Do you want to practice serving \n6. Do you want to practice receiving \n7. Exit")
        
        # [LOOPING STRUCTURE]
        while True:
            user_choice = int(input("\nEnter number: ")) # Integer data type
            if user_choice == 1:
                print("Lets start")
            elif user_choice == 2:
                print("Jog for 8 minutes, 15 jumping jacks, open gates + closing gates to net and back, scoops to the net and back.")
            elif user_choice == 3:
                print("Pass the ball with a partner or with a wall: 2 sets of 20")
            elif user_choice == 4:
                print("Set to the wall or a teammate: 2 sets of 30")
            elif user_choice == 5:
                print("Serve the ball over the net: 1 set of 10")
            elif user_choice == 6:
                print("Receive serves/digs with the wall or a partner")
            elif user_choice == 7:
                break
            else:
                print("Please enter a number from 1 to 7.")
                
        print("End strong by stretching!")

# Calling the custom function to run the program
main()
