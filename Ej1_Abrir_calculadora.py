# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='moto g(20)',
    appPackage='com.android.settings',
    appActivity='.homepage.SettingsHomepageActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723/wd/hub'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

