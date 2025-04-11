
import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

img_path = "../output_videos/cropped_image.jpg"
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)

top_half_img = img[0: int(img.shape[0] / 2), :]
plt.imshow(top_half_img)

# unsupervised learning algorithm to separate 2 colors the background and the player (shirt)
img_2d = top_half_img.reshape(-1, 3)

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(img_2d)

labels = kmeans.labels_
len(labels)

clustered_img = labels.reshape(top_half_img.shape[0], top_half_img.shape[1])
clustered_img.shape
plt.imshow(clustered_img)

corner_clusters = [clustered_img[0,0], clustered_img[0, -1], clustered_img[-1,0], clustered_img[-1,-1]]
non_player_cluster = max(set(corner_clusters), key=corner_clusters.count())

player_cluster = 1 - non_player_cluster
print(player_cluster)

kmeans.cluster_centers_[player_cluster] 
