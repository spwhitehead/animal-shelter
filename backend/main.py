# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import Shelter, Animal


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


shelters: list = [
    
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals= Animal(
            cats= 13,
            dogs= 15
        )
    ),
     
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals= Animal(
            cats= 12,
            dogs= 9
        )
    ),

    Shelter(
        name="Sample Shelter D",
        address="134 Banana Street",
        animals= Animal(
            cats= 1,
            dogs= 43
        )
    ),

    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals= Animal(
            cats= 4,
            dogs= 7
        )
    )
]

@app.get("/")
async def get_shelters() -> list:
    return shelters

@app.get("/{shelter_name}/animals")
async def list_animals(shelter_name: str) -> Animal:
    for shelter in shelters:
        if shelter.name == shelter_name:
            return shelter.animals
    raise HTTPException(status_code=404, detail="Shelter not found")
    

@app.post("/")
async def add_shelter(shelter: Shelter):
    shelters.append(shelter)
    return f"{shelter.name} added successfully"

@app.put("/{shelter_name}")
async def update_animals(shelter_name: str, updated_animals: Animal):
    for shelter in shelters:
        if shelter.name == shelter_name:
            shelter.animals = updated_animals
            return "Animal count updated successfully"
    raise HTTPException(status_code=404, detail="Shelter not found")

@app.delete("/{shelter_name}")
async def delete_shelter(shelter_name: str):
    for index, shelter in enumerate(shelters):
        if shelter.name == shelter_name:
            shelters.pop(index)
            return "Shelter deleted successfully"
    raise HTTPException(status_code=404, detail="Shelter not found")