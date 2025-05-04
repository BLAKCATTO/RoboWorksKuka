import math
import csv

# Motion configuration in the format:
# (joint name, start value, end value, step_start, step_end, easing_function)
CONFIGURATION = [
# Theta1 - Main Joint Movement
    ('Theta1', 0, 80, 0, 300, 'ease_in_out_sine'),
    ('Theta1', 80, 80, 300, 600, None),#
    ('Theta1', 80, 30, 600, 900, 'ease_in_out_sine'),
    ('Theta1', 30, 30, 900, 1200, None),#
    ('Theta1', 30, 0, 1200, 1500, 'ease_in_out_sine'),

    # Theta2 - Arm Movement
    ('Theta2', 0, 0, 0, 300, None),#
    ('Theta2', 0, 85, 300, 600, 'ease_in_out_quad'),
    ('Theta2', 85, 40, 600, 900, 'ease_in_out_quad'),
    ('Theta2', 40, 65, 900, 1200, 'ease_in_out_quad'),
    ('Theta2', 65, 0, 1200, 1500, 'ease_in_out_quad'),

    # Theta3 - Elbow Movement
    ('Theta3', 0, 0, 0, 300, None),#
    ('Theta3', 0, -50, 300, 600, 'ease_in_out_quad'),
    ('Theta3', -50, -50, 600, 900, None),#
    ('Theta3', -50, -70, 900, 1200, "ease_in_out_quad"),
    ('Theta3', -70, 0, 1200, 1500, 'ease_in_out_quad'),

    # Theta4 - Wrist Rotation
    ('Theta4', 0, 0, 0, 300, None),#
    ('Theta4', 0, 0, 300, 600, None),#
    ('Theta4', 0, 0, 600, 900, None),#
    ('Theta4', 0, 90, 900, 1200, 'linear'),
    ('Theta4', 90, 0, 1200, 1500, 'linear'),
    
    # Theta5 - Grapple
    ('Theta5', 0, 0, 0, 300, None),#
    ('Theta5', 0, 60, 300, 600, 'ease_in_out_sine'),
    ('Theta5', 60, 60, 600, 900, None),#
    ('Theta5', 60, 0, 900, 1200, 'ease_in_out_sine'),
    ('Theta5', 0, 0, 1200, 1500, None),#
    
    # Theta6 - Tool Rotation
    ('Theta6', 0, 0, 0, 300, None),#
    ('Theta6', 0, 0, 300, 600, None),#
    ('Theta6', 0, 0, 600, 900, None),#
    ('Theta6', 0, 90, 900, 1200, 'ease_in_out_sine'),
    ('Theta6', 90, 0, 1200, 1500, 'ease_in_out_quad')
]

JOINT_LIMITS = {
    'Theta1': (-185, 185),
    'Theta2': (-50, 90),
    'Theta3': (-120, 145),
    'Theta4': (-350, 350),
    'Theta5': (-120, 120),
    'Theta6': (-350, 350)
}

TOTAL_STEPS = 1500

# Easing functions
def ease_in_out_sine(t):
    return -(math.cos(math.pi * t) - 1) / 2

def ease_in_out_quad(t):
    if t < 0.5:
        return 2 * t * t
    return 1 - math.pow(-2 * t + 2, 2) / 2

def linear(t):
    return t

def clamp(value, min_val, max_val):
    return max(min(value, max_val), min_val)

def calculate_angle(step, config):
    joint, start, end, step_start, step_end, easing = config
    
    if step < step_start or step > step_end:
        return None
        
    t = (step - step_start) / (step_end - step_start)
    
    if easing == 'ease_in_out_sine':
        progress = ease_in_out_sine(t)
    elif easing == 'ease_in_out_quad':
        progress = ease_in_out_quad(t)
    elif easing == 'linear':
        progress = linear(t)
    elif easing == 'sin':
        progress = math.sin(math.pi * t)
    else:  # For constant values
        return end
        
    return start + (end - start) * progress

def generate_animation():
    steps = [{} for _ in range(TOTAL_STEPS)]
    
    # Initialize starting positions
    for joint in JOINT_LIMITS:
        for step in range(TOTAL_STEPS):
            steps[step][joint] = 0.0
    
    # Configuration application
    for config in CONFIGURATION:
        joint = config[0]
        for step in range(config[3], config[4]+1):
            if step >= TOTAL_STEPS:
                continue
            value = calculate_angle(step, config)
            if value is not None:
                steps[step][joint] = value
    
    # Clamping and rounding
    for step in range(TOTAL_STEPS):
        for joint in JOINT_LIMITS:
            steps[step][joint] = clamp(round(steps[step][joint], 2), *JOINT_LIMITS[joint])
    
    return steps

def save_to_csv(steps, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(['KukaTheta-1', 'KukaTheta-2', 'KukaTheta-3', 
                        'KukaTheta-4', 'KukaTheta-5', 'KukaTheta-6'])
        
        for step in steps:
            writer.writerow([
                f"{step['Theta1']:.2f}",
                f"{step['Theta2']:.2f}",
                f"{step['Theta3']:.2f}",
                f"{step['Theta4']:.2f}",
                f"{step['Theta5']:.2f}",
                f"{step['Theta6']:.2f}"
            ])

if __name__ == "__main__":
    animation = generate_animation()
    save_to_csv(animation, 'kuka_animation.txt')
    print("Animations with "+str(TOTAL_STEPS)+" steps generated in kuka_animation.txt file")