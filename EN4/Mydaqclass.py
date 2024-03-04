## Code met dank aan Meinhard
                                                 
import nidaqmx as dx
import matplotlib.pyplot as plt
import numpy as np
import time

class MyDAQ():  
   
    def _init_(self):
        pass
 
    def writeread(self, samplerate1, sampsperchan1, voltarray,channelin1='ai0', channelout1='ao0'):
        with dx.Task('AOTask') as writeTask, dx.Task('AITask') as readTask:    
            readTask.ai_channels.add_ai_voltage_chan(f'myDAQ2/{channelin1}')
            writeTask.ao_channels.add_ao_voltage_chan(f'myDAQ2/{channelout1}')
            
            writeTask.timing.cfg_samp_clk_timing(samplerate1,sample_mode = dx.constants.AcquisitionType.FINITE, \
                                         samps_per_chan=sampsperchan1)
   
            
            writeTask.write(voltarray, auto_start=True)

            readTask.timing.cfg_samp_clk_timing(samplerate1,sample_mode = dx.constants.AcquisitionType.FINITE, samps_per_chan=sampsperchan1)

            data=readTask.read(number_of_samples_per_channel = sampsperchan1)
            
            time.sleep(sampsperchan1/samplerate1 + 0.001)

            writeTask.stop()
            return np.array(data)
        
    def readwrite(self, samplerate1,sampsperchan1,channelin1='ai0', channelout1='ao0'):
        with dx.Task('AOTask') as writeTask, dx.Task('AITask') as readTask:    
            
            writeTask.ao_channels.add_ao_voltage_chan(f'myDAQ2/{channelout1}')
            readTask.ai_channels.add_ai_voltage_chan(f'myDAQ2/{channelin1}')
            
            
            readTask.timing.cfg_samp_clk_timing(samplerate1,sample_mode = dx.constants.AcquisitionType.FINITE, samps_per_chan=sampsperchan1)
    

            data=readTask.read(number_of_samples_per_channel = sampsperchan1)

            writeTask.timing.cfg_samp_clk_timing(samplerate1,sample_mode = dx.constants.AcquisitionType.FINITE, \
                                         samps_per_chan=sampsperchan1)
   
            time.sleep(sampsperchan1/samplerate1 + 0.001)

            writeTask.stop()
            return np.array(data)