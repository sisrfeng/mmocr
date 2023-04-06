toy_data_root = '/data2/wf2/seal_data/data_gen_cooked'
# toy_data_root = 'tests/data/rec_toy_dataset/'

toy_rec_train = dict(type='OCRDataset',
                     data_root   = toy_data_root,
                     data_prefix = dict(img_path='./'),
                     # data_prefix = dict(img_path='imgs/'),
                     ann_file    = 'train_labels.json',
                     pipeline    = None,
                     test_mode   = False,
                    )

toy_rec_test = dict(type='OCRDataset',
                    data_root   = toy_data_root,
                    data_prefix = dict(img_path='./'),
                    ann_file    = 'test_labels.json',
                    pipeline    = None,
                    test_mode   = True,
                   )
