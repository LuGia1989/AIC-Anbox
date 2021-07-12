#################################################
# $1: resolution
# $2: fps
# $3: containers
# $4: gpu slot
#
# $./gpuResourceUsages.sh 720 30 10 0
#################################################

now=$(date +"%m-%d-%y_%I-%M-%S")
echo "Current time: $now"

for file in "decUtil.sh" "encUtil.sh" "gpuUtil.sh" "memUtil.sh" "pwrDraw.sh" "temp.sh" "violPwr.sh" "violThm.sh" 
do 
	./$file $1 $2 $3 $4 $now & 
done

sleep 125

echo "Data collection done!"

