import util;
import mp_io as mio;
import motor-shield.PiMotor as pim;

def main():
    left_m = pim.Motor("MOTOR1", 1);
    right_m = pim.Motor("MOTOR2", 1);
    arm_m = pim.Motor("MOTOR3", 1);
    turret_m = pim.Motor("MOTOR4", 1);

    while True:
        in_data = mio.readfile();

        util.setmotor(left_m, in_data["left_m"]);
        util.setmotor(right_m, in_data["right_m"]);

if __name__ == "__main__":
    main()
