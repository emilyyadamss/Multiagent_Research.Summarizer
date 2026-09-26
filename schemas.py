from pydantic import BaseModel 

class ResearchOutput( BaseModel ) : 
    query: str 
    key_findings : list[str] 
    sources: list[str] 
    notes: str 

class SummaryOutput( BaseModel ) : 
    final_summary: str
    bullet_points: list[str] 
    recommended_next_step: str 
