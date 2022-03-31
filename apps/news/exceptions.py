from rest_framework.exceptions import APIException


class NewsNotFound(APIException):
    status_code = 404
    deafult_detail = "The requested item does not exist"