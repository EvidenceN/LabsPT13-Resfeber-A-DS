from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px

router = APIRouter()


@router.get('/viz experiment')
async def viz():
    """
    Visualize Life Expectancy Data 📈
    
    ### Path Parameter
    *NOT BEING USED IN THIS VISUALIZATION*
    `statecode`: The [USPS 2 letter abbreviation](https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations#Table) 
    (case insensitive) for any of the 50 states or the District of Columbia.

    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/) 
    """

    # Validate the state code
    #statecodes = {
    #    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 
    #    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 
    #    'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida', 
    #    'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 
    #    'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky', 
    #    'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 
    #    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 
    #    'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 
    #    'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 
    #    'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 
    #    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 
    #    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 
    #    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 
    #    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 
    #    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 
    #    'WI': 'Wisconsin', 'WY': 'Wyoming'
    #}
    #statecode = statecode.upper()
    #if statecode not in statecodes:
    #    raise HTTPException(status_code=404, detail=f'State code {statecode} #not found')
#
    # loading the data

    data = 'https://raw.githubusercontent.com/EvidenceN/Life-Expectancy-Prediction/master/Life%20Expectancy/Data/Life%20Expectancy%20Data.csv'

    life = pd.read_csv(data)

    # Make Plotly figure

    # statename = statecodes[statecode]
    fig = px.scatter(life, x=' HIV/AIDS', y='Life expectancy ', 
           title='Relationship between hiv aids and life expectancy')

    # Return Plotly figure as JSON string
    return fig.to_json()
