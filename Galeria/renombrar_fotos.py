import os
import random
import glob

def rename_images():
    # Obtiene la ruta de la carpeta actual
    current_folder = os.getcwd()
    
    # Busca todos los archivos de imagen en la carpeta
    image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff')
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(current_folder, ext)))
    
    # Mezcla aleatoriamente la lista de imágenes
    random.shuffle(image_files)
    index = 0
    # Renombra las imágenes con el formato FOTO_1, FOTO_2, etc.
    for index, image_path in enumerate(image_files, start=1):
        folder, original_name = os.path.split(image_path)
        ext = os.path.splitext(original_name)[1]
        new_name = f"FOTO_{index}{ext}"
        new_path = os.path.join(folder, new_name)
        
        try:
            os.rename(image_path, new_path)
            print(f"Renombrado: {original_name} -> {new_name}")
        except Exception as e:
            print(f"Error renombrando {original_name}: {e}")

if __name__ == "__main__":
    rename_images()