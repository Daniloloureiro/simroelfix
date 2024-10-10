from fastapi import FastAPI, HTTPException
import os
from files.parameters import Params
from files.file_manager import FileManager
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
parameters_path = os.path.join(os.getcwd(), "simroel-py-v3", "parameters.json")
file_manager = FileManager()
params = Params()
app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/set_slot_size",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#from fastapi.staticfiles import StaticFiles
#app.mount("/app", StaticFiles(directory="app"), name="app")

class SlotSizeModel(BaseModel):
    slot_size: float
###TODO TESTANDO GET E SET(Preciso de ajuda, o GET está recebendo dos docs do FASTAPI, trocando o valor no site o get
###TODO Muda, porém o parameters.json não altera
###Parameters.json que é lido pelo main.py, o dentro de data não é lido e reconhecido.
@app.post("/set_slot_size")
def set_slot_size(slot_size_data: SlotSizeModel):
    try:
        success = file_manager.set_slot_size(slot_size_data.slot_size)
        if success:
            return {"message": "Slot size updated successfully", "new_value": slot_size_data.slot_size}
        else:
            raise HTTPException(status_code=500, detail="Failed to update slot size")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_slot_size")
def get_slot_size():
    try:
        params = file_manager.get_params()
        return {"slot_size": params["slot_size"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/get_n_cores")
def get_n_cores():
    params = Params()
    return {"n_cores": params.get_n_cores()}

@app.get("/get_cores")
def get_cores():
    params = Params()
    return {"cores": params.get_cores()}

@app.get("/get_allocation_type")
def get_allocation_type():
    params = Params()
    return {"allocation_type": params.get_allocation_type()}

@app.get("/get_allocation_fn")
def get_allocation_fn():
    params = Params()
    return {"allocation_fn": params.get_allocation_fn()}
### TODO TESTANDO GET E SET
class BandwidthModel(BaseModel):
    bandwidth: int
# POST endpoint to receive the bandwidth value
@app.post("/set_bandwidth")
def set_bandwidth(bandwidth: BandwidthModel):
    params.set_bandwidth(bandwidth.bandwidth)
    return {"message": "Bandwidth set successfully"}

@app.get("/get_bandwidth")
def get_bandwidth():
    return {"bandwidth": params.get_bandwidth()}

@app.get("/get_traffic_lambda")
def get_traffic_lambda():
    params = Params()
    return {"traffic_lambda": params.get_traffic_lambda()}

@app.get("/get_traffic_refresh")
def get_traffic_refresh():
    params = Params()
    return {"traffic_refresh": params.get_traffic_refresh()}

@app.get("/get_traffic_file")
def get_traffic_file():
    return {"traffic_file": params.get_traffic_file()}

@app.get("/get_traffic_conn_types")
def get_traffic_conn_types():
    return {"traffic_conn_types": params.get_traffic_conn_types()}

@app.get("/get_route_algorithm")
def get_route_algorithm():
    return {"route_algorithm": params.get_route_algorithm()}

@app.get("/get_k_routes")
def get_k_routes():
    return {"k_routes": params.get_k_routes()}

@app.get("/get_route_selection")
def get_route_selection():
    return {"route_selection": params.get_route_selection()}

@app.get("/get_pcc_holding_time")
def get_pcc_holding_time():
    return {"pcc_holding_time": params.get_pcc_holding_time()}

@app.get("/get_guard_band")
def get_guard_band():
    return {"guard_band": params.get_guard_band()}

@app.get("/get_conn_holding_time")
def get_conn_holding_time():
    return {"conn_holding_time": params.get_conn_holding_time()}

@app.get("/get_tracer")
def get_tracer():
    return {"tracer": params.get_tracer()}

@app.get("/get_osnr")
def get_osnr():
    return {"osnr": params.get_osnr()}

@app.get("/get_modulation")
def get_modulation():
    return {"modulation": params.get_modulation()}

@app.get("/get_lambda")
def get_lambda():
    return {"lambda": params.get_lambda()}

@app.get("/get_fn")
def get_fn():
    return {"fn": params.get_fn()}

@app.get("/get_p")
def get_p():
    return {"p": params.get_p()}

@app.get("/get_span_length")
def get_span_length():
    return {"span_length": params.get_span_length()}

@app.get("/get_node_loss")
def get_node_loss():
    return {"node_loss": params.get_node_loss()}

@app.get("/get_band_ref")
def get_band_ref():
    return {"bandwidth_reference": params.get_band_ref()}

@app.get("/get_limit_single_carrier")
def get_limit_single_carrier():
    return {"limit_single_carrier": params.get_limit_single_carrier()}

@app.get("/get_wavelength")
def get_wavelength():
    return {"wavelength": params.get_wavelength()}

@app.get("/get_bending_radius")
def get_bending_radius():
    return {"bending_radius": params.get_bending_radius()}

@app.get("/get_coupling_coeff")
def get_coupling_coeff():
    return {"coupling_coeff": params.get_coupling_coeff()}

@app.get("/get_core_pitch")
def get_core_pitch():
    return {"core_pitch": params.get_core_pitch()}

@app.get("/get_port_isolation")
def get_port_isolation():
    return {"port_isolation": params.get_port_isolation()}

@app.get("/get_crosstalk_reason")
def get_crosstalk_reason():
    return {"crosstalk_reason": params.get_crosstalk_reason()}

@app.get("/get_calculate_crosstalk")
def get_calculate_crosstalk():
    return {"calculate_crosstalk": params.get_calculate_crosstalk()}

@app.get("/get_confidence_interval")
def get_confidence_interval():
    return {"confidence_interval": params.get_confidence_interval()}

@app.get("/get_thread_number")
def get_thread_number():
    return {"thread_number": params.get_thread_number()}

@app.get("/get_pcc_time_threshold")
def get_pcc_time_threshold():
    return {"pcc_time_threshold": params.get_pcc_time_threshold()}

@app.get("/get_ber_type")
def get_ber_type():
    return {"ber_type": params.get_ber_type()}

@app.get("/mcf-config")
def get_mcf():
    params = Params()
    return {"mcf_config": params.get_mcf_config()}

@app.get("/file-topology")
def get_file_topology():
    params = Params()
    return {"file_topology": params.get_file_topology()}

@app.get("/get_xt_table")
def get_xt_table():
    params = Params()
    return {"xt_table": params.get_xt_table()}

@app.get("/get_osnr_table")
def get_osnr_table():
    params = Params()
    return {"osnr_table": params.get_osnr_table()}

@app.get("get_topology_info")
def get_topology_info():
    params = Params()
    return {"topology_info": params.get_topology_info()}

@app.get("/get_traffic_input_file")
def get_traffic_input_file():
    params = Params()
    return {"traffic_input_file": params.get_traffic_input_file()}

@app.get("/get_n_connections")
def get_n_connections():
    params = Params()
    return {"n_connections": params.get_n_connections()}
