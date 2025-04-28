# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.spatial import Voronoi, voronoi_plot_2d
#
# # مختصات صندوق‌ها (ورودی)
# points = np.array([[1, 1], [2, 4], [5, 2], [3, 3], [6, 5]])
#
# # محاسبه نواحی Voronoi
# vor = Voronoi(points)
#
# # رسم نواحی Voronoi
# fig, ax = plt.subplots()
# voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2)
#
# # رسم نقطه‌های صندوق‌ها
# ax.plot(points[:, 0], points[:, 1], 'bo', markersize=8, label='صندوق‌ها')
# for i, point in enumerate(points):
#     ax.text(point[0], point[1], f' صندوق {i+1}', fontsize=12, ha='right')
#
# # تنظیمات گراف
# ax.set_title("نواحی Voronoi")
# ax.set_xlabel("محور X")
# ax.set_ylabel("محور Y")
# ax.legend()
# plt.grid()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.cluster import KMeans

# تولید نقاط تصادفی
np.random.seed(0)
n_points = 100  # تعداد نقاط بسیار زیاد
points = np.random.rand(n_points, 2) * 10  # نقاط در محدوده 0 تا 10

# خوشه‌بندی نقاط با K-means
n_clusters = 10  # تعداد خوشه‌ها
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(points)
cluster_centers = kmeans.cluster_centers_

# محاسبه نواحی Voronoi با مراکز خوشه‌ها
vor = Voronoi(cluster_centers)

# رسم نواحی Voronoi
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2)

# رسم نقاط خوشه‌ها
ax.plot(cluster_centers[:, 0], cluster_centers[:, 1], 'bo', markersize=8, label='مراکز خوشه‌ها')
for i, center in enumerate(cluster_centers):
    ax.text(center[0], center[1], f' خوشه {i+1}', fontsize=12, ha='right')

# تنظیمات گراف
ax.set_title("نواحی Voronoi با خوشه‌بندی")
ax.set_xlabel("محور X")
ax.set_ylabel("محور Y")
ax.legend()
plt.grid()
plt.show()