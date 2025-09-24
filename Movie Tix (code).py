# Program #2: Movie Tix

# Ask how many movies the user wants to enter
num_movies = int(input("How many movies would you like to enter? "))

# Keep track of total tickets
total_tickets = 0

# Loop through each movie
for i in range(1, num_movies + 1):
    movie = input(f"\nEnter the name of movie #{i}: ")
    tickets = int(input(f"How many tickets do you want for '{movie}'? "))
    total_tickets += tickets

# Final result
print("\n----- Summary -----")
print(f"Total number of tickets desired: {total_tickets}")
