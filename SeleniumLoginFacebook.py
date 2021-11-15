from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

LOGIN_URL = 'https://www.facebook.com/'

class FacebookLogin():
    def __init__(self, email, password):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })
        # Store credentials for login
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=option)
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
 
 
    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too
 
        login_button = self.driver.find_element_by_name('login')
        login_button.click() # Send mouse click
 
        time.sleep(2) # Wait for 2 seconds for the page to show up
        time.sleep(5) # Wait for 2 seconds for the page to show up

       
    def post(self):
        #Class post in facebook
        post= 'a8c37x1j ms05siws hwsy1cff b7h9ocf4 n90h9ftp rgmg9uty b73ngqbp'
        #Format to class_a.class_b
        post_class = post.replace(' ', '.')
        #Get locale button create post
        click_post = self.driver.find_element_by_class_name(post_class)
        #Click button create post
        click_post.click()

        time.sleep(3)

        #Get locale content
        post_content = self.driver.find_element_by_class_name('notranslate._5rpu')
        #Add message to content
        post_content.send_keys('Hello World Python Selenium')

        time.sleep(3)

        #Class button up post
        up_post = 'k4urcfbm discj3wi dati1w0a hv4rvrfc i1fnvgqd j83agx80 rq0escxv bp9cbjyn'
        #Format class to class_a.class_b
        up_post_class = up_post.replace(' ', '.')
        #Get locale button up post
        click_post = self.driver.find_element_by_class_name(up_post_class)
        #Click button up post
        click_post.click()

if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='youremail@gmail.com', password='yourpassword')
    fb_login.login()
    fb_login.post()