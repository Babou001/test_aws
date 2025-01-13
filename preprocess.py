import cv2

def preprocess(file, image_size):
    # Charger une image
    image = cv2.imread(file)
    
    # Convertir en niveaux de gris
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Redimensionner l'image
    image = cv2.resize(image, (image_size, image_size))
    
    
    # Normalisation à une plage personnalisée
    image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    
    return image