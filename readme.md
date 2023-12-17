# Incident reporter FastAPI

*Report incidents, update them, and close them.*

### Visit live site at [https://incident-reporter-nextjs.vercel.app/](https://incident-reporter-nextjs.vercel.app/)

## Stack

- **Frontend**: Next.js, NextAuth, Tailwind CSS
- **Backend**: FastAPI
- **Database**:  Upstash (Redis)
- **Deployment**: Vercel (frontend), Google App Engine (backend)

## Usage
Place a .env file in the root directory with the following variables:
```
NEXTAUTH_SECRET="YOUR_SECRET"
NEXTAUTH_URL="http://127.0.0.1:3000"
UPSTASH_REDIS_REST_URL="YOUR_UPSTASH_REDIS_REST_URL"
UPSTASH_REDIS_REST_TOKEN="YOUR_UPSTASH_REDIS_REST_TOKEN"
```
Install dependencies
```bash
pip install -r requirements.txt
```
Run the development server:
```bash
uvicorn main:app --reload
```
Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## API Reference
### Create incident
```http
POST /fastapi/incident
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | **Required**. Incident title |
| `description` | `string` | **Required**. Incident description |
### Update incident
```http
PUT /fastapi/incident/${id}
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | **Required**. Incident title |
| `description` | `string` | **Required**. Incident description |
| `status` | `string` | **Required**. Incident status |
### Delete incident
```http
DELETE /fastapi/incident/${id}
```
### Get incident
```http
GET /fastapi/incident/${id}
```
### Get all incidents
```http
GET /fastapi/incidents
```

