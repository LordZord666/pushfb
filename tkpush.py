import facebook
import config
import requests
from dbConnection import getData
import schedule
import time
import cv2
#from fbpush.dbConnection import getData

page_access_token = "EAAF219B1ahEBAEPKtkgJVpnOBNVajj63uoi7kazXZBNBVHfuYVrd6J2CPpj3PGaWgq1SVe5ZCqDZB5EqW4sJGDMfFY4tberZAMy2rkSRppTgcMSMOseUF9zZBWeES7tXHT8d1SPwVO8K2JpZAzXDETnXXUTywPjfjUw0wsKz6xKGlkYqKqewri"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "113544291367455"

#post_url = 'https://graph.facebook.com/{}/feed'.format(config.facebook_page_id)
#payload ={
# 'message'=msg,
# 'access_token': config.page_access_token
# }
#r=requests.post(post_url, data=payload)
#print(r.text)  #for viewing id:

def job():
  print("Posting started")
  datas = getData()
  message = ''
  for data in datas:
    message += str(data[0])+" "+str(data[1])+" "+str(data[2])+" "+str(data[3])+'\n'  
  graph.put_object(facebook_page_id, "feed", message=message)
  print("Posting completed")
  
# graph = facebook.GraphAPI(page_access_token)
# photo = open("G:\python\push/fbpush/rice.png", "rb")
# graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
# photo.close()

schedule.every(5).seconds.do(job)
while True:
  schedule.run_pending()
  time.sleep(1)
  
  # image_url = 'https://graph.facebook.com/{}/photos'.format(facebook_page_id)
  # image_location = 'G:\python\push/fbpush/rice.png'
  # image_playload = {
  #   'url': image_location,
  #   'access_token': config.page_access_token
  # }
  # r = requests.post(image_url, data=image_playload) 
  # print(r.text)



# img =  cv2.imread('468206.jpg')
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image",gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
