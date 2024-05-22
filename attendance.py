import math

def main():
    # Prompt user for input
    lecture = int(input("Enter number of total lectures: "))
    absent = int(input("Enter number of total absents: "))
    delegation = int(input("Enter number of total delegations: "))

    # Calculate attendance
    a = absent - delegation
    b = a / lecture
    c = b * 100
    d = 100 - c
    attendance = math.floor(d)  # Round down to the nearest whole number

    # Display the attendance
    print(f"Your total Attendance is: {attendance}%")

    # Calculate fine if attendance is less than 90%
    if attendance < 90:
        fine = (90 - attendance) * 400
        print(f"Your attendance is less than 90%. You will be charged a fine of: {fine} rupees")

# Call the main function
if __name__ == "__main__":
    main()
