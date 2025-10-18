# HNG Stage 0 - profile_api task

# My Project Overview
This is my submission for the Stage 0 Task of the  HNG Internship.  
The project is a simple RESTful API built with Python Django, which returns my personal profile information along with a random cat fact fetched from an external API.

---

## Technologies Used
- Python 3.x  
- Django  
- Requests (for consuming the external API)

# Sample JSON Response:
```json
{
  "status" : "success",
  "user":{
    "email":"<myemail>",
    "name":"<myfullname>",
    "stack":"<mybackendstack",
  },
  "timestamp":"<current UTC time in ISO 8601 format>",
  "fact":"<random fact about cats from facts api>"
}

## Setup Instructions

## 1. Clone the repository
```bash
git clone https://github.com/<Olakitan-01>/HNG-Stage0-my_profile.git
cd HNG-Stage0-my_profile

## install all dependencies 
pip install -r rquirements.txt

## Run locally
After installing, you can then python manage.py runserver