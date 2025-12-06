import base64
import os

# This script converts the profile image to Base64 for embedding in HTML

def convert_image_to_base64(image_path):
    """Convert image file to base64 string"""
    try:
        with open(image_path, 'rb') as image_file:
            # Read the image file
            image_data = image_file.read()
            # Encode to base64
            base64_string = base64.b64encode(image_data).decode('utf-8')
            return base64_string
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_data_uri(image_path, mime_type='image/jpeg'):
    """Create a data URI from image file"""
    base64_string = convert_image_to_base64(image_path)
    if base64_string:
        data_uri = f"data:{mime_type};base64,{base64_string}"
        return data_uri
    return None

if __name__ == "__main__":
    # Look for profile image in images directory
    image_path = os.path.join("images", "profile.jpg")
    
    if os.path.exists(image_path):
        data_uri = create_data_uri(image_path)
        if data_uri:
            print("Successfully converted image to Base64!")
            print("\nData URI (use this in HTML img src):")
            print(data_uri[:100] + "..." if len(data_uri) > 100 else data_uri)
            
            # Save to a file for reference
            with open("image_data_uri.txt", "w", encoding="utf-8") as f:
                f.write(data_uri)
            print("\nFull data URI saved to 'image_data_uri.txt'")
    else:
        print(f"Image file not found at {image_path}")
        print("Please place your profile.jpg in the 'images' folder")
