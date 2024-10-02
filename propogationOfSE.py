import numpy as np

def main():
    angle1 = 19
    std_dev_angle1 = 1
    force1 = .6029099
    std_dev_force1 = .012058198
    
    angle2 = 127
    std_dev_angle2 = 1
    force2 = .9739314
    std_dev_force2 = .019478628
    
    angle3 = 270
    std_dev_angle3 = 1
    force3 = -1.034955
    std_dev_force3 = .0206991
    
    x = np.sqrt((std_dev_force1 * np.cos(np.deg2rad(angle1)))**2 + (force1 * np.sin(np.deg2rad(angle1)) * np.deg2rad(std_dev_angle1))**2)
    y = np.sqrt((std_dev_force2 * np.cos(np.deg2rad(angle2)))**2 + (force2 * np.sin(np.deg2rad(angle2)) * np.deg2rad(std_dev_angle2))**2)
    z = np.sqrt((std_dev_force3 * np.cos(np.deg2rad(angle3)))**2 + (force3 * np.sin(np.deg2rad(angle3)) * np.deg2rad(std_dev_angle3))**2)
    print("Standard propogation of #1: ", x)
    print("Standard propogation of #2: ", y)
    print("Standard propogation of #3: ", z)
    
    # net uncertainty
    f = np.sqrt(x**2 + y**2 + z**2)
    
    
    print("Net of #1 and #2 and #3: ", f)
    
if __name__ == "__main__":
    main()