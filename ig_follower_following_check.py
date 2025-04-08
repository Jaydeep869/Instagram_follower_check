from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Starting the Instagram follower checker...")
chrome_driver_path = "/usr/bin/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

print("Opening Instagram...")
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

print("Logging in to Instagram...")
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

username_input.send_keys('-------')#enter your username here
password_input.send_keys('-------')#enter your password here

login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

print("Waiting for login to complete...")
time.sleep(5)

print("Going to your profile page...")
driver.get('https://www.instagram.com/-------')#enter your username here to check your profile
time.sleep(5)

print("Looking for your follower and following numbers...")

try:
    all_elements = driver.find_elements(By.TAG_NAME, "span")
    
    follower_count = 1000
    following_count = 1000
    
    for element in all_elements:
        try:
            text = element.text.lower()
            if "follower" in text and not "following" in text:
                number = text.split()[0]
                if number.replace('k', '').replace('m', '').replace('.', '').isdigit():
                    follower_count = int(float(number.replace('k', '')) * 1000 if 'k' in number 
                                     else float(number.replace('m', '')) * 1000000 if 'm' in number 
                                     else number)
                    print(f"Found follower count: {follower_count}")
            
            elif "following" in text:
                number = text.split()[0]
                if number.replace('k', '').replace('m', '').replace('.', '').isdigit():
                    following_count = int(float(number.replace('k', '')) * 1000 if 'k' in number 
                                      else float(number.replace('m', '')) * 1000000 if 'm' in number 
                                      else number)
                    print(f"Found following count: {following_count}")
        except:
            continue
    
    print(f"Your account has {follower_count} followers and is following {following_count} accounts")
    
except Exception as e:
    print(f"Couldn't find exact counts, using default values: 41 followers, 101 following")
    follower_count = 41
    following_count = 101

def get_list_of_users(list_type, expected_count):
    print(f"\nGetting your {list_type} list...")
    
    try:
        print(f"Clicking on {list_type} link...")
        
        elements_with_text = driver.find_elements(By.XPATH, f"//*[contains(text(), '{list_type}')]")
        clicked = False
        
        for element in elements_with_text:
            try:
                element.click()
                clicked = True
                print(f"Clicked on {list_type} link!")
                break
            except:
                continue
        
        if not clicked:
            profile_stats = driver.find_elements(By.CSS_SELECTOR, "section ul li")
            if list_type == "followers" and len(profile_stats) >= 2:
                profile_stats[1].click()
                clicked = True
            elif list_type == "following" and len(profile_stats) >= 3:
                profile_stats[2].click()
                clicked = True
        
        if not clicked:
            print(f"Couldn't click on {list_type} link. Please try clicking it manually.")
            input("Press Enter once you've clicked the link and the popup is open...")
    
    except Exception as e:
        print(f"Error clicking {list_type} link: {e}")
        print("Please try clicking it manually.")
        input("Press Enter once you've clicked the link and the popup is open...")
    
    time.sleep(2)
    try:
        dialog = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
        )
        print(f"Popup dialog for {list_type} is open!")
    except:
        print("Couldn't find the popup dialog. Please make sure it's open.")
        dialog = driver.find_element(By.XPATH, "//div[@role='dialog']")
    
    print(f"Scrolling to load all {list_type}...")
    
    last_count = 0
    last_update_time = time.time()
    
    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 500", dialog)
        time.sleep(1)
        
        users = dialog.find_elements(By.XPATH, ".//a[@role='link']")
        current_count = 0
        for user in users:
            if user.text:
                current_count = current_count + 1
        
        if current_count >= expected_count:
            print(f"Found all {expected_count} {list_type}!")
            break
        
        if current_count > last_count:
            last_count = current_count
            last_update_time = time.time()
            print(f"Found {current_count} out of {expected_count} {list_type} so far...")
        
        elif time.time() - last_update_time > 15:
            print(f"No new {list_type} loaded for 15 seconds. Stopping at {current_count}/{expected_count}.")
            break
    
    users = dialog.find_elements(By.XPATH, ".//a[@role='link']")
    
    usernames = []
    for user in users:
        if user.text:
            usernames.append(user.text)
    
    try:
        close_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, '_abl-')] | //button[@aria-label='Close']")
        if close_buttons:
            close_buttons[0].click()
        else:
            from selenium.webdriver.common.keys import Keys
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        print(f"Couldn't close the {list_type} popup. Please close it manually.")
        input("Press Enter once you've closed the popup...")
    
    time.sleep(2)
    
    return usernames

followers_list = get_list_of_users("followers", follower_count)
print(f"\nYou have {len(followers_list)} followers:")
for username in followers_list:
    print(username)

following_list = get_list_of_users("following", following_count)
print(f"\nYou are following {len(following_list)} accounts:")
for username in following_list:
    print(username)

print("\nFinding accounts that don't follow you back...")
not_following_back = []
for user in following_list:
    if user not in followers_list:
        not_following_back.append(user)

print(f"\nAccounts that don't follow you back ({len(not_following_back)}):")
for username in not_following_back:
    print(username)

print("\nDone! Closing the browser...")
driver.quit()

print("Instagram follower checker complete!")