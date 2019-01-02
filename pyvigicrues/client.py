import requests
import json
import datetime

VIGICRUES_OBS_URL = "https://www.vigicrues.gouv.fr/services/observations.json/index.php"

class PyVigicruesError(Exception):
    pass

class VigicruesClient(object):
    def __init__(self, stationid, type, timeout=None):
        """Initialize the client object."""
        self.stationid = stationid
        self.type = type
        self._timeout = timeout


    def get_data(self):
        """Get data."""

        try:
            payload = { 'CdStationHydro': self.stationid, 'GrdSerie': self.type, 'FormatSortie': 'json' }
            headers = { 'content-type': 'application/json' }
            raw_data = requests.get(VIGICRUES_OBS_URL,
                                            params=payload,
                                            headers=headers,
                                            allow_redirects=False,
                                            timeout=self._timeout)
        except OSError:
            raise PyVigicruesError("Can not get data")

        try:
            json_output = raw_data.json()
            return json_output

        except (OSError, json.decoder.JSONDecodeError):
            raise PyVigicruesError("Could not get data")
