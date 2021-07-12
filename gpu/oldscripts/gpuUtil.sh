# $1: 720p or 1080p
# $2: fps
# $3: containers
# $4: gpu_slot

nvidia-smi stats -i $4 -d gpuUtil -c 120 -f ./logs/gpuUtil_$1p_$2fps_$3c_gpu$4_$5.csv
