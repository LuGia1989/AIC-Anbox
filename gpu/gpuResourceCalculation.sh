#running_containers = "amc ls | grep -i 'running' | wc"
echo "##  Running containers  ##"
amc ls | grep -i 'running' | wc

for gpuID in 0 1
  do
    echo "====================================="
    echo "     GPU: $gpuID Performance Data    "
    echo "====================================="

    for file in gpuUtil encUtil memUtil pwrDraw temp  violPwr violThm decUtil
      do
	echo "###################################"
	echo "#TEST: $file                           "                    
	python3 $file.py ./logs/$file*_gpu$gpuID*.csv
	mv ./logs/$file*_gpu$gpuID*.csv ./logs/archives/
      done
  done


