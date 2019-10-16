#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program tells if you get a bonus in your salary
# with user input


def main():
    # This function tells if you get a bonus in your salary

    # input
    your_salary = (input("Enter your yearly salary: "))
    your_service = (input("Enter your year of service: "))

    # process & output
    try:
        salary_as_integer = int(your_salary)
        service_as_integer = int(your_service)
        if service_as_integer >= 5:
            net_bonus_amount = 0.05*salary_as_integer
            print("Your 5% bonus is: ${}".format(net_bonus_amount))
            print("")
        else:
            print("Continue working to earn that bonus!")
    except Exception:
        print("These were not integers!")
    finally:
        print("")
        print("Lets try again!!!")


if __name__ == "__main__":
    main()
