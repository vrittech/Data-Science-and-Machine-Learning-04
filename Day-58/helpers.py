import pickle

def get_save_file(file_path:str):
    
    with open(file_path,"rb") as file:
        output = pickle.load(file)
        
    return output