# Protocol:
#   {   "left_m":       <float left motor sp>,
#       "right_m":      <float right motor sp>,
#       "turret_s":     <bool turret start>,
#       "arm_up_s":     <bool start arm going up>
#       "arm_down_s":   <bool start arm going down>
#       "stop":         <bool stop the rove>
#   }

def readfile(filename = "exchange.txt"):
    data = {};
    fi = open(filename, "r");
    data["left_m"] = float(file.readline());
    data["right_m"] = float(file.readline());
    data["turret_s"] = bool(file.readline());
    data["arm_up_s"] = bool(file.readline());
    data["arm_down_s"] = bool(file.readline());
    data["stop"] = bool(file.readline());
    fi.close();
    return data;
