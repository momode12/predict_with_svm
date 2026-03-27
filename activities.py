import httpx
from temporalio import activity

BASE_URL = "http://localhost:8000"

@activity.defn
async def predict_activity(mot: str) -> str:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE_URL}/predict", json={"mot": mot})
        return r.json()

@activity.defn
async def perf_number_activity() -> dict:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/show_perf_as_number")
        return r.json()

@activity.defn
async def perf_graph_activity() -> str:
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/show_perf_as_graph")
        r.raise_for_status()
        with open("svm_perf_result.png", "wb") as f:
            f.write(r.content)
        return "svm_perf_result.png"