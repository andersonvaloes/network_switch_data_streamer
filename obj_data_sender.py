class Obj_data_giver:

    def __init__(self):
        pass
    
    def give_text(self):
        return "text"
    
    def give_image(self):
        return "image"

    def give_video(self):
        return "video"

    def get_data_function_giver(self, n_function):
        list_of_function = [self.give_text, self.give_image, self.give_video]
        return list_of_function[n_function]



a = Obj_data_giver()
function_given = a.get_data_function_giver(1)
print(function_given())
function_given = a.get_data_function_giver(2)
print(function_given())