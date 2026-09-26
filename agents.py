import json 
import anthropic 
from schemas import ResearchOutput, SummaryOutput
from tools import mock_search
from prompts import RESEARCH_AGENT_PROMPT, SUMMARIZER_AGENT_PROMPT

client = anthropic.Anthropic() # reads API key 
MODEL = "claude-sonnet-5" 

def researchAgent( userQuery: str ) -> dict : 
    searchResults = mock_search( userQuery ) 
    response = client.messages.parse( 
        model=MODEL , 
        max_tokens=16000 , 
        system=RESEARCH_AGENT_PROMPT , 
        messages=[{ 
            "role": "user" , 
            "content": f"User query: { userQuery }\n\nSearch Results:\n{ json.dumps( searchResults, indent=2 ) }", 
        }] , 
        output_format=ResearchOutput , 
    ) 
    return response.parsed_output.model_dump() 

def summarizerAgent( research_output: dict ) -> dict : 
    response = client.messages.parse( 
        model=MODEL , 
        max_tokens=16000 , 
        system=SUMMARIZER_AGENT_PROMPT , 
        messages=[{ 
            "role": "user" , 
            "content": f"Research findings:\n{ json.dumps( research_output, indent=2 ) }" , 
        }] , 
        output_format=SummaryOutput , 
    ) 
    return response.parsed_output.model_dump() 
    
