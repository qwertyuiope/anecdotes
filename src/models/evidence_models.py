"""Module for evidence models"""

from typing import List, Dict, Any
from pydantic import BaseModel

class EvidencePayload(BaseModel):
    """
    Model for evidence payload
    """
    evidence_id: int | str
    evidence_data: List[Dict[str, Any]]
