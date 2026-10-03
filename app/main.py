from fastapi import FastAPI, HTTPException
from app.models.schemas import InvestigationRequest, InvestigationResult
from app.services.investigation import InvestigationService

app = FastAPI(title="NorthStar Health Prior Authorization Investigation API", version="0.1.0")
service = InvestigationService()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/investigations", response_model=InvestigationResult)
def investigate(request: InvestigationRequest) -> InvestigationResult:
    try:
        return service.investigate(request)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
