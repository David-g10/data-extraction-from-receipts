EXECUTION:

To execute the code, you must only install the requirements.txt in a virtual environment, then you must leave in the "ocr_samples" folder the json inputs that contain the ocr response (the text), finally in the other folder "extracted_info" a resulting json with the required information will be generated for each input hosted in the first folder.

APPROACHES AND ASSUMPTIONS:

The text that comes in the ocr response in the key ["textAnnotations"][0] is not in the order that the image is visually appreciated. When performing the extraction through the patterns, this makes the procedure difficult. This problem could be solved using the other keys of the dictionary where the coordinates of the words are found and thus give them an order by line to the words. In this case, the aforementioned procedure was not carried out and an attempt was made to extract the original raw text.

At the time of reading the ocr information, it is intuited that the amount of
pages will always be 1, because the ocr performs the processing of
extraction for each image and normally the invoices are not documents that have several
pages. This is why it is indexed by [0].

In the text the SUBTOTAL and TOTAL_PER_ITEM fields are not in a standard location where a regex can be applied properly.

For multi-valued fields (line elements), it could have been done differently, instead of the findall method of the regex library, a key could have been generated within the final json for each of the ticket elements, so way to avoid dealing with problems with the dimensions of lists in cases of missing values.

