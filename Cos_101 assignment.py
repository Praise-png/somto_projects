print(''''
For speed press A
For presssure press B
For density press C
For force press D
For impulse press E
''')

def calculate_speed():
    distance=float(input('Enter distance'))
    time=float(input('Enter time'))
    speed=distance/time
    print(f"speed: {speed} units")


def calculate_pressure():
    force=float(input('Enter force'))
    area=float(input('Enter area'))
    pressure = force*area
    print(f"pressure:{pressure} units")

def calculate_density():
    mass=float(input('Enter mass'))
    volume=float(input('Enter volume'))
    density=mass/volume
    print(f"density: {density} units")

def calculate_force():
     mass=float(input('Enter mass'))
     acceleration=float(input('Enter mass'))
     force=mass*acceleration
     print(f"force: {force} N")
def calculate_impulse():
     force=float(input('Enter force'))
     time=float(input('Enter time'))
     impulse=force/time
     print(f"impulse: {impulse} units")

choice= input ("What do you need (A/B/C/D/E)? ").strip().upper()
if choice == 'A':
    calculate_speed()
elif choice == 'B':
    calculate_pressure()
elif choice == 'C':
    calculate_density()
elif choice == 'D':
    calculate_force()
elif choice == 'E':
    calculate_impulse()
else:
    print('Invalid choice. Please enter an alphabet between A to E')