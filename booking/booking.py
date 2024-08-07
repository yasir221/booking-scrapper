
from types import TracebackType
from typing import Type
import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
# import tensorflow as tf

# # Load your TensorFlow Lite model
# interpreter = tf.lite.Interpreter(model_path="your_model.tflite")

# # Configure XNNPACK delegate
# interpreter.add_delegate(tf.lite.experimental.load_delegate('libtensorflowlite_xnnpack.so'))

# # Allocate tensors
# interpreter.allocate_tensors()

# # Perform inference, etc.



class Booking(webdriver.Chrome):
  def __init__(self, driver_path=r"D:\SeleniumDriver", teardown=False):
      self.driver_path = driver_path
      self.teardown = teardown
      os.environ['PATH'] += self.driver_path

      # Create ChromeOptions instance and add experimental option
      options = webdriver.ChromeOptions()
      options.add_experimental_option('detach', True)

      # Initialize the parent webdriver.Chrome class with the options
      super().__init__(options=options)

      self.implicitly_wait(15)
      self.maximize_window()
    
    
  def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, traceback: TracebackType | None):
    if self.teardown:
      self.quit()
    
    
  def land_first_page(self):
    print(const.BASE_URL)
    self.get(const.BASE_URL)
    
  # def change_currency(self, currency=None):
  #   currency_element= self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
    
  #   currency_element.click()
  
  # selected_currency_element = self.find_elemment(By.CSS_SELECTOR ,f'a[data-model-header-async-url-param*="selected_currency={currency}"]'
  # )
  # selected_currency_element.click()
  def select_place_to_go(self,place_to_go):
    search_field = self.find_element(By.ID, ":rh:")
    search_field.clear()
    search_field.send_keys(place_to_go)
    
    first_result = self.find_element(By.CSS_SELECTOR,
         'div[role="button"][tabindex="-1"]')
    first_result.click()
    
    
  
    