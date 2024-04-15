from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "platformVersion": "9",
  "deviceName": "laurel_sprout",
  "automationName": "UiAutomator2",
  "appPackage": "com.google.android.calculator",
  "appActivity": "com.android.calculator2.Calculator"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
#suma de dos numeros
driver.find_element_by_id("com.google.android.calculator:id/arrow").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_7").click()
driver.find_element_by_id("com.google.android.calculator:id/op_add").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_9").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()
