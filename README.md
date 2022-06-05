# qa-assignment
step1 : create a test data notepad file in your system ![image](https://user-images.githubusercontent.com/106878275/172048282-3073184f-6761-4885-ab26-7e4b12f8ec90.png)
Now give this path in the test data sheet that is present in the repository ![image](https://user-images.githubusercontent.com/106878275/172048335-9c827f75-d61a-44d5-a5dc-cbfb954b2efe.png)
Now execute the Login_testcase1.py and New_repository.py
Login_testcase1.py will reproduce the steps of Testcase1
New_repository.py will reproduce the step of Testcase 2
###############################################################################################################################################
**Testcase 1**
Open GitHub 

Type email/username into the "Username or email address" field.

Type the password into the password field.

Click on the Sign-in button.

On the top right corner, there is a view profile icon. Click on that icon that should list a bunch of profile related options (Your profile, Your repositories, Sign out etc.).

Verify that the right username/email address is displayed on the text "Signed in as <username/email address>".

Click on the Sign-out button.

**Testcase 2**
Open GitHub 

Type email/username into the "Username or email address" field.

Type the password into the password field.

Click on the sign-in button.

On the left-hand pane, click on the New button to create a new repository.

Create a new repository with the following inputs -

Repository name - qa-assignment

Check Public

Check Add .gitignore and select “Node” from the options

Click on the “Create repository” button.

Validate the name of the repo and if the .gitignore file is present.

Click on Sign out.
