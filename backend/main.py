from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Nexus-3 Backend", description="Deep Reasoning & Global Crisis Orchestration Engine")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Nexus-3 Command Center Operational", "status": "active"}

@app.get("/api/status")
def get_system_status():
    return {
        "deep_reasoning": "standby",
        "simulation_core": "ready",
        "active_crises": 0
    }
