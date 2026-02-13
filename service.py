import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(requirement: str):

    prompt = f"""
    You are a senior QA engineer.
    Generate detailed manual test cases for the following requirement.

    Requirement:
    {requirement}

    Format output as JSON array with:
    - title
    - steps
    - expected_result
    - priority
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert QA engineer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
