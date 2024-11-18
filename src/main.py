"""Main module of Fast API for parsing evidences"""

from fastapi import FastAPI, APIRouter, HTTPException
from models.evidence_models import EvidencePayload
from services.evidence_handler import process_evidence
app = FastAPI()

router = APIRouter()

#if API gets to big make dedicated routes/controllers folder
@router.post("/process-evidence/")
async def process_evidence_endpoint(payload: EvidencePayload):
    """
    Processes evidence data
    """
    try:
        result = process_evidence(payload.evidence_id, payload.evidence_data)
        return {"structured_data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
