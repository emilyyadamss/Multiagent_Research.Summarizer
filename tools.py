def mock_search( query: str ) :
    database = {
        "customer support": [
            "AI agents can reduce support response times.",
            "AI agents provide 24/7 coverage.",
            "AI agents can lower customer service costs."
        ],
        "sales": [
            "AI agents can qualify leads.",
            "AI agents can automate follow-ups.",
            "AI agents can improve CRM productivity."
        ], 
        "operations" : [ 
            "AI automation can reduce manual data entry errors.", 
            "AI automation can speed up invoice and order processing.", 
            "AI automation frees staff for higher-value work."
        ]
    }
 
    for key in database :
        if key in query.lower() :
            return database[key]
 
    return [ "No strong results found." ]