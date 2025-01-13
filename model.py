import face_recognition
import preprocess as pre


def compare_faces(file1, file2):

    known_image = pre.preprocess(file1, 200)
    unknown_image = pre.preprocess(file2, 200)
    
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    return results[0]
    

"""im1 = "visages/obama.jpeg"
im2 = "visages/Barack-Obama.jpeg"
im3 = "visages/macron.jpg"

image1 = pre.preprocess(im1, 200)
image2 = pre.preprocess(im2, 200)



print(compare_faces(im1, im2))"""
