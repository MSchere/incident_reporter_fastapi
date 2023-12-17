from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from auth.queries.get_jwt.get_jwt_controller import router as get_jwt_router
from auth.queries.greet_user.greet_user_controller import router as greet_user_router

from incidents.queries.get_incident.get_incident_controller import router as get_incident_router
from incidents.queries.get_incidents.get_incidents_controller import router as get_incidents_router
from incidents.commands.create_incident.create_incident_controller import router as create_incident_router
from incidents.commands.update_incident.update_incident_controller import router as update_incident_router
from incidents.commands.delete_incident.delete_incident_controller import router as delete_incident_router

app = FastAPI()
app.include_router(get_jwt_router)
app.include_router(greet_user_router)
app.include_router(get_incident_router)
app.include_router(get_incidents_router)
app.include_router(create_incident_router)
app.include_router(update_incident_router)
app.include_router(delete_incident_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def health_check():
    return JSONResponse({"status": "Hello from FastAPI!"})
