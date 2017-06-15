import util;
import mp_io as mio;
import spi_bitbang as mcp3008;
import gaugette.rotary_encoder as encoder
import motorshield.PiMotor as pim;
import spi_bitbang
import RPi.GPIO as GPIO

CLK = 31
MOSI = 33
MISO = 35
CS = 37
TEMP_SENSOR = 0
LIGHT_SENSOR = 1
TURRET_PIN_A = 8
TURRET_PIN_B = 10
ANAMOMETER_PIN_A = 38
ANAMOMETER_PIN_B = 40

wind_a = [];

def main():
    left_m = pim.Motor("MOTOR1", 1);
    right_m = pim.Motor("MOTOR2", 1);
    arm_m = pim.Motor("MOTOR3", 1);
    turret_m = pim.Motor("MOTOR4", 1);
    turret_e = encoder.RotaryEncoder(TURRET_PIN_A, TURRET_PIN_B)
#    turret_e.start()
    anamometer_e = encoder.RotaryEncoder(ANAMOMETER_PIN_A, ANAMOMETER_PIN_B)
#    anamometer_e.start()

    c = 0;
    num = 0;

    prevTempVolts = 0.;

    while True:
        if num == 30:
            c = 0;
            num = 0;
        in_data = mio.readfile();

        util.setmotor(left_m, in_data["left_m"]);
        util.setmotor(right_m, in_data["right_m"]);

        if data["arm_up_s"]:
            util.setmotor(arm_m, -50.)
        else if data["arm_down_s"]:
            util.setmotor(arm_m, 50.)

        num += 1

        anamometer_e.update();
        if len(wind_a) > 30:
            wind_a.pop(0)
            wind_a.append(anamometer_e.get_steps());

        if in_data["read_data"]:
            s = sum(wind_a);
            print "Wind: "+str(s)
            if s <= 10:
                print "Wind speed: 0"
            elif s <= 15:
                print "Wind speed: 1"
            elif s <= 20:
                print "Wind speed: 2"
            else:
                print "Wind speed: 3"

#print "Temperature (volts): "+str(mcp3008.readAdc(TEMP_SENSOR, CLK, MISO, MOSI, CS))
#tempVolts =  spi_bitbang.readAdcChannel(0);

#if (tempVolts != 0):
#    prevTempVolts = tempVolts;

#print "Temperature (volts): " + str(tempVolts);

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    spi_bitbang.setupSpiPins(CLK, MISO, MOSI, CS)
    main()
