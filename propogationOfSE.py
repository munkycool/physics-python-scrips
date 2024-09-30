import numpy as np

def main():
    angle1 = 31
    std_dev_angle1 = 0.5
    force1 = 450
    std_dev_force1 = 10
    
    angle2 = 44
    std_dev_angle2 = 0.5
    force2 = 320
    std_dev_force2 = 10
    
    x = np.sqrt((std_dev_force1 * np.cos(np.deg2rad(angle1)))**2 + (force1 * np.sin(np.deg2rad(angle1)) * np.deg2rad(std_dev_angle1))**2)
    y = np.sqrt((std_dev_force2 * np.cos(np.deg2rad(angle2)))**2 + (force2 * np.sin(np.deg2rad(angle2)) * np.deg2rad(std_dev_angle2))**2)
    print("Standard propogation of #1: ", x)
    print("Standard propogation of #2: ", y)
    
    # net uncertainty
    z = np.sqrt(x**2 + y**2)
    
    print("Net of #1 and #2: ", z)
    
if __name__ == "__main__":
    main()