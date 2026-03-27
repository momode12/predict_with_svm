from temporalio import workflow
from datetime import timedelta
from activity import predict_activity, perf_number_activity, perf_graph_activity

@workflow.defn
class SVMPredictWorkflow:
    @workflow.run
    async def run(self, mot: str) -> dict:

        prediction = await workflow.execute_activity(
            predict_activity,
            mot,
            start_to_close_timeout=timedelta(seconds=10),
        )
        perf = await workflow.execute_activity(
            perf_number_activity,
            start_to_close_timeout=timedelta(seconds=10),
        )
        graph = await workflow.execute_activity(
            perf_graph_activity,
            start_to_close_timeout=timedelta(seconds=15),
        )
        return {
            "mot": mot,
            "prediction": prediction,
            "accuracy": perf["accuracy"],
            "loss": perf["loss"],
            "graph_saved": graph,
        }