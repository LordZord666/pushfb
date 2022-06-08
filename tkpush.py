import facebook
from dbConnection import getData
import schedule
import time

page_access_token = "EAAF219B1ahEBAEPKtkgJVpnOBNVajj63uoi7kazXZBNBVHfuYVrd6J2CPpj3PGaWgq1SVe5ZCqDZB5EqW4sJGDMfFY4tberZAMy2rkSRppTgcMSMOseUF9zZBWeES7tXHT8d1SPwVO8K2JpZAzXDETnXXUTywPjfjUw0wsKz6xKGlkYqKqewri"
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = "113544291367455"

def job():
  print("Posting started")
  datas = getData()
  message = ''
  for data in datas:
    message += str(data[0])+" "+str(data[1])+" "+str(data[2])+" "+str(data[3])+'\n'  
  graph.put_object(facebook_page_id, "feed", message=message)
  print("Posting completed")

schedule.every(5).seconds.do(job)
while True:
  schedule.run_pending()
  time.sleep(1)
