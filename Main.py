import cv2
import numpy as np


img = cv2.imread(".\data\hoodies\\2NA22S0A9-K12@1.1.jpg")

image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
twoDimage = image.reshape((-1,3))
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
attempts=10

ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((image.shape))



cv2.imshow("img",img)
cv2.imshow("image",image)
cv2.imshow("result_image",result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
