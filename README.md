# get_unused_gpu
module to get the index of unused gpu.

this module will return the index of unused gpu.

the condition regarded as unused GPU is shown below.

```
gpu temp: under 40°C
utilization.gpu: 0 %
utilization.memory: 0 %
```

this module will return only one index number.
and, if the condition is not filled, this module will crash with error message.

if you want to avoid it, please use with try ~ catch ~ sentence.
thank you.
