# Copyright (c) Facebook, Inc. and its affiliates.
#!/bin/bash

python optimize.py --iter 200 --objmask 80.0 --size 0.01 --center 0.01 --smooth 1.0 \
                --hfacing 0.8 --gamma 1.0 --alpha 1.0 --smpl 0.1 --depth 0.1 --range 10.0 \
                --contact 0.5 --scale 100.0 --exp_name exp_refrigerator --category refrigerator \
                --cadpath /home/siyich/siyich/cad_sapien_2 --datapath /home/siyich/siyich/d3dhoi_video_data/ \
                --device 0 --use_gt_objmodel --use_gt_objpart  


