# Instagram Follow Request Canceller

This is a simple python program that uses the BeautifulSoup and Selenium libraries to parse the accounts of an Instagram user's pending follow requests and cancels them automatically.

In a recent update, Instagram removed the user's ability to see their pending follow requests from the website or the mobile app. Rather, they allow the user to download all their data, which includes these requests. _Instagram Follow Request Canceller_ uses the html file that contains this information, namely pending_follow_requests.html, to automate the cancellation of these requests.

The program uses the Selenium webdriver as I was unable to find a method to gather a user's Instagram ID from their account link. If I was able to find such method, then simple API requests could make this a lot easier.

If there is a way to convert an Instagram account's account link to their Instagram ID, please let me know so I can update the program.

**Important note**: the program only works if you **don't** have two factor authentication enabled.

## Usage

1. Clone or download this repository
2. Copy the path of the pending_follow_requests.html on your device (typically of the form "C:\ ...")
3. Enter your account's credentials, along with the path you copied in step 2, to their respective fields in [credential.py](credentials.py)
4. Make sure your python installation has BeautifulSoup and Selenium. If you're unsure, you can install them using these commands:

```shell
pip3 install bs4
pip3 install selenium
```

5. Run canceller.py either by using an IDE such as VSCode or directly from the command prompt with the command:

```shell
cd path_to_the_repository_on_your_device
python canceller.py
```

6. Enjoy an account free of pending follow requests

Note that step 5 can take quite a long time depending on the number of follow requests you have.

## Potential problems

Currenly, the program assumes that the login page and any profile page will fully load in a maximum duration of 3 seconds. This can be modified in the [canceller](canceller.py) file if needed.
