for i in {1..600};
do
	nvidia-smi --format=csv --query-gpu=clocks_throttle_reasons.hw_thermal_slowdown >> thermalchecking.log 
	sleep 0.1 
done
