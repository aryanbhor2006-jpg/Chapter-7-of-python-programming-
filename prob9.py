# Get the square's width and height.
n = int(input("Enter a number: "))

# Print each row of the square.
for i in range(n):
    # Print a solid row at the top and bottom.
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        # Print a hollow row between the borders.
        print("*" + " " * (n - 2) + "*")


'''output
****
*  *
****

'''