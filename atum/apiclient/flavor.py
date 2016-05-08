from atum.apiclient.base import AtumObject


class FlavorBase(AtumObject):
    """Manage Flavors"""

    def create(self):
        pass

    def delete(self):
        pass


class FlavorObject(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.memory = kwargs.get("memory", None)
        self.cpus = kwargs.get("cpus", None)
        self.disk = kwargs.get("disk", None)
        self.transfer = kwargs.get("transfer", None)
        self.available = kwargs.get("available", False)

        self.x_swap = kwargs.get("x_swap", None)
        self.x_ephemeral_disk = kwargs.get("x_ephemeral", None)
        self.x_public = kwargs.get("x_public", False)
        self.x_regions = kwargs.get("x_regions", None)
        self.x_cph = kwargs.get("x_cph", None)
        self.x_cpm = kwargs.get("x_cpm", None)
