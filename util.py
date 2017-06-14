def setmotor(motor, pvbus):
	if abs(pvbus) > 100:
		print str(pvbus) + " is too high. Setpoints must be within +- 100"
	if pvbus > 0:
		motor.forward(pvbus)
	elif pvbus < 0:
		motor.reverse(pvbus)
	else:
		motor.stop()
