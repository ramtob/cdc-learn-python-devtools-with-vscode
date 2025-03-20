import warnings

# Function to calculate gravity based on the planet
def calculate_gravity(planet):
    planet_gravity = {
        "Earth": 9.8,
        "Mars": 3.7,
        "Venus": 8.87
    }
    if planet not in planet_gravity:
        return "Unknown planet"  
    return planet_gravity[planet]

# Function to check astronaut health based on health score
def check_astronaut_health(health_score):
    if health_score < 0:
        return "Invalid health score"  
    elif health_score < 50:
        return "Astronaut not fit for the mission"
    return "Astronaut is fit for the mission"

# Function to add a planet to the mission plan
def add_planet_to_mission(planet, mission_plan):
    if planet in mission_plan:
        warnings.warn(f"{planet} is already in the mission plan", UserWarning)
    else:
        mission_plan.append(planet) 
    return mission_plan
