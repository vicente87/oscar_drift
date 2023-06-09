"""API module."""

import logging
import os
from litestar import Router, get, post
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar.status_codes import (
    HTTP_200_OK,
)

from model import Model
from schemas import (
    HealthResponse,
    ModelInputData,
    PredictResponse,
)
from settings import (
    api_settings,
    model_settings,
    transformer_settings,
)

model = Model(
    settings_model=model_settings,
    settings_transformer=transformer_settings,
)

def predict(data: ModelInputData = Body(media_type=RequestEncodingType.MULTI_PART,),out) -> PredictResponse:
    """Predict function.

    :param data: model input data
    :type data: ModelInputData
    :return: prediction response
    :rtype: BasePredictionResponse
    """
    image = await data.image
    logging.info("Transforming image...")
    transformed_image = model.transform(
        data=image,
    )
    logging.info("Image transformed.")
    logging.info("Predicting...")
    prediction = model.predict(
        data=transformed_image,
    )
    logging.info("Prediction made.")
    result= PredictResponse(
        **prediction,
    )
    f = open(str(out)+".txt", "a")
    f.write(str(result)
    f.close()


img = Image.open(sys.argv[1])
predict(img,sys.argv[2])
