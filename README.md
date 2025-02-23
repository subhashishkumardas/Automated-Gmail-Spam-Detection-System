# Automated-Gmail-Spam-Detection-System
   The Automated Gmail Spam Detection System is a standalone application that allows users to connect to their Gmail accounts, automatically detect spam emails, and log their details for review. The software work on Gmail API and check spam mail on a widely used spam dataset to classify emails based on their content.
# Project Description 
The Automated Gmail Spam Detection System is a standalone application that allows users to connect to their Gmail accounts, automatically detect spam emails, and log their details for review. The software work on Gmail API and check spam mail on a widely used spam dataset to classify emails based on their content. Through a graphical user interface (GUI), users can initiate the spam-checking process and view real-time feedback on the application’s progress.
# Features: 
• User Authentication: The system uses Google’s OAuth 2.0 authentication, ensuring secure access to the user’s Gmail account.                        
• Spam Classification: By using Gmail API it read mails and a system trained on labelled email data classifies emails as spam or legitimate messages.                                                           
• User Interface: The GUI, built with Tkinter, allows users to enter their email address, start spam checks, and view the process status.                                 
• Logging: Details of each spam email are saved to a log file (log.txt), enabling users to review spam emails without interacting with them directly in their inbox.
# Project Structure: 
• Graphical User Interface (GUI) Module: Handles user input and feedback, allowing users to interact with the software and view progress.                                        
• Email Fetching and Processing Module: Uses the Gmail API to securely connect to the inbox, fetch emails, and extract relevant details.                   
• Spam Detection Module: A Naive Bayes classifier trained on spam data (spam.csv) analyses email content and predicts whether each email is spam or legitimate.                  
• Logging Module: Stores details of detected spam emails, including sender, subject, and a message snippet, in log.txt.
# Screenshots
![Screenshot 2024-11-06 145858](https://github.com/user-attachments/assets/82ba498e-dd3e-4559-b047-c4c8dbc6488e)
![si](https://github.com/user-attachments/assets/c2f3fff3-f592-4640-a7d2-8030d022c161)
![so](https://github.com/user-attachments/assets/4061e1e5-9280-4cf5-8a03-a780a21e574d)
