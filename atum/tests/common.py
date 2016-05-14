digitalocean_output = {
    "Flavor": [
        {'regions': ['ams1', 'ams2', 'ams3', 'fra1', 'lon1', 'nyc1',
                     'nyc2', 'nyc3', 'sfo1', 'sgp1', 'tor1'],
         'price_monthly': 5.0, 'slug': '512mb', 'price_hourly': 0.00744,
         'available': True, 'disk': 20, 'memory': 512, 'vcpus': 1,
         'transfer': 1.0},
        {'regions': ['ams1', 'ams2', 'ams3', 'fra1', 'lon1', 'nyc1',
                     'nyc2', 'nyc3', 'sfo1', 'sgp1', 'tor1'],
         'price_monthly': 10.0, 'slug': '1gb', 'price_hourly': 0.01488,
         'available': True, 'disk': 30, 'memory': 1024, 'vcpus': 1,
         'transfer': 2.0}
    ],
    "Image": [
        {'id': 17168961, 'name': '1010.3.0 (beta)',
         'size_gigabytes': None, 'slug': 'coreos-beta',
         'regions': ['nyc1', 'sfo1', 'nyc2', 'ams2', 'sgp1', 'lon1',
                     'nyc3', 'ams3', 'fra1', 'tor1', 'sfo2'],
         'distribution': 'CoreOS', 'created_at': '2016-05-05T17:56:32Z',
         'public': True, 'min_disk_size': 20, 'type': 'snapshot'},
        {'id': 17154031, 'name': '7.2 x64', 'size_gigabytes': 19.66,
         'slug': 'centos-7-2-x64', 'regions': ['nyc1', 'sfo1', 'nyc2',
                                               'ams2', 'sgp1', 'lon1',
                                               'nyc3', 'ams3', 'fra1',
                                               'tor1', 'sfo2'],
         'distribution': 'CentOS', 'created_at': '2016-05-04T22:25:39Z',
         'public': True, 'min_disk_size': 20, 'type': 'snapshot'}
    ],
    "Region": [
        {'name': 'New York 1', 'slug': 'nyc1',
         'sizes': ['32gb', '16gb','2gb', '1gb', '4gb', '8gb', '512mb',
                   '64gb', '48gb'],
         'features': ['private_networking', 'backups', 'ipv6', 'metadata'],
         'available': True},
        {'name': 'San Francisco 1', 'slug': 'sfo1',
         'sizes': ['32gb', '16gb', '2gb', '1gb', '4gb', '8gb', '512mb',
                   '64gb', '48gb'],
         'features': ['private_networking', 'backups', 'ipv6', 'metadata'],
         'available': True}
    ]
}

digitalocean_expected_result = {
    "Flavor": [
        {'memory': 512, 'x_regions': ['ams1', 'ams2', 'ams3', 'fra1',
                                      'lon1', 'nyc1', 'nyc2', 'nyc3',
                                      'sfo1', 'sgp1', 'tor1'],
         'x_cpm': 5.0, 'disk': 20, 'x_cph': 0.00744,
         'available': True, 'transfer': 1.0, 'cpus': 1,
         'name': '512mb', 'id': '512mb'
         },
        {'memory': 1024, 'x_regions': ['ams1', 'ams2', 'ams3', 'fra1',
                                       'lon1', 'nyc1', 'nyc2', 'nyc3',
                                       'sfo1', 'sgp1', 'tor1'],
         'x_cpm': 10.0, 'disk': 30, 'x_cph': 0.01488,
         'available': True, 'transfer': 2.0, 'cpus': 1, 'name': '1gb',
         'id': '1gb'
         }
    ],
    "Image": [
        {'id': 17168961, 'name': 'coreos-beta',
         'created_at': '2016-05-05T17:56:32Z', 'min_disk': 20,
         'public': True, 'x_regions': ['nyc1', 'sfo1', 'nyc2', 'ams2',
                                       'sgp1', 'lon1', 'nyc3', 'ams3',
                                       'fra1', 'tor1', 'sfo2'],
         'x_type': 'snapshot', 'x_distribution': 'CoreOS'},
        {'id': 17154031, 'name': 'centos-7-2-x64',
         'created_at': '2016-05-04T22:25:39Z', 'min_disk': 20,
         'public': True, 'x_regions': ['nyc1', 'sfo1', 'nyc2', 'ams2',
                                       'sgp1', 'lon1', 'nyc3', 'ams3',
                                       'fra1', 'tor1', 'sfo2'],
         'x_type': 'snapshot', 'x_distribution': 'CentOS'}
    ],
    "Region": [
        {'name': 'New York 1', 'x_flavors': ['32gb', '16gb', '2gb', '1gb',
                                             '4gb', '8gb', '512mb',
                                             '64gb', '48gb'],
         'id': 'nyc1', 'x_available': True,'x_features': [
            'private_networking', 'backups', 'ipv6', 'metadata'
        ]},
        {'name': 'San Francisco 1', 'x_flavors': ['32gb', '16gb', '2gb',
                                                  '1gb', '4gb', '8gb',
                                                  '512mb', '64gb', '48gb'],
         'id': 'sfo1', 'x_available': True, 'x_features': [
            'private_networking', 'backups', 'ipv6', 'metadata'
        ]},
    ]
}
