# ./launch_contaiers.sh <container ID> <number_containers>

for i in {1..20}
  do
	 echo "container: $i"
	 amc launch $1 -p webrtc
	 sleep 3
  done 
