import pandas as pd

gps_data = pd.read_csv("../config/log/Graph1.txt")
acc_data = pd.read_csv("../config/log/Graph2.txt")

print(
    "gps std:",
    gps_data[" Quad.GPS.X"].std(),
    ", acc std:",
    acc_data[" Quad.IMU.AX"].std(),
)

# gps std: 0.6765889594082294 , acc std: 0.4825805329386176
print("done!")
