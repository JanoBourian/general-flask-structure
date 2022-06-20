# Here we can use (must have) pydantic for Models and typing
from typing_extensions import TypedDict
from typing import Optional, List
from pydantic import BaseModel, validator

# total = True means keys are required
class Filtro(TypedDict, total=True):
    id_tipo_filtro: int
    valor_filtro: int


class Payload(BaseModel):
    id_proceso_venta: int
    filtro_busqueda: Optional[List[Filtro]] = None

    @validator("id_proceso_venta")
    def is_valid_proceso_venta(cls, v):
        return v if isinstance(v, int) else False
