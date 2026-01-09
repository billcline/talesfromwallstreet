import os
from PIL import Image

def process_images():
    source_path = os.path.join('images', 'cover.jpg')
    if not os.path.exists(source_path):
        print(f"Error: {source_path} not found.")
        return

    try:
        with Image.open(source_path) as img:
            # Convert to RGB if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')

            widths = [320, 640, 1200]
            
            for width in widths:
                aspect_ratio = img.height / img.width
                height = int(width * aspect_ratio)
                
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Save as JPG with optimization
                jpg_output = os.path.join('images', f'cover-{width}.jpg')
                # Lower quality to 75 and enable optimize flag
                resized_img.save(jpg_output, 'JPEG', quality=75, optimize=True)
                print(f"Generated: {jpg_output}")
                
                # Save as WebP with optimization
                webp_output = os.path.join('images', f'cover-{width}.webp')
                # Lower quality to 75
                resized_img.save(webp_output, 'WEBP', quality=75)
                print(f"Generated: {webp_output}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_images()
