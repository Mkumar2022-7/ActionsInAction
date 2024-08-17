import sys

# Check if the user provided an argument
if len(sys.argv) > 1:
    # Take the first argument as input
    user_input = sys.argv[1]
    print(f"Hello, {user_input}!")
else:
    print("Hello, World!")
