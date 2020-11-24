Set ws = CreateObject("Wscript.Shell")
command = "cmd /c .\IoT\start.bat " & WScript.Arguments(0)
ws.run command, vbhide