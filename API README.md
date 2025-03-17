# 🌍 Flask Weather API

This project is a **Flask-based Weather API** that fetches real-time weather data using the **OpenWeather API**. Firstly read the Questions zip file to understand below  mentioned tasks.

It includes:

- **Task 1**: Basic Flask API with weather data.  
- **Task 2**: Error handling for invalid city names.  
- **Task 3**: Fetching weather for multiple cities.  
- **Task 4**: Deployment using Ngrok.
- **Question 1 client/server**: A server fetches real-time weather data (temperature, humidity, pressure) from a third-party API and evaluates crop health based on predefined optimal conditions,whereas client sends requests to the server with a city and crop type to receive the health status of the crop in that city.
- **Agriculture**: This task involves designing and implementing a Flask-based RESTful API to help farmers manage their agricultural needs efficiently. The API will provide multiple services, including crop advisory, bank loan approval, seed and fertilizer procurement, and transport logistics.
- Both **Question 1 client/server** and **Agriculture** are in zip files. Separate zip files for code and output screenshots with a detailed word document explaining things and flowchart.

---

## Features**
- Get weather details (**temperature, humidity, wind speed, pressure**).
- Support for **multiple cities** (comma-separated).
- Handles **invalid city names** with a custom error message.
- Deployable online using **Ngrok**.
  
- Server Functions: Fetches weather data (temperature, humidity, pressure) via an API. Defines optimal conditions for crops (wheat, corn, rice, cotton). Compares real-time weather with optimal values and determines: **Optimal** or **Not Optimal** for each parameter. **Healthy** or **Unhealthy** crop status.

- Client Functions: Sends city and crop type as input to the server. Receives and displays: Weather data, parameter statuses, and overall crop health.

- Agriculture Service Platform API:

- Crop Advisory Service: Determines suitability of weather for a given crop type.
  
- Bank Loan Approval: Calculates trust factor based on loan history. Approves or rejects loan requests.

- Seed Procurement: Orders seeds from different suppliers based on ratings.

- Fertilizer Procurement: Validates fertilizer supplier authenticity before approving requests.

-  Transport Logistics: Arranges transportation for seed and fertilizer delivery.

- Integrated Smart Agriculture Service: Single request processes all services together and returns a combined decision.

---

