import logging
from math import pi
import random
import pickle
import os

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    BMI: float = Field(..., example=3.14)
    HIV_AIDS: float = Field(..., example=3.14)
    School: float = Field(..., example=3.14)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('BMI')
    def bmi_must_be_positive(cls, value):
        """Validate that BMI is a positive number."""
        assert value >= 0, f'BMI == {value}, must be >= 0'
        return value

    @validator('HIV_AIDS')
    def hiv_must_be_positive(cls, value):
        """Validate that HIV_AIDS is a positive number."""
        assert value >= 0, f'HIV_AIDS == {value}, must be >= 0'
        return value

    @validator('School')
    def school_must_be_positive(cls, value):
        """Validate that School is a positive number."""
        assert value >= 0, f'School == {value}, must be >= 0'
        return value

@router.post('/life_expectancy_test')
async def predict(item: Item):
    """
    ### Predict Life expectancy using 
    - **BMI - Body Mass Index**, 
    - **Percentage of Deaths per 1000 Live Birth from HIV AIDS**
    - **Number of Years Spent in School**

    ### Request Body
    - `BMI`: positive float
    - `HIV_AIDS`: positive float
    - `School`: positive float

    ### Response
    - `prediction`: Life expectancy number
    """

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'Life.pickle')

    with open(my_file, "rb") as f:
        model = pickle.load(f)

    # getting the inputed value
    Data = item.to_df()

    # Extracting just the data

    bmi = Data['BMI'][0]
    hiv_aids = Data['HIV_AIDS'][0]
    school = Data['School'][0]

    
    life_expectancy = model.predict([[bmi, hiv_aids, school]])

    return {
        'Life Expectancy': round(life_expectancy[0])
        }
    

