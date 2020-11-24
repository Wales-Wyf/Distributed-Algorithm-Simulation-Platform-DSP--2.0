@echo off
for /l %%x in (1,1,%1) do start /b python .\IoT\test.py %%x
exit
