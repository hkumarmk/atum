
class FlavorBase(object):
    """Manage Flavors"""

    def list(self):
        pass

    def get(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass


class FlavorObject(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", None)
        self.memory = kwargs.get("memory", None)
        self.cpus = kwargs.get("cpus", None)
        self.disk = kwargs.get("disk", None)
        self.transfer = kwargs.get("transfer", None)
        self.available = kwargs.get("available", False)

        self.x_swap = kwargs.get("swap", None)
        self.x_ephemeral_disk = kwargs.get("ephemeral", None)
        self.x_public = kwargs.get("is_public", False)
        self.x_regions = kwargs.get("regions", None)
        self.x_cph = kwargs.get("price", None)
        self.x_cpm = kwargs.get("price_monthly", None)
        self.x_id = kwargs.get("id", None)
