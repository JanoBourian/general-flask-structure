from typing import List
from models.request_schema import Payload


class RutinaListadoProcesoVenta:
    def __init__(self, request_json):
        self.payload = Payload(**request_json)

    def start(self):
        # Validate id_proceso_venta
        id_proceso_venta = self.payload.id_proceso_venta
        if not id_proceso_venta:
            response = RutinaListadoProcesoVenta.prepare_response(
                message="id_proceso_venta no valido", status_code=400
            )
            return response

        # Validate each one item in filtro_busqueda

        response = RutinaListadoProcesoVenta.prepare_response()
        return response

    @classmethod
    def prepare_response(
        cls, information: List = [], message: str = "", status_code: int = 200
    ):
        output = {
            "datos": information,
            "mensaje_ejecucion": message,
            "codigo_ejecucion": status_code,
        }
        return output
