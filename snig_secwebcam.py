import cv2
import dropbox
import time
import random
start_time=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    video_capture_object=cv2.VideoCapture(0)
    result=True 
    while (result):
        ret,frame=video_capture_object.read()
        image_name="image"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    print("snapshot taken")
    video_capture_object.release()
    cv2.destroyAllWindows()
def upload_files(image_name):
    access_token="sl.ApvTIOFyqy635nT7pQ3fccNzVdZ37Mb33g1HnN-nKkkkV89VrpRgEl4F6Njov18B_K8TxJPD_uAZMYeGGbdophqG7Syd1YVt5js1SeMlB263FQTm_TZf6-UTboipe71X7ZCYZ4s"
    file=image_name
    file_from=file
    file_to="/class101/"+image_name
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
      dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
      print("files uploaded")
def main():
    while (True):
        if((time.time()-start_time>60)):
            name=takeSnapshot()
            upload_files(name)
main()