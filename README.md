# Project Shortify

An URL shortener application built with **FastAPI** and **Redis** for faster lookups. This project allows users to shorten long URLs into compact, shareable links and redirect them back to the original URLs.

---

## Features

1. **URL Shortening**: 
   - Users can input a long URL, and the application generates a unique short URL.
   - The short URL is stored in Redis for fast retrieval.

2. **Redirection**:
   - When a user accesses the short URL, they are redirected to the original long URL.

3. **Frontend Integration**:
   - A simple and responsive HTML frontend for user interaction.
   - Users can paste a URL, shorten it, and view the generated short URL.

4. **Fast Performance**:
   - Uses Redis as the database for quick lookups and storage.

5. **CORS Support**:
   - Configured to allow cross-origin requests for seamless integration with other services.

---

## Tech Stack

- **Backend**: FastAPI
- **Database**: Redis
- **Frontend**: HTML, TailwindCSS
- **Containerization**: Docker
- **Deployment**: Render

---

## How to Run the Project Locally

### Prerequisites

1. Install **Python 3.9+**.
2. Install **Docker** and **Docker Compose**.
3. Install **Redis** (if not using Docker).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-shortify.git
   cd project-shortify

2. Start the application using docker compose
    docker compose up -d --build

### API Endpoints

1. GET /:
Serves the main HTML page.

2. POST /shorten:
Accepts a long URL and returns a shortened URL.

3. GET /{short_url}:
Redirects to the original long URL based on the short URL.

### Deployment
The project is configured for deployment on Render using the render.yaml file. It includes:

A web service for the FastAPI application.
A Redis service for storing URL mappings.

### Future Enhancements
- Add user authentication for managing URLs.
- Implement analytics to track URL usage.
- Add expiration for short URLs.
- Enhance error handling and validation.