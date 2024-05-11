from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/multiply-matrices")
def multiply_matrices():
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    product = numpy.matmul(matrix_a, matrix_b)
    matrix_a_list = matrix_a.tolist()
    matrix_b_list = matrix_b.tolist()
    product_list = product.tolist()
    response_data = {
        "matrix_a": matrix_a_list,
        "matrix_b": matrix_b_list,
        "product": product_list
    }
    return response_data
