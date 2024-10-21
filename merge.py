from PIL import Image
import os

def merge_a5_to_a4(input_folder, output_folder):
    A4_WIDTH, A4_HEIGHT = 2480, 3508
    
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]
    
    image_files.sort()
    
    for i in range(0, len(image_files), 2):
        if i + 1 < len(image_files):
            img1 = Image.open(os.path.join(input_folder, image_files[i]))
            img2 = Image.open(os.path.join(input_folder, image_files[i+1]))
            
            img1 = img1.rotate(-90, expand=True)
            img2 = img2.rotate(-90, expand=True)
            
            a4_img = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
            
            new_width = int(img1.width)
            new_height = int(img1.height)
            img1_resized = img1.resize((new_width, new_height), Image.LANCZOS)
            img2_resized = img2.resize((new_width, new_height), Image.LANCZOS)
            
            a4_img.paste(img1_resized, (0, 6))
            a4_img.paste(img2_resized, (0, new_height + 6))
            
            output_filename = f"sheet-{i//2+1}.jpg"
            a4_img.save(os.path.join(output_folder, output_filename), "JPEG", quality=95)
            print(f"Created {output_filename}")