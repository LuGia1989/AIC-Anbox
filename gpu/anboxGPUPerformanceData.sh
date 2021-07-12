#sleeptime = 130
#sleeptime = 320

./gpuResourceGeneration.sh $1 $2 $3 0 &
sleep 1
./gpuResourceGeneration.sh $1 $2 $3 1
sleep 3
./gpuResourceCalculation.sh
