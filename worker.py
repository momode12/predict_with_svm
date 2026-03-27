import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import (
    SandboxedWorkflowRunner,
    SandboxRestrictions,
)
from workflow import SVMPredictWorkflow
from activities import predict_activity, perf_number_activity, perf_graph_activity

async def main():
    print("Connexion au Temporal Server...")
    client = await Client.connect("localhost:7233")
    print("Connecté !")

    worker = Worker(
        client,
        task_queue="svm-queue",
        workflows=[SVMPredictWorkflow],
        activities=[predict_activity, perf_number_activity, perf_graph_activity],
        workflow_runner=SandboxedWorkflowRunner(
            restrictions=SandboxRestrictions.default.with_passthrough_modules("httpx")
        ),
    )
    print("Worker démarré sur svm-queue... en attente de tâches")
    await worker.run()

asyncio.run(main())