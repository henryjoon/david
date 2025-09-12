def is_num(num) -> bool: 
    
    try: 
        float(num) 
        return True 
    
    except: 
        return False 


def input_values():
    
    diameter = input("Input diameter(q: quit): ")
    if diameter == "q":
        return "quit"
    if not diameter:
        return "no_input_diameter"
    if not is_num(diameter):
        return "not_number_diameter"
    if float(diameter)<=0:
        return "Invalid_diameter"
    
    material = input("Input material(유리(glass), 알루미늄(aluminium), 탄소강(carbon_steel), q: quit): ")
    if material == "q":
        return "quit"
    if not material:
        return "no_input_material"
    if material not in ["glass", "유리", "aluminium", "알루미늄", "carbon steel", "carbon_steel", "탄소강"]:
        return "Invalid_input"
    return [float(diameter), material]


def sphere_area(diameter, material, thickness = 1):
    
    density_dictionary = {
        "glass" : 2.4,
        "유리": 2.4,
        "aluminium": 2.7,
        "알루미늄": 2.7,
        "carbon_steel": 7.85,
        "carbon steel": 7.85,
        "탄소강": 7.85
    }
    radius = diameter/2
    gravity_mars = 0.38
    density = density_dictionary[material]
    PI = 3.1415926535
    
    surface = 2*PI*radius*radius
    mass = density * ((2/3 * PI * radius*radius*radius)-(2/3 * PI * (radius-1)*(radius-1)*(radius-1))) * gravity_mars
    
    print(f"재질 => {material}, 지름 => {diameter}, 두께 => {thickness}, 면적 => {surface}, 무게 => {mass}")
    
    
def main():
    
    continuous = True
    
    while continuous == True:
        get_value = input_values()
        match get_value:
            case "quit":
                continuous = False
                break
            case "not_number_diameter":
                print("Hint: diameter should be number.")
            case "no_input_diameter":
                print("Hint: None value is not allowed.")
            case "Invalid_diameter":
                print("Hint: diameter should be greater than 0")
            case "no_input_material":
                print("Hint: None value is not allowed.")
            case "Invalid_input":
                print("Hint: material should be in this list - [glass, 유리, aluminium, 알루미늄, carbon steel, carbon_steel, 탄소강]")
            case _:
                sphere_area(get_value[0], get_value[1])
        

if __name__ == "__main__":
    main()