import cv2
import numpy as np
import os

def ensure_input_image_exists():
    """Generates a fallback image if input_image.jpg is missing."""
    filename = "input_image.jpg"
    if not os.path.exists(filename):
        print(f"Creating a placeholder test image as '{filename}'...")
        # Create a clean 800x800 high-res colored block as a base target canvas
        placeholder = np.zeros((800, 800, 3), dtype=np.uint8)
        cv2.rectangle(placeholder, (50, 50), (750, 750), (0, 165, 255), -1) # Orange block
        cv2.circle(placeholder, (400, 400), 200, (255, 255, 255), -1)       # White core circle
        cv2.putText(placeholder, "Original High-Res", (180, 420), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 4)
        cv2.imwrite(filename, placeholder)

def main():
    # Make sure we have an asset image to work with safely
    ensure_input_image_exists()

    # 1. Load Image Feature: Read target file asset using OpenCV
    input_filename = "input_image.jpg"
    img = cv2.imread(input_filename)
    
    if img is None:
        print(f"Error: Unable to load or decode image from '{input_filename}'")
        return
    print("✓ Successfully loaded the base source image asset layer.")

    # 2. Resize Image Feature: Define the dimensions from your instruction sheets
    # Format rules specify width x height parameters inside a tuple structure
    sizes = {
        "small": (200, 200),
        "medium": (400, 400),
        "large": (600, 600)
    }

    resized_images = {}

    print("\n--- Processing Array Scale Operations ---")
    for key, dim in sizes.items():
        # cv2.resize handles matrix pixel interpolation calculations automatically
        resized_images[key] = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)
        print(f"✓ Resized image matrix to {key.upper()} size: {dim}x{dim} pixels")

    # 4. Save Resized Images Feature: Output file elements to storage layout path
    print("\n--- Writing Output Image Files to Disk ---")
    cv2.imwrite("input_image_small.jpg", resized_images["small"])
    cv2.imwrite("input_image_medium.jpg", resized_images["medium"])
    cv2.imwrite("input_image_large.jpg", resized_images["large"])
    print("✓ Successfully wrote 'input_image_small.jpg'")
    print("✓ Successfully wrote 'input_image_medium.jpg'")
    print("✓ Successfully wrote 'input_image_large.jpg'")

    # 3. Display Resized Images Feature: Project frames into discrete screen windows
    print("\nDisplaying window framework panels... Press ANY key on your keyboard to exit.")
    cv2.imshow("Small Size - 200x200", resized_images["small"])
    cv2.imshow("Medium Size - 400x400", resized_images["medium"])
    cv2.imshow("Large Size - 600x600", resized_images["large"])

    # 5. Exit Feature: Clear resources safely after a keyboard interaction block
    cv2.waitKey(0) # Waits indefinitely until a keyboard key is touched
    cv2.destroyAllWindows()
    print("✓ Closed all visual windows safely. Application execution complete! 🎉")

if __name__ == "__main__":
    main()