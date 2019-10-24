@echo off
:: Run as admin source:
:: https://stackoverflow.com/questions/14639743/batch-script-to-run-as-administrator
:: icals doc:
:: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls

call :isAdmin

if %errorlevel% == 0 (
goto :run
) else (
echo Requesting administrative privileges...
goto :UACPrompt
)

exit /b

:isAdmin
fsutil dirty query %systemdrive% >nul
exit /b

:run
:: Init, put into variable?
echo Working direcotry: %~dp0

:: Installation
echo Installation de FreesSWITCH
msiexec /i "FreeSWITCH-1.10.0-Release-x64.msi" /passive

echo Creation du dossier "run"
mkdir "C:\Program Files\FreeSWITCH\run"

echo Donner les permissions sur le dossier
:: Administrateur
icacls "C:\Program Files\FreeSWITCH" /grant *S-1-5-21-2558747116-3120154829-1202218365-500:(F)

:: Utilisateur
icacls "C:\Program Files\FreeSWITCH" /grant *S-1-5-21-1538731068-585382227-1213672966-10360:(F)

:: Default account
icacls "C:\Program Files\FreeSWITCH" /grant *S-1-5-21-2558747116-3120154829-1202218365-503:(F)
icacls "C:\Program Files\FreeSWITCH" /grant Utilisateurs:(F)

echo Copie des fichiers de configuration du serveur
xcopy "%~dp0\conf" "C:\Program Files\FreeSWITCH\conf" /r /s /y /v /q

echo Demarrage du serveur FreeSwitch
"C:\Program Files\FreeSWITCH\FreeSwitchConsole.exe"

goto :end

:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "cmd.exe", "/c %~s0 %~1", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
del "%temp%\getadmin.vbs"
exit /B`

:end
pause
exit /b