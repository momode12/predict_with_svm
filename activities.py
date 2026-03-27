import httpx
from temporalio import activity

BASE_URL = "http://localhost:8000"

@activity.defn
async def predict_activity(mot: str) -> str:
    async with httpx.AsyncClient() as client:
        payload = {"mot": mot}
        response = await client.post(f"{BASE_URL}/predict", json=payload)
        return response.json()

@activity.defn
async def perf_number_activity() -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/show_perf_as_number")
        return response.json()

@activity.defn
async def perf_graph_activity() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/show_perf_as_graph")
        response.raise_for_status()
        with open("svm_perf_result.png", "wb") as f:
            f.write(response.content)
        return "svm_perf_result.png"