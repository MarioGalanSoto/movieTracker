import json
import random
import os

clear = lambda: os.system('clear')

# Constants for file paths
UNSEEN_FILE = 'unseen_movies.json'
SEEN_FILE = 'seen_movies.json'

#prompt the user and clear the screen on key press
def pressAnyKey():
    anykey = input("\nPress any key to continue...\n")
    clear()

def load_movies(file_path):
    """Load movies from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

def save_movies(file_path, movies):
    """Save movies to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(movies, file, indent=4)

def add_movie():
    """Add a new movie to the unseen list."""
    movie = input("Enter the movie name: ")
    unseen_movies = load_movies(UNSEEN_FILE)
    unseen_movies.append(movie)
    save_movies(UNSEEN_FILE, unseen_movies)
    print(f"'{movie}' has been added to the unseen movies list.")

def display_unseen_movies():
    """Display the list of unseen movies."""
    unseen_movies = load_movies(UNSEEN_FILE)
    if unseen_movies:
        print("Unseen Movies:")
        for i, movie in enumerate(unseen_movies, 1):
            print(f"{i}. {movie}")
    else:
        print("No unseen movies found.")

def display_seen_movies():
    """Display the list of seen movies."""
    seen_movies = load_movies(SEEN_FILE)
    if seen_movies:
        print("Seen Movies:")
        for i, movie in enumerate(seen_movies, 1):
            print(f"{i}. {movie}")
    else:
        print("No seen movies found.")

def mark_movie_as_seen():
    """Mark a movie from the unseen list as seen."""
    display_unseen_movies()
    unseen_movies = load_movies(UNSEEN_FILE)
    seen_movies = load_movies(SEEN_FILE)
    if unseen_movies:
        try:
            movie_index = int(input("Enter the number of the movie you have seen: ")) - 1
            if 0 <= movie_index < len(unseen_movies):
                movie = unseen_movies.pop(movie_index)
                seen_movies.append(movie)
                save_movies(UNSEEN_FILE, unseen_movies)
                save_movies(SEEN_FILE, seen_movies)
                print(f"'{movie}' has been moved to the seen movies list.")
            else:
                print("Invalid selection.")
        
        except ValueError:
            print("Please enter a valid number.")

        

def delete_movie():
    """Delete a movie from the unseen or seen list."""
    while True:
        choice = input("Do you want to delete from unseen (u) or seen (s) list? you can also press (n) if you want to go back: ")
        print("\n")
        if choice.lower() == 'u':
            display_unseen_movies()
            unseen_movies = load_movies(UNSEEN_FILE)
            if unseen_movies:
                try:
                    movie_index = int(input("Enter the number of the movie to delete: ")) - 1
                    if 0 <= movie_index < len(unseen_movies):
                        movie = unseen_movies.pop(movie_index)
                        save_movies(UNSEEN_FILE, unseen_movies)
                        print(f"'{movie}' has been deleted from the unseen movies list.")
                        #in loop until this point (success)
                        break;
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice.lower() == 's':
            display_seen_movies()
            seen_movies = load_movies(SEEN_FILE)
            if seen_movies:
                try:
                    movie_index = int(input("Enter the number of the movie to delete: ")) - 1
                    if 0 <= movie_index < len(seen_movies):
                        movie = seen_movies.pop(movie_index)
                        save_movies(SEEN_FILE, seen_movies)
                        print(f"'{movie}' has been deleted from the seen movies list.")
                        #in loop until this point (success)
                        break;
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid choice. Please enter 'u' or 's' or 'n'")
        

def random_unseen_movie():
    """Pick a random movie from the unseen list."""
    unseen_movies = load_movies(UNSEEN_FILE)
    if unseen_movies:
        movie = random.choice(unseen_movies)
        print(f"Randomly selected unseen movie: {movie}")
    else:
        print("No unseen movies found.")

def display_menu():
    """Display the main menu."""
    print("\nMovie Watch List Menu\n")
    print("1. Add a movie")
    print("2. Get a random unseen movie")
    print("3. Display unseen movies")
    print("4. Mark a movie as seen")
    print("5. Delete a movie")
    print("6. Exit")
    print("\n")

def main():
    """Main function to run the menu-driven program."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        print("\n")
        if choice == '1':
            add_movie()
            pressAnyKey()
        elif choice == '2':
            random_unseen_movie()
            pressAnyKey()
        elif choice == '3':
            display_unseen_movies()
            pressAnyKey()
        elif choice == '4':
            mark_movie_as_seen()
            pressAnyKey()
        elif choice == '5':
            delete_movie()
            pressAnyKey()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

