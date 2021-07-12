for i in {1..30}
do
	nvidia-smi  --format=csv --query-gpu=clocks.current.graphics
done 
echo "+++++++++++++++++++++++++++++++++++++"


for i in {1..30} 
do
	nvidia-smi  --format=csv --query-gpu=clocks.current.memory
done

echo "+++++++++++++++++++++++++++++++++++++"

for i in {1..30}
do
	nvidia-smi  --format=csv --query-gpu=clocks.current.video
done
echo "+++++++++++++++++++++++++++++++++++++"
