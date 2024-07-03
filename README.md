Hello, this is an automation project for **"automationexercise.com"**. The project is made of **Python**, **Selenium** and **Pytest**. It is maintaied with **Page Object
Model** structure. The automation project consists the following steps.

1. Launch browser(Chrome/Firefox)
2. Navigate to URL 'http://automationexercise.com'
3. Verify that the home page is visible successfully
4. Add products to the cart
5. Click the 'Cart' button
6. Verify that the cart page is displayed
7. Click Proceed To Checkout
8. Click the 'Register / Login' button
9. Fill all details in Sign up and create an account
10. Verify 'ACCOUNT CREATED!' and click the 'Continue' button
11. Verify ' Logged in as username' at top
12. Click the 'Cart' button
13. Click the 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter the description in a comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click the 'Pay and Confirm Order' button
18. Verify the success message 'Your order has been placed successfully!'

**To run the project follow the steps below:**
1. Download or clone the project
2. Open the project using Pycharm(Preferable) or VS Code
3. Change Directory > **cd kinetikenv\Scripts\***
4. Activate Virtual Environment > **activate.bat**
5. Back to Homepage > **cd ..** (2 times)
6. Install Required Packages > **pip install -r requirements.txt**
7. Run Pytest Command to automate > **pytest tests\test_assessment.py -v -s**
8. 6 Cases will be passed
9. *If any failure occurs (due to internet or something else) **run command 7 again.***

Thank you.
