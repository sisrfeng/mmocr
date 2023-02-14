echo '不开代理, 不然brew有点问题 (毕竟换了tuna源)'
unset ALL_PROXY
unset HTTP_PROXY
unset HTTPS_PROXY
pqi use tuna > /dev/null


conda create -n openMM  python=3.8
conda activate openMM
conda install  pytorch cudatoolkit torchvision   -y
pipt
pip3 install openmim
mim install mmengine
mim install 'mmcv>=2.0.0rc1'
mim install 'mmdet>=3.0.0rc0'
git checkout 1.x
pip3 install -e .

