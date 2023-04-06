_base_ = [
    'svtr-tiny_20e_st_mj.py',
]



# print(f'{_base_= }')

# print(f'{type(_base_)= }')
    # type(_base_)= <class 'mmengine.config.config.ConfigDict'>
    # _base_ 不是一个list!!!!!


# 我是一个故意的error
# print('本文件被ast.parse, 再执行, 所以故意的error, 在parse时就引发报错, 不会print(_base_)')

model = dict(
             preprocessor = dict(output_image_size=(48, 160), ),
             encoder      = dict(img_size = [48, 160],
                                 max_seq_len  = 40                              ,
                                 out_channels = 256                             ,
                                 embed_dims   = [128, 256, 384]                 ,
                                 depth        = [3, 6, 9]                       ,
                                 num_heads    = [4, 8, 12]                      ,
                                 mixer_types  = ['Local'] * 8 + ['Global'] * 10 ,
                                ),
             decoder       = dict(in_channels=256))

train_dataloader = dict(batch_size=32, )
