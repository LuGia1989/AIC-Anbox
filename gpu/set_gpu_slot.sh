for i in {1..120} 
  do
    echo "Iterate No.: $i"	  
    juju ssh ams/0 -- /snap/bin/amc node set lxd0 gpu-slots 60
    juju ssh ams/0 -- /snap/bin/amc node set lxd0 gpu-encoder-slots 60
    amc node show lxd0
    sleep 1
done
