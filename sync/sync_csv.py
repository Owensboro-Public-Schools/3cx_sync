import os
import csv

from sync.sync import SyncSourceStrategy
from app.mapping import CSVMapping
from typing import Optional, List, Dict
from tcx_api.components.schemas.pbx import User
from sync.schema import CSVUser
from pydantic import TypeAdapter


def create_subclass_with_custom_comparison(prefix: str, base_class, properties_to_compare: list[str]):
    def custom_eq(self, other):
        # Compare only the specified properties
        for prop in properties_to_compare:
            if getattr(self, prop) != getattr(other, prop):
                return False
        return True

    return type(prefix + base_class.__name__, (base_class,), {"__eq__": custom_eq})


class SyncCSV(SyncSourceStrategy):
    @property
    def mapping(self):
        return self._mapping

    @mapping.setter
    def mapping(self, value):
        self._mapping = value

    def initialize(self):
        self.output("Initializing CSV Source")
        self.output("Loading CSV Mapping")
        self.mapping = CSVMapping()
        CSVUser._update_fields = self.mapping.get(
            "Extension", {}).get("Update", [])
        self.output("CSV Mapping Loaded")

    def get_source_users(self) -> Optional[List[User]]:
        user_data = list()
        self.output("Loading CSV User Data")
        csv_data_path = self.mapping.get("Extension", {}).get("Path", "")
        if not os.path.isfile(csv_data_path):
            self.output(f"Unable to find file at: {csv_data_path}")
            raise (FileNotFoundError)

        with open(csv_data_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            user_mapping = self.mapping.get("Extension").get("New")
            headers = next(csv_reader)
            headers = [user_mapping[key] for key in headers]

            for row in csv_reader:
                row_dict = dict(zip(headers, row))
                user_data.append(row_dict)
        csv_user_list = TypeAdapter(List[CSVUser]).validate_python(user_data)
        self.output(f"Loaded {len(csv_user_list)} Users from CSV File")
        return csv_user_list

    def get_source_groups(self):
        return None

    def comopare_users(self, tcx_users: list[User], source_users: list[User]):
        pass
