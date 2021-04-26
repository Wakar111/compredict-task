# function for user inputs for only numbers.

def inputValueSensor(counter):
    print('********* Enter '+ str(counter) + ' number(s) ****************')
    sensor = []

    while True:
        userInput = input('enter '+ str(counter) + '.number: ')
        try:
            val = float(userInput)
            sensor.append(val)

            counter -= 1

            if counter == 0:
                break

        except ValueError:
            print("That's not an number!")

    return sensor