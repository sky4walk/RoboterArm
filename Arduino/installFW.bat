REM Arduino ueber USB Bus anschliessen
REM %AVRPATH%\listComPorts.exe aufrufen um COM Port zu bestimmen
REM erhaltenen COM Port anstatt COM7 eintragen

SET AVRPATH=avrdude
SET COMPORT=COM10

%AVRPATH%\avrdude.exe -C%AVRPATH%\avrdude.conf -v -patmega328p -carduino -P%COMPORT% -b115200 -D -Uflash:w:RobotArmArduino.ino.hex:i 
