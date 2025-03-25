from kedro.pipeline import Pipeline, node, pipeline

from .nodes import predict_price_from_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=predict_price_from_data,
                inputs=[
                    "input_data",
                    "regressor"
                ],
                outputs="predicted_price",
                name="predict_node",
            ),
        ]
    )
