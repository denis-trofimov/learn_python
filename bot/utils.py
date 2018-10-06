#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pprint
from clarifai.rest import ClarifaiApp
import settings


def image_classification(file_name):
    """ Add ClarifaiApp call for image_classification"""
    is_cat = False
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    response = model.predict_by_filename(file_name, max_concepts=5)
#    pprint.pprint(response)
    if response['status']['code'] == 10000:
        for concept in response['outputs'][0]['data']['concepts']:
            if concept.get('name') == 'cat':
                is_cat = True
                break
    return is_cat


if __name__ == "__main__":
#    image_classification('images/cat1.jpg')
    if image_classification('2017-10-14 14-25-04.JPG'):
        print('Have cat!')
