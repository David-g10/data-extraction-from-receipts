import json
import re
import yaml
import os
import glob

class Extractor():

    def __init__(self):
        self.config = yaml.safe_load(open(os.path.join("config", "config.yaml")))
    

if __name__ == "__main__":

    ocr_jsons = glob.glob("ocr_samples/*.json")
    extractor = Extractor()

    for ocr_json in ocr_jsons:
        f = open(ocr_json)
        receipt_json = json.load(f)
        text = receipt_json["pages"][0]["textAnnotations"][0]["description"]









