now=$(date +"%m-%d-%y_%I-%M-%S")
echo "Current time: $now"

time_count=60
#time_count=300

#for word_name in "encUtil" "gpuUtil" "memUtil" "pwrDraw" "temp" "violPwr" "violThm" "decUtil"
#do
#  nvidia-smi stats -i $4 -d $word_name -c $time_count -f ./logs/$word_name_$1p_$2fps_$3c_gpu$4_$now.csv
#done

encUtil() {
  nvidia-smi stats -i $4 -d encUtil -c $time_count -f ./logs/encUtil_$1p_$2fps_$3c_gpu$4_$now.csv
}


gpuUtil() {
  nvidia-smi stats -i $4 -d gpuUtil -c $time_count -f ./logs/gpuUtil_$1p_$2fps_$3c_gpu$4_$now.csv
}

memUtil() {
  nvidia-smi stats -i $4 -d memUtil -c $time_count -f ./logs/memUtil_$1p_$2fps_$3c_gpu$4_$now.csv
}


pwrDraw() {
  nvidia-smi stats -i $4 -d pwrDraw -c $time_count -f ./logs/pwrDraw_$1p_$2fps_$3c_gpu$4_$now.csv
}

temp() {
  nvidia-smi stats -i $4 -d temp -c $time_count -f ./logs/temp_$1p_$2fps_$3c_gpu$4_$now.csv
}

violPwr() {
  nvidia-smi stats -i $4 -d violPwr -c $time_count -f ./logs/violPwr_$1p_$2fps_$3c_gpu$4_$now.csv
}

violThm() {
  nvidia-smi stats -i $4 -d violThm -c $time_count -f ./logs/violThm_$1p_$2fps_$3c_gpu$4_$now.csv
}

decUtil() {
  nvidia-smi stats -i $4 -d decUtil -c $time_count -f ./logs/decUtil_$1p_$2fps_$3c_gpu$4_$now.csv
}


encUtil $1 $2 $3 $4 &
gpuUtil $1 $2 $3 $4 &
memUtil $1 $2 $3 $4 &
pwrDraw $1 $2 $3 $4 &
temp    $1 $2 $3 $4 &
violPwr $1 $2 $3 $4 &
violThm $1 $2 $3 $4 &
decUtil $1 $2 $3 $4

