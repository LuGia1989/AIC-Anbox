import sys
import pandas as pd


f=sys.argv[1]
something = []
mylines = []
utils_all = []
utils = []
tempC = []
gpuMemoryUtils = []
powerConsumption = []


def gpu_utilization(f):
    with open(f, 'r+') as myfile:
        for line in myfile:
            mylines.append(line.rstrip('\n'))
    for idx, word in enumerate(mylines):
        index = word.find('0  Tesla T4')
        if index != -1:
            something.append(mylines[idx + 1])
    for i in something:
        utils_all.append(i.rstrip().split())
    for i in range(119):
        utils.append(utils_all[i][12].rstrip('%'))
        tempC.append(utils_all[i][2].rstrip('C'))
        gpuMemoryUtils.append((int(utils_all[i][8].rstrip('MiB'))/15109)*100)
        powerConsumption.append(utils_all[i][4].rstrip('W'))


    df_utils = pd.DataFrame(utils).astype('int')
    ave_utils = int(df_utils.mean())
    min_utils = int(df_utils.min())
    max_utils = int(df_utils.max())

    df_tempC  = pd.DataFrame(tempC).astype('int')
    ave_tempC = int(df_tempC.mean())
    min_tempC = int(df_tempC.min())
    max_tempC = int(df_tempC.max())

    df_gpuMemoryUtils  = pd.DataFrame(gpuMemoryUtils).astype('float')
    ave_gpuMemoryUtils = float(df_gpuMemoryUtils.mean())
    min_gpuMemoryUtils = float(df_gpuMemoryUtils.min())
    max_gpuMemoryUtils = float(df_gpuMemoryUtils.max())


    df_powerConsumption  = pd.DataFrame(powerConsumption).astype('int')
    ave_powerConsumption = int(df_powerConsumption.mean())
    min_powerConsumption = int(df_powerConsumption.min())
    max_powerConsumption = int(df_powerConsumption.max())


        
    return utils, ave_utils, min_utils, max_utils, tempC, ave_tempC, min_tempC, max_tempC, gpuMemoryUtils, \
            ave_gpuMemoryUtils, min_gpuMemoryUtils, max_gpuMemoryUtils, powerConsumption, ave_powerConsumption, min_powerConsumption, max_powerConsumption 

def main():
    utils, ave_utils, min_utils, max_utils, tempC, ave_tempC, min_tempC, max_tempC, \
            gpuMemoryUtils, ave_gpuMemoryUtils, min_gpuMemoryUtils, max_gpuMemoryUtils, \
            powerConsumption, ave_powerConsumption, min_powerConsumption, max_powerConsumption = gpu_utilization(f)
    print('#################################################')
    print('GPU UTILIZATION')
    #print(utils)
    print('Average GPU Utilization = '+ str(ave_utils) + '%')
    print('Min GPU Utilization = ' + str(min_utils) +'%')
    print('Max GPU Utilization = ' + str(max_utils) + '%')
    print('#################################################')
    print('GPU TEMPERATURE')
    #print(tempC)
    print('Average Temperature = ' + str( ave_tempC) + 'C')
    print('Min Temperature = '+ str(min_tempC) + 'C')
    print('Max Temperature = '+ str(max_tempC) +'C')
    print('#################################################')
    print('GPU MEMORY UTILIZATION')
    #print(gpuMemoryUtils)
    print('Average gpu memory utilization = ' + '{:.2f}'.format(ave_gpuMemoryUtils) + '%')
    print('Min gpu memory utilization     = ' + '{:.2f}'.format(min_gpuMemoryUtils) + '%')
    print('Max gpu memory utilization     = ' + '{:.2f}'.format(max_gpuMemoryUtils) + '%')
    print('#################################################')
    print('GPU POWER CONSUMPTION')
    #print(powerConsumption)
    print('Average Power Consumption = ', ave_powerConsumption, 'Watts')
    print('Min Power Consumption = ', min_powerConsumption, 'Watts')
    print('Max Power Consumption = ', max_powerConsumption, 'Watts')
    print('#################################################')



if __name__ == '__main__':
        main()
