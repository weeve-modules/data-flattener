"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .flattener import flattener

log = getLogger("module")

def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            processed_data = []

            for data in received_data:
                flattened = flattener(data, "")

                # in case of flattener returning error
                if type(flattened) == str:
                    return None, flattened

                processed_data.append(flattened)

        else:
            processed_data = flattener(received_data, "")

            # in case of flattener returning error
            if type(processed_data) == str:
                return None, processed_data

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
