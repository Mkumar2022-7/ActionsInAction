import sys
import os

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    # Vulnerable to command injection
    #os.system(f"echo Hello, {user_input}!")
else:
    print("Hello, World!")
