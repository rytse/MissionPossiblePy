import PiMotor
import time

def run():
    '''Procedure to test all the motor pins

    Outputs to the terminal which motor is being powered and which config is being executed.
    Calls the "Forward" method in order to demonstrate which config you should be using to 
    define the correct "forward" for your project.
'''
    d = ["MOTOR1","MOTOR2","MOTOR3","MOTOR4"]
    for motor in d:
        for config in range(1,3):
            print(motor + " config: " + str(config))
            m = PiMotor.Motor(motor,config)
            m.forward(100)
            time.sleep(0.2)
            #m.stop()
try:
    while True:
        # Continously test all the Motor's
        run()

except KeyboardInterrupt:
    print("\nExiting Motor Shield Testing\n")
    
