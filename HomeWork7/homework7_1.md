Напишите любой user-story и соответствующий тест 
кейс для сайта https://openweathermap.org/

### ***User-story:

As a registered user, I must be able to recover my password to restore access to my personal account.

**Acceptance criteria**:

1. The user navigates to the login page "Sign In To Your Account". The user click the link "Click here to recover".
Enters a valid email to receive a link for password recovery. The system sends the link to the entered email.
2. The user receives the link via the email. The user navigates through the link received in the email. 
The system enables the user to set a new password.
3. The user navigates to the login page "Sign In To Your Account". Enters the valid email and new password, click "Submit". 
The user is authorized success in to the system and logged into the personal account.


### ***Test case 1 (E2E): 

**_Precondition_**:

The user have an account the system.
Navigate to page "Sign In To Your Account" https://home.openweathermap.org/users/sign_in

**_Step 1_**:

Find and verify the link to recover access.

**_Expected results_**:

Visible and expected text **Lost your password?**, and clickable link with expected text **Click here to recover.**.

**_Step 2_**:

Click link **Click here to recover.**

**_Expected results_**:

Display visible and expected text **Enter your email address and we will send you a link to reset your password.**.
Visible input field with placeholder text **Enter email**, clickable button **Send**.

**_Step 3_**:

Enter valid email (the account the system) and click button **Send**

**_Expected results_**:

Display **Notice** with text **You will receive an email with instructions on how to reset your password in a few minutes.**

**_Step 4_**:

Navigate and open the Inbox email (see email from previous step). Open unread new email from sender **crm@openweathermap.org** 
with theme **Reset password instructions**.

**_Expected results_**:

Verify to body email a link to change password with text **Change my password**.

**_Step 5_**:

Click link **Change my password**

**_Expected results_**:

Open page "Change your password". Visible input fields with placeholder text **Password** and **Repeat password**, 
clickable button **Change my password**.

**_Step 6_**:

Enter a valid new password in field **Password** and the same password in field **Repeat password**. 
Click button **Change my password**.

**_Expected results_**:

Verify display **Notice** with text **Your password has been changed successfully.**
Open page "Sign In To Your Account" https://home.openweathermap.org/users/sign_in

**_Step 7_**:

Enter email in input field with placeholder **Enter email**, enter a valid new password in input field **Password**. 
Click button **Submit**.

**_Expected results_**:

Verify display **Notice** with text **Signed in successfully.**
Verify display in navigation bar a name registered user.  
