import random

def bernoulli_trial(p):
    """
    Simulate a Bernoulli trial with the given probability of success.

    Parameters:
    p (float): The probability of success.

    Returns:
    int: 1 for success, 0 for failure.
    """
    if random.random() < p:
        return 1  # Success
    else:
        return 0  # Failure

def main():
    try:
        p = float(input("Enter the probability of success: "))
        while p < 0 or p > 1:
            print("Error!\nYou must enter a probability between 0 and 1.")
            p = float(input("Enter the probability of success: "))

        result = bernoulli_trial(p)
        print("Outcome:", result)

    except ValueError:
        print("Invalid input. Please enter a valid probability.")
    except Exception as e:
        print("An error occurred:", e)

    print("End of the program")

if __name__ == '__main__':
    main()
