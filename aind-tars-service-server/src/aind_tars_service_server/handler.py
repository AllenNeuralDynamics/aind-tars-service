"""Module to retrieve data from TARS using session object"""

from copy import deepcopy
from typing import Any, Dict, List, Optional

from httpx import AsyncClient


class SessionHandler:
    """Handle pulling data from Sharepoint lists"""

    def __init__(self, client: AsyncClient):
        """
        Class constructor.
        Parameters
        ----------
        client : AsyncClient
        """
        self.client = client

    async def get_data(
        self, url: str, params: Optional[Dict[str, str]], limit: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Returns data from TARS.

        Parameters
        ----------
        url : str
        params : Dict[str, str] | None
        limit : int
          Limit number of items returned. Set to 0 to return all.

        Returns
        -------
        List[Dict[str, Any]]

        """

        params_copy = {"page": "0"} if params is None else deepcopy(params)
        response = await self.client.get(url=url, params=params_copy)
        response.raise_for_status()
        all_data = []
        more_pages = response.json()["morePages"]
        total_count = response.json()["totalCount"]
        page_num = response.json()["page"]
        all_data.extend(response.json()["data"])
        number_of_records = len(all_data)
        max_count = total_count if limit == 0 else min(total_count, limit)
        while more_pages and number_of_records < max_count:
            params_copy["page"] = page_num + 1
            response = await self.client.get(url=url, params=params_copy)
            response.raise_for_status()
            more_pages = response.json()["morePages"]
            page_num = response.json()["page"]
            all_data.extend(response.json()["data"])
            number_of_records = len(all_data)
        if limit and len(all_data) > 0:
            all_data = all_data[0:max_count]
        return all_data
