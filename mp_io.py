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
    data["left_m"] = float(fi.readline());
    data["right_m"] = float(fi.readline());
    data["turret_s"] = bool(fi.readline());
    data["arm_up_s"] = bool(fi.readline());
    data["arm_down_s"] = bool(fi.readline());
    data["read_data"] = bool(fi.readline());
    data["stop"] = bool(fi.readline());
    fi.close();
    return data;
