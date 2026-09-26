import json 
from agents import researchAgent, summarizerAgent 

def run_system( user_query: str ) -> dict : 
    research_output = researchAgent( user_query ) 
    if not research_output.get( "key_findings" ) :
        raise ValueError( "Research output is missing key_findings" ) 
    summary_output = summarizerAgent( research_output ) 
    if not summary_output.get( "final_summary" ) :
            raise ValueError( "Summary output is missing final_summary" ) 

    return { 
        "research_output" : research_output , 
        "summary_output" : summary_output
    }

def main() :
    result = run_system( "How can AI agents improve customer support?" )
    print("== Research Agent Output ==") 
    print( result["research_output"] ) 

    print("== Summarizer Agent Output ==") 
    print( result["summary_output"] ) 

if __name__ == "__main__" :
    main()
