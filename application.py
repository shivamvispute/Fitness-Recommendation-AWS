from flask import Flask, request, render_template
import boto3
import json

app = Flask(__name__)

personalize_runtime = boto3.client('personalize-runtime', region_name='us-east-1')
campaign_arn = 'arn:aws:personalize:us-east-1:260461238631:campaign/fitness-recommendation-campaign'

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        user_id = request.form['user_id']
        try:
            response = personalize_runtime.get_recommendations(
                campaignArn=campaign_arn,
                userId=user_id,
                numResults=5
            )
            for item in response['itemList']:
                recommendations.append(item['itemId'])
        except Exception as e:
            recommendations.append(f"Error: {str(e)}")

    return render_template('index.html', recommendations=recommendations)

application = app

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port)