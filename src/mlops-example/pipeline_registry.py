"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.data_predict.pipeline import create_pipeline as predict_data


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["all_pipelines"]  = sum(pipelines.values())
    pipelines["__default__"]    = predict_data()
    return pipelines
