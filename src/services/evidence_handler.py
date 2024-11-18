"""Module for handling evidences"""

import json
from pathlib import Path
from typing import List, Dict, Any

config_path = Path(__file__).parent.parent / "config" / "parsing_configs.json"

with open(config_path, "r", encoding="utf-8") as f:
    parsing_configs = json.load(f)


def process_evidence(evidence_id: int, evidence_data: List[Dict]) -> List[Dict]:
    """
    Processes evidence data according to evidence_id
    """

    if str(evidence_id) not in parsing_configs:
        raise ValueError(
            f"No configuration found for evidence_id {evidence_id}"
        )

    config = parsing_configs[str(evidence_id)]
    fields = config["fields"]

    structured_data = []
    for record in evidence_data:
        structured_record = {
            field["target"]: get_nested_value(record, field["source"])
            for field in fields
        }
        structured_data.append(structured_record)

    return structured_data


def get_nested_value(data: Dict[str, Any], path: str) -> Any:
    """
    Returns nested value from dictionary or 
    returns None if not foud
    """
    keys = path.split(".")
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key)
    return data
