import json
import re
import yaml
import os
import glob

class Extractor():

    def __init__(self) -> None: 
        self.config = yaml.safe_load(open(os.path.join("config", "config.yaml")))
        self.client = "JUMBO"
        self.line_items = []
        self.folder_results = "extracted_info"

        if self.client == "JUMBO":
            self.line_items = ["DESCRIPTION", "SKU", "TOTAL_PER_ITEM", "TAX_CODE"]
    
    def apply_regexs(self, fields_n_patterns, text) -> dict:
        extracted_info = {}
        
        for field,pattern in fields_n_patterns.items():
            if field not in self.line_items:
                extracted_info[field] = ''
                if re.search(pattern, text, re.S):
                    value = re.search(pattern, text, re.S)["capture"]
                    extracted_info[field] = value
            else:
                extracted_info[field] = re.findall(pattern, text)
        return extracted_info

    def check_lists_dimentions(self, extracted_info_dict) -> dict:
        number_of_items = int(extracted_info_dict["NUMBER_OF_ITEMS"])
        for field in extracted_info_dict.keys():
            if (type(extracted_info_dict[field]) is list) and (len(extracted_info_dict[field]) != number_of_items):
                extracted_info_dict[field].clear()
        return extracted_info_dict       
        
    def json_response(self, json_file, file_name) -> None:
        json_object = json.dumps(json_file)
        file_path = os.path.join(self.folder_results, file_name)
        with open(file_path, "w") as outfile:
            outfile.write(json_object)
   
if __name__ == "__main__":

    extractor = Extractor()
    client = extractor.client
    line_items = extractor.line_items

    ocr_jsons = glob.glob("ocr_samples/*.json")
    fields_n_patterns = Extractor().config[client]

    for ocr_json in ocr_jsons:
        try:
            f = open(ocr_json)
            receipt_json = json.load(f)
            text = receipt_json["pages"][0]["textAnnotations"][0]["description"]
            extracted_info = extractor.apply_regexs(fields_n_patterns, text)
            extracted_info = extractor.check_lists_dimentions(extracted_info)
            json_file_name = ocr_json[ocr_json.index("/")+1:-5]+ "_result_.json"
            extractor.json_response(extracted_info, json_file_name)
        except Exception as e:
            print(f"Could not perform the extraction of information for that text, due to: {e} in file {ocr_json}")









