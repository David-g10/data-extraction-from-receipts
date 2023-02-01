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

        if self.client == "JUMBO":
            self.line_items = ["DESCRIPTION"]
    
    def apply_regexs(self, fields_n_patterns, text) -> dict:
        extracted_info = {}
        
        for field,pattern in fields_n_patterns.items():
            if field not in self.line_items:
                extracted_info[field] = re.search(pattern, text, re.S)["capture"]
            else:
                extracted_info[field] = re.findall(pattern, text)
        return extracted_info

if __name__ == "__main__":

    extractor = Extractor()
    client = extractor.client
    line_items = extractor.line_items

    ocr_jsons = glob.glob("ocr_samples/*.json")
    fields_n_patterns = Extractor().config[client]

    for ocr_json in ocr_jsons:
        f = open(ocr_json)
        receipt_json = json.load(f)
        text = receipt_json["pages"][0]["textAnnotations"][0]["description"]
        extracted_info = extractor.apply_regexs(fields_n_patterns, text)
        print(extracted_info)







