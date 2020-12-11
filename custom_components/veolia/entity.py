"""VeoliaEntity class"""
from datetime import datetime

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME


class VeoliaEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.config_entry.entry_id}_{self.name}"

    @property
    def device_info(self):
        return {
            "identifiers": {DOMAIN},
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "last_report": datetime.fromtimestamp(self.coordinator.data.get("time")),
        }