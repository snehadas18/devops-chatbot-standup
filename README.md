# devops-chatbot-standup

A simple Python chatbot that collects daily stand-up reports from team members and saves them with timestamps.

## Features
- Asks 3 key stand-up questions
- Handles multiple users
- Saves responses to a text file
- Easy to run and customize

## How to Use
1. Run with Docker
docker build -t devops-chatbot-standup .
docker run -p 5000:5000 devops-chatbot-standup
2. Follow the link
3. Answer the questions
4. Check standup_report.txt for saved summaries
