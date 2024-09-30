import random
import numpy as np

def main():
    normal_force_x = 6
    std_dev_norm_force_x = 0.5
    angle = 2
    std_dev_angle = 0.1
    num_iterations = 100000
    
    force_samples = np.random.normal(normal_force_x, std_dev_norm_force_x, num_iterations)
    angle_samples = np.random.normal(angle, std_dev_angle, num_iterations)
    
    # Calculate propagated error
    propagated_error = np.sqrt((std_dev_norm_force_x / normal_force_x)**2 + (std_dev_angle / angle)**2)
    
    z = force_samples / angle_samples
    
    print(np.std(z))

if __name__ == "__main__":
    main()