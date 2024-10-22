import copy
import pprint


def del_dictionary(data):
    cleared_dictionary = copy.deepcopy(data)
    for i in data.get('creatives'):
        kept_items = []
        for item in data['creatives'][i]:
            if 'checked' not in item or item['checked'] is True:
                kept_items.append(item)
        cleared_dictionary['creatives'][i] = kept_items

    keys_to_delete = []
    for key, value in cleared_dictionary.get('creatives').items():
        if not value or 'checked' not in value[0]:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del cleared_dictionary['creatives'][key]

    return cleared_dictionary


def main():
    dictionary = {
        'campaign_id': None,
        'campaign_name': '',
        'creatives': {
            'GAGAPPQ-2021_v1_IOAPPQ_packshot': [
                {
                    'checked': True,
                    'google_drive_url': 'https://drive.google.com/uc?export=view&id=1nwYmWi4s6n_LUr6dPOSfbkZ50cNNNpK5',
                    'id': '1nwYmWi4s6n_LUr6dPOSfbkZ50cNNNpK5',
                    'name': 'GAGAPPQ-2021_v1_35s_en_1080x1920.mp4'
                },
                {
                    'checked': True,
                    'google_drive_url': 'https://drive.google.com/uc?export=view&id=1O9bTCrOptj2LSU5hGZ8zL4E4f1vySpFL',
                    'id': '1O9bTCrOptj2LSU5hGZ8zL4E4f1vySpFL',
                    'name': 'GAGAPPQ-2021_v1_35s_en_1920x1080.mp4'
                },
                {
                    'end_card_path': {
                        'IOAPPQ_packshot.jpeg': '/Users/admin/Documents/GIT/aso_tools/aso_tools/unity/static/files/banner/IOAPPQ_packshot.jpeg'
                    }
                }
            ],
            'GAGAPPQ-2021_v2_IOAPPQ_packshot': [
                {
                    'checked': False,
                    'google_drive_url': 'https://drive.google.com/uc?export=view&id=1Kj6737kRGRhN2SmodeMRCvpqp53Cn8Uw',
                    'id': '1Kj6737kRGRhN2SmodeMRCvpqp53Cn8Uw',
                    'name': 'GAGAPPQ-2021_v2_35s_en_1920x1080.mp4'
                },
                {
                    'checked': False,
                    'google_drive_url': 'https://drive.google.com/uc?export=view&id=1rdYaEUzWQ1XUKuJXZdZ249FzGv5H4bVk',
                    'id': '1rdYaEUzWQ1XUKuJXZdZ249FzGv5H4bVk',
                    'name': 'GAGAPPQ-2021_v2_35s_en_1080x1920.mp4'
                },
                {
                    'end_card_path': {
                        'IOAPPQ_packshot.jpeg': '/Users/admin/Documents/GIT/aso_tools/aso_tools/unity/static/files/banner/IOAPPQ_packshot.jpeg'
                    }
                }
            ]
        }
    }
    pprint.pprint(del_dictionary(dictionary))


if __name__ == '__main__':
    main()
