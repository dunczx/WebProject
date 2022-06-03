from fnmatch import fnmatch
from selenium import webdriver
import names

class WebBot_Google:
    def __init__(self):
        self.generate_names()
        
        
    def generate_names(self):
        fname = names.get_first_name(gender='male')
        lname = names.get_last_name()
        
        
        
        
        
        
if __name__ == "__main__":
    WebBot_Google()
        