# Instagram Follow Request Canceller

This is a simple python program that uses the BeautifulSoup and Selenium libraries to parse the accounts of an Instagram user's pending follow requests and cancels them automatically.

In a recent update, Instagram removed the user's ability to see their pending follow requests from the website or the mobile app. Rather, they allow the user to download all their data, which includes these requests. _Instagram Follow Request Canceller_ uses the html file that contains this information, namely pending_follow_requests.html, to automate the cancellation of these requests.

The program uses the Selenium webdriver as I was unable to find a method to gather a user's Instagram ID from their account link. If I was able to find such method, then simple API requests could make this a lot easier.

If there is a way to convert an Instagram account's account link to their Instagram ID, please let me know so I can update the program.

**Important note**: the program only works if you **don't** have two factor authentication enabled.

## Usage

This program used to be a cli-application. Now, using tkinter, it is a GUI program so the instructions are much easier to follow:

0. From the [Releases](releases) page, download InstagramPendingFollowRequestCanceller.exe
1. Enter your username and password
2. Click on the 'Pending Requests File' button and select your "pending_follow_requests.html" file.
3. Click 'Get Rid Of Pending Requests!' and wait for the procedure to end (a chrome tab will open and automatically log in to your account and cancel all your pending follow requests).
4. Enjoy an account free of pending follow requests!

Note that step 3 can take quite a long time depending on the number of follow requests you have.