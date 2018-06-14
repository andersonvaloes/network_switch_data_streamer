import cv2

class Obj_data_giver:

    cap = cv2.VideoCapture("video.mp4")
    ret = None
    frame = None
    frame_counter = 0

    def __init__(self):
        pass
    
    def give_text(self):
        self.ret, self.frame = self.cap.read()
        self.frame_counter += 1
        return "text num {}".format(self.frame_counter)
    
    def give_image(self):
        f = 0.4
        count_skipped_images = 0
        # print(self.cap.get(cv2.CAP_PROP_FRAME_COUNT), "   ", self.frame_counter)
        while(count_skipped_images < 50):
            self.ret, self.frame = self.cap.read()
            self.frame_counter += 1
            if(self.frame_counter == self.cap.get(cv2.CAP_PROP_FRAME_COUNT)):
                self.frame_counter = 0
                self.cap.set(cv2.CV_CAP_PROP_POS_FRAMES, 0)
                count_skipped_images+=1
            # time.sleep(3)
            count_skipped_images += 1
        return cv2.resize(self.frame, (0,0), fx=f, fy=f)

        
    def give_video(self):
        f = 0.4
        self.ret, self.frame = self.cap.read()
        self.frame_counter += 1
        if(self.frame_counter == self.cap.get(cv2.CAP_PROP_FRAME_COUNT)):
            self.frame_counter = 0
            self.cap.set(cv2.CV_CAP_PROP_POS_FRAMES, 0)
        return cv2.resize(self.frame, (0,0), fx=f, fy=f)

    def get_data_function_giver(self):
        list_of_function = [self.give_text, self.give_image, self.give_video]
        return list_of_function