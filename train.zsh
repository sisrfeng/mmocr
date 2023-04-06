CONFIG='configs/textrecog/svtr/svtr-base_20e_st_mj.py'
GPUS=4
NNODES=${NNODES:-1}
NODE_RANK=${NODE_RANK:-0}
PORT=29501
MASTER_ADDR=${MASTER_ADDR:-"127.0.0.1"}

PYTHONPATH=".":$PYTHONPATH \
\python3 -m torch.distributed.launch \
    --nnodes=$NNODES \
    --node_rank=$NODE_RANK \
    --master_addr=$MASTER_ADDR \
    --nproc_per_node=$GPUS \
    --master_port=$PORT \
    tools/train.py \
    $CONFIG \
    --launcher pytorch ${@:3}  \
    --work-dir svtr_wf_out \
    --amp

