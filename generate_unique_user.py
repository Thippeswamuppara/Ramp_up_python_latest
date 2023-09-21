import random
import string



# Function to generate a random username
def generate_username():

    l1=[]
    for j in range(1,11):
    # Generate a random string of letters and numbers
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        if random_string not in l1:
            l1.append(random_string)
            yield  l1[-1]

    # Combine timestamp and random string to create a unique username





# Example usage:
username = generate_username()
try:
    while True:
        print(username.__next__())
except:
    print("iterations over")

