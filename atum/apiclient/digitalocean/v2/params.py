PARAMS = {
    "SSHKey": {
        "field_map": {
          "id": "id",
          "name": "name",
          "fingerprint": "fingerprint",
          "public_key": "public_key",
        },
        "url": "account/keys",
        "result_key": "ssh_keys",
        "object_class_name": "SSHKeyObject",
    },
    "FloatingIP": {
        "field_map": {
            "id": "ip",
            "ip": "ip",
            "server": "server",
            "region": "region",
        },
        "object_class_name": "FloatingIPObject",
        "url": "floating_ips",

    },
    "Tag": {
      "field_map": {
          "id": "name",
          "name": "name",
          "resources": "resources"
      },
    },
    "Domain": {
        'field_map': {
            "id": "name",
            "name": "name",
            "ttl": "ttl",
            "zone": "zone_file",
        },
    },
    "Flavor": {
        "field_map": {
            "id": "slug",
            "name": "slug",
            "cpus": "vcpus",
            "memory": "memory",
            "available": "available",
            "disk": "disk",
            "transfer": "transfer",
            "x_cph": "price_hourly",
            "x_cpm": "price_monthly",
            "x_regions": "regions",
        },
        "url": "sizes",
    },
    "Image": {
        "field_map": {
            "id": "id",
            "name": "slug",
            "public": "public",
            "created_at": "created_at",
            "min_disk": "min_disk_size",
            "x_distribution": "distribution",
            "x_regions": "regions",
            "x_type": "type",
        },
    },
    "Region": {
        "field_map": {
            "id": "slug",
            "name": "name",
            "x_available": "available",
            "x_features": "features",
            "x_flavors": "sizes",
        },
    },
    "Server": {
        "field_map": {
            "id": "id",
            "name": "name",
            "cpus": "vcpus",
            "memory": "memory",
            "disk": "disk",
            "status": "status",
            "created_at": "created_at",
            "image": "image",
            "flavor": "size",
            "networks": "networks",
            "region": "region",
            "x_tags": "tags",
            "x_locked": "locked",
            "x_kernel": "kernel",
            "x_features": "features",
            "x_backup_ids": "backup_ids",
            "x_snapshot_ids": "snapshot_ids",
        },
        "url": "droplets",
    },
}
