import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Updated base_url for better compatibility
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/",
)

SYSTEM_PROMPT = """
You are an execution planner.
Break the goal into 5-15 small actionable tasks based on task complexity.
Return the output strictly in JSON format:
{
  "tasks": [
    {"title": "Task 1"},
    {"title": "Task 2"}
  ]
}
"""
SUBTASK_PROMPT = """
You are an expert task decomposer. 
Break the following task into 3-5 distinct, tiny micro-steps (subtasks).
Return the output strictly in JSON format:
{
  "subtasks": [
    {"title": "Step 1"},
    {"title": "Step 2"}
  ]
}
"""


"""
# For Online deployed models
def generate_tasks(goal_text):
    try:
        response = client.chat.completions.create(
            model="gemma-3-12b-it",  # Ensure this matches your enabled models
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": goal_text},
            ],
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        return json.loads(content)["tasks"]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
"""


# For Offline Deployed models which has restrictions: Supports no system and json format
def generate_tasks(goal_text, model_name="Gemma3 12b"):
    # Move instructions into the user prompt since 'system' role is disabled
    prompt = f"{SYSTEM_PROMPT}\n\nGoal: {goal_text}\n\nReturn ONLY the JSON object."

    # Map your readable names to actual API model IDs if necessary
    # Example mapping (adjust based on your actual API provider/Proxy)
    model_map = {
        "Gemini 2.5 Flash": "gemini-2.5-flash",  # Example ID
        "Gemma3 12b": "gemma-3-12b-it",
        "Gemma3 27b": "gemma-3-27b-it",
    }

    effective_model = model_map.get(model_name, "gemma-3-12b-it")
    # For now, we pass it directly assuming your proxy handles it:
    # effective_model = model_name

    try:
        response = client.chat.completions.create(
            model=effective_model,  # <--- USE THE VARIABLE HERE
            messages=[
                # CRITICAL FIX: Only use 'user' role. Do NOT include 'system'.
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        # REMOVE this line: response_format={"type": "json_object"}
        # It causes the 400 error on Gemma 3

        content = response.choices[0].message.content

        # Clean up the response in case the model adds ```json ... ``` blocks
        clean_content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(clean_content)["tasks"]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


def generate_subtasks_llm(task_title, model_name="Gemma3 12b"):
    # Move instructions into the user prompt since 'system' role is disabled
    prompt = f"{SUBTASK_PROMPT}\n\nGoal: {task_title}\n\nReturn ONLY the JSON object."

    # Map your readable names to actual API model IDs if necessary
    # Example mapping (adjust based on your actual API provider/Proxy)
    model_map = {
        "Gemini 2.5 Flash": "gemini-2.5-flash",  # Example ID
        "Gemma3 12b": "gemma-3-12b-it",
        "Gemma3 27b": "gemma-3-27b-it",
    }

    effective_model = model_map.get(model_name, "gemma-3-12b-it")
    # For now, we pass it directly assuming your proxy handles it:
    # effective_model = model_name

    try:
        response = client.chat.completions.create(
            model=effective_model,  # <--- USE THE VARIABLE HERE
            messages=[
                # CRITICAL FIX: Only use 'user' role. Do NOT include 'system'.
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
        )
        # REMOVE this line: response_format={"type": "json_object"}
        # It causes the 400 error on Gemma 3

        content = response.choices[0].message.content

        # Clean up the response in case the model adds ```json ... ``` blocks
        clean_content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(clean_content)["subtasks"]
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


# Test call
# print(generate_tasks("I wanna make a rc car."))
