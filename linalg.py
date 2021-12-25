import Image
import numpy as np

def main():
    # read image to numpy array
    img = np.array(Image.open("img.png"))

    # transpose image
    transpose_image = img.T

    # check if the matrix is diagonal or triangular
    if np.allclose(img, np.diag(np.diag(img))):
        print("Diagonal")
    if np.allclose(img, np.triu(img)):
        print("Upper Triangular")
    if np.allclose(img, np.tril(img)):
        print("Lower Triangular")

    # compute l1 and l2 norms for first column
    l1 = np.linalg.norm(img[:, 0], 1)
    l2 = np.linalg.norm(img[:, 0], 2)

if __name__ == "__main__":
    main()