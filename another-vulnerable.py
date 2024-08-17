import sys

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    # Vulnerable to insecure use of eval()
    eval(f'print("Hello, {user_input}!")')
else:
    print("Hello, World!")
