from snake import create_tables, get_or_create_user, get_user_level, save_game

def run_game():
    create_tables()
    
    # Get username
    username = input("Enter your username: ")
    user_id = get_or_create_user(username)
    
    # Get current level of the user
    level = get_user_level(user_id)
    print(f"Hello, {username}! Your current level is: {level}")
    
    # Simulate a game: Get the score from user
    score = int(input("Enter your score (e.g., 300): "))
    
    # Calculate the next level (for simplicity, we just increment it)
    next_level = level + 1
    
    # Save the game data (score and level)
    save_game(user_id, score, next_level)
    print(f"Your new level: {next_level}")

if __name__ == "__main__":
    run_game()
