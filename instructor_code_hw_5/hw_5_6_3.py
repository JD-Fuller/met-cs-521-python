while True:

    user_input = input("Enter three comma separated numbers: ").strip().split(',')
    if len(user_input) != 3:
        print('You must enter 3 numbers')
        continue

    try:
        num_list = [float(e) for e in user_input]
        calc = num_list[0] / num_list[1] + num_list[2]
    except ValueError as e:
        print("error: {}".format(e))
    except ZeroDivisionError as e:
        print("Error: {}".format(e))
    else:
        print("{} / {} + {} = {:,.4f}".format(num_list[0], num_list[1], num_list[2], calc))
        break
