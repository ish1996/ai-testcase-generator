from fastapi import FastAPI
from pydantic import BaseModel
from service import generate_test_cases

app = FastAPI()

class RequirementRequest(BaseModel):
    requirement: str

@app.post("/generate-testcases")
def generate(req: RequirementRequest):
    result = generate_test_cases(req.requirement)
    return {"test_cases": result}
