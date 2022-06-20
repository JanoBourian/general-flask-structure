from flask import Request, make_response
from creditkit_tools.measure_time import measure_time
from services.RutinaListadoProcesoVenta import RutinaListadoProcesoVenta
import logging


@measure_time("expediente-listado-proceso-venta")
def run_function(request: Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    if request.method == "POST":
        try:
            request_json = request.get_json()
            logging.warning(f"START ROUTINE: expediente-listado-proceso-venta")
            logging.warning(f"request_json: {request_json}")
            response = RutinaListadoProcesoVenta(request_json).start()
            logging.warning(f"END ROUTINE: expediente-listado-proceso-venta")
            return make_response(response), response["codigo_ejecucion"]
        except Exception as e:
            logging.warning(f"ERROR: {e}")
            return (
                make_response(
                    {"datos": [], "mensaje_ejecucion": f"{e}", "codigo_ejecucion": 500}
                ),
                500,
            )
    else:
        return make_response({"message": "Method not allowed"}), 400
