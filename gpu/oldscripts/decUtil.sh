# $1: 720p or 1080p
# $2: fps
# $3: containers
# $4: gpu_slot
# $5: time

nvidia-smi stats -i $4 -d decUtil -c 120 -f ./logs/decUtil_$1p_$2fps_$3c_gpu$4_$5.csv
