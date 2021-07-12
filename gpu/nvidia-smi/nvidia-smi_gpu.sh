FILE=./logs/gpu.log
if [ -f "$FILE" ]; then
	echo "$FILE exist.  Deleting...."
	rm "$FILE"
fi
echo "***********************************" >> ./logs/gpu.log
echo "Begin time ....." >> ./logs/gpu.log
echo "***********************************" >> ./logs/gpu.log
date +"%T" >> ./logs/gpu.log

for i in {1..120}; do nvidia-smi >> ./logs/gpu.log; sleep 1; done

echo "***********************************" >> ./logs/gpu.log
echo "End time ....." >> ./logs/gpu.log
echo "***********************************" >> ./logs/gpu.log
date +"%T" >> ./logs/gpu.log
