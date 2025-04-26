import numpy as np

def load_mnist_images(filename):
    with open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        num_images = int.from_bytes(f.read(4), 'big')
        num_rows = int.from_bytes(f.read(4), 'big')
        num_cols = int.from_bytes(f.read(4), 'big')
        images = np.frombuffer(f.read(), dtype=np.uint8)
        images = images.reshape((num_images, num_rows, num_cols))
        return images

def load_mnist_labels(filename):
    with open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        num_labels = int.from_bytes(f.read(4), 'big')
        labels = np.frombuffer(f.read(), dtype=np.uint8)
        return labels
    
def display_image(image, label):
    import matplotlib.pyplot as plt
    plt.imshow(image, cmap='gray')
    plt.title(f'Label: {label}')
    plt.axis('off')
    plt.show()
# Example usage
if __name__ == "__main__":
    # Load MNIST dataset
    images = load_mnist_images('data/train-images.idx3-ubyte')
    labels = load_mnist_labels('data/train-labels.idx1-ubyte')

    # Display the first image and its label
    display_image(images[0], labels[0])