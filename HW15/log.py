import logging

logger = logging.getLogger(__name__)
FORMAT = '{levelname:<8} - {asctime} - {msg}'
logging.basicConfig(filename='HW15.log', filemode='w', encoding='UTF-8', 
                    level=logging.INFO, style='{', format=FORMAT)