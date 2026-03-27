import asyncio
from temporalio.client import Client
from workflow import SVMPredictWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        SVMPredictWorkflow.run,
        "robe",                         # ← le mot à prédire
        id="svm-run-001",
        task_queue="svm-queue",
    )
    print("Résultat :", result)

asyncio.run(main())
