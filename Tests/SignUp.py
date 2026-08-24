from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.nykaa.com/auth/verify?ptype=auth&redirect=%2F%3F" \
"utm_content%3Dads%26utm_source%3DGooglePaid%26utm_medium%3Dsearch%26utm_campaign%3DSearch_Nykaa_NCA%26gad_source%3D1%26gad_campaignid%3D17456562941%26gbraid%3D0AAAAADo9oc9U6B3Bw6KAqju-" \
"KWWSPrQuK%26gclid%3DCj0KCQjw16_UBhCqARIsAIdOaXwIRsI3O2hzlgTdG5AC3QICCpU994NHoXRtOe8qSgCA_" \
"Y2MF5OEsCQaApQ2EALw_wcB")

driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Fill signup form

mobile = driver.find_element(By.XPATH, "//input[@aria-label='Mobile Number']").send_keys("6747957957")
button = driver.find_element(By.CLASS_NAME, 'css-15q5a8e')


if button.is_enabled()==True:
    print('Get OTP Test Case Successfull!')
    button.click()


    otp_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[normalize-space()='OTP Verification']")
        )
    )

    print("TEXT FOUND:", repr(otp_text.text))

    assert "OTP Verification" in otp_text.text
    if otp_text.text!="OTP Verification":
        print(
        "Get OTP Test Case Failed!")

else:
    print('Get OTP Test Case Failed!')


# Close browser
driver.quit()