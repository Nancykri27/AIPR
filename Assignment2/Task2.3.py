import math

def calculate_area():
    """Calculate area of different shapes based on user input."""
    
    # Dictionary of available shapes and their required parameters
    shapes = {
        'circle': ['radius'],
        'rectangle': ['length', 'width'],
        'triangle': ['base', 'height'],
        'square': ['side'],
        'pentagon': ['side'],
        'ellipse': ['major radius', 'minor radius']
    }
    
    print("Available shapes:", ", ".join(shapes.keys()))
    shape = input("Enter the shape: ").lower().strip()
    
    try:
        if shape not in shapes:
            raise ValueError("Invalid shape selected")
            
        # Get measurements based on shape requirements
        measurements = {}
        for param in shapes[shape]:
            value = float(input(f"Enter the {param}: "))
            if value <= 0:
                raise ValueError(f"{param} must be positive")
            measurements[param] = value
            
        # Calculate area based on shape
        if shape == "circle":
            area = math.pi * measurements['radius'] ** 2
            
        elif shape == "rectangle":
            area = measurements['length'] * measurements['width']
            
        elif shape == "triangle":
            area = 0.5 * measurements['base'] * measurements['height']
            
        elif shape == "square":
            area = measurements['side'] ** 2
            
        elif shape == "pentagon":
            area = (0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) 
                   * measurements['side'] ** 2)
            
        elif shape == "ellipse":
            area = math.pi * measurements['major radius'] * measurements['minor radius']
        
        print(f"\nThe area of the {shape} is: {area:.2f} square units")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    calculate_area()

