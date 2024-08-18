import sys

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    # Vulnerable to code injection if the input is not sanitized
    print("Hello, %s!" % user_input)
else:
    print("Hello, World!")
