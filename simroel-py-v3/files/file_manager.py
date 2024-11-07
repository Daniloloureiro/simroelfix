import os
from glob import glob
import json


def structure(directory, extension):
    # Usando string raw (r) para evitar o erro de escape, estava dando erro pra encontrar(os 2 \\...)
    paths = glob(rf"{directory}\*{extension}")
    elements = list(map(lambda path: path.split("\\")[-1].replace(extension, ""), paths))

    return dict(zip(elements, paths))


def get_files(directory, extension="*.txt"):
    # Usando string raw (r) para evitar o erro de escape, estava dando erro pra encontrar(os 2 \\...)
    return glob(rf"{directory}\{extension}")

class FileManager(object):
    def __init__(self):
        abs_path = os.path.abspath(os.getcwd())
        # PATH ARRUMADO
        abs_path = abs_path[:abs_path.find("simroel-py-v3") + len('simroel-py-v3') + 1]
        self.data_dir = os.path.join(abs_path, "data")
        self.topologies_dir = os.path.join(self.data_dir, "topologies")
        self.osnr_dir = os.path.join(self.data_dir, "osnr")
        self.crosstalk_dir = os.path.join(self.data_dir, "crosstalk")
        self.parameters_path = os.path.join(self.data_dir, "parameters.json")
        self.confidence_interval_path = os.path.join(self.data_dir, "confidence_interval.csv")
        self.traffic_input_file_path = os.path.join(self.data_dir, "traffic_input_file.csv")
        self.parameters_path = "../simroel-py-v3/parameters.json"  # Pode ser ajustado para data...
        self.params = {"slot_size": 12.5}
        topologies_paths = get_files(self.topologies_dir)
        topologies = list(map(lambda path: path.split("\\")[1].replace(".txt", ""),
                              topologies_paths))

        self.dict_topologies = dict(zip(topologies, topologies_paths))
        self.traffic_input_file_path = os.path.join(self.data_dir, "traffic_input_file.csv")
        self.dict_topologies = structure(self.topologies_dir, ".txt")
        # print(self.dict_topologies)
        self.dict_osnr = structure(self.osnr_dir, ".txt")
        self.dict_crosstalk = structure(self.crosstalk_dir, ".txt")

    def create_default_params(self):
        # Cria um default, não sei se valeria a pena mas está aqui um esqueleto.
        default_params = {"slot_size": 12.5}  # Default initial value
        with open(self.parameters_path, "w") as f:
            json.dump(default_params, f, indent=4)

    def get_params(self):
        # print(self.parameters_path)
        with open(self.parameters_path, "r") as f:
            properties = json.load(f)
        return properties
    ###TODO Tentativas de escrever no parameters.json
    def save_params(self, params):
        try:
            with open(self.parameters_path, "w") as f:
                json.dump(params, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving parameters: {e}")
            return False

    def set_slot_size(self, slot_size):
        try:
            params = self.get_params()
            params["slot_size"] = slot_size
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting slot size: {e}")
            return False
    def set_core_pitch(self, core_pitch):
        try:
            params = self.get_params()
            params["core_pitch"] = core_pitch
            return self.save_params(params)
        except Exception as e:
            print(f"Error setting core pitch: {e}")
            return False