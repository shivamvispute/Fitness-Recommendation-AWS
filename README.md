# AWS Machine Learning Powered Fitness Recommendation Web App

This project is a full-stack **Machine Learning Recommendation System** deployed live using AWS services.  
The system recommends personalized fitness activities to users based on past behavior.

## 🔥 Technologies Used

- **AWS Elastic Beanstalk** — for cloud hosting and deployment
- **AWS Personalize** — machine learning recommendation engine
- **Flask (Python)** — lightweight backend web framework
- **HTML5 + CSS3** — basic frontend user interface
- **Amazon S3** — storage for dataset uploads
- **IAM Roles** — secure API permission management
- **GitHub** — version control and collaboration


## 🚀 How It Works

1. **User** enters a `USER_ID` into the web form.
2. Flask app sends a live request to **AWS Personalize Campaign**.
3. Amazon Personalize returns **top 5 recommended fitness activities**.
4. Flask app displays the results neatly on the web page.
5. App is deployed and hosted globally using **AWS Elastic Beanstalk**.

## 🌎 Live Demo

**Fitness-recommendation-app-env-1.eba-3s8tztjm.us-east-1.elasticbeanstalk.com**

