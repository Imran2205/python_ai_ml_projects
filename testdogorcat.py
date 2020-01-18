import cv2
import tensorflow as tf
import matplotlib.pyplot as plt

cat = ["dog", "cat"]

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction = 0.5)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))

def prep(path):
    img_size = 50
    img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(img_array)

    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)

model = tf.keras.models.load_model("dog-cat_trained.model")


prediction = model.predict([prep('bbbb.jpg')])

print(cat[int(prediction[0][0])])
plt.show()