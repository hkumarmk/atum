from atum.apiclient.base import AtumObject


class ImageBase(AtumObject):
    """Manage Images"""

    def create(self):
        pass

    def delete(self):
        pass


class ImageObject(object):

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("slug", None)
        self.public = kwargs.get("public", None)
        self.min_disk_size = kwargs.get("min_disk_size", None)
        self.created_at = kwargs.get("created_at", None)

        self.x_distribution = kwargs.get("distribution", None)
        self.x_regions = kwargs.get("regions", None)
        self.x_type = kwargs.get("type", None)