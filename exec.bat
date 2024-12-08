@echo off
setlocal enabledelayedexpansion

Set _fBlack=[30m
Set _fRed=[31m
Set _fGreen=[32m
Set _fYellow=[33m
Set _fBlue=[34m
Set _fMag=[35m
Set _fCyan=[36m
Set _fLGray=[37m
Set _fDGray=[90m
Set _fBRed=[91m
Set _fBGreen=[92m
Set _fBYellow=[93m
Set _fBBlue=[94m
Set _fBMag=[95m
Set _fBCyan=[96m
Set _fBWhite=[97m

Set _bBlack=[40m
Set _bRed=[41m
Set _bGreen=[42m
Set _bYellow=[43m
Set _bBlue=[44m
Set _bMag=[45m
Set _bCyan=[46m
Set _bLGray=[47m
Set _bDGray=[100m
Set _bBRed=[101m
Set _bBGreen=[102m
Set _bBYellow=[103m
Set _bBBlue=[104m
Set _bBMag=[105m
Set _bBCyan=[106m
Set _bBWhite=[107m

Set _RESET=[0m

for %%f in (*.png) do (
    set "filename=%%~nf"
    
    echo Processando arquivo: %_fRed%%_bBlack% %%f %_RESET% para: %_fGreen%%_bBlack% !filename!.txt %_fYellow%%_bBlack%
    
    replace_transparency_with_white.py %%f input.png
    convert_to_grayscale.py input.png input.png
    resize_image.py input.png input.png 18 18
    image_to_text.py input.png !filename!.txt
    get_image_resolution.py input.png env_vars.bat
    
    echo %_fBBlue%%_bBlack%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    call env_vars.bat
    
    echo @startuml > !filename!.puml
    echo sprite $!filename! [!IMG_WIDTH!x!IMG_HEIGHT!/16] { >> !filename!.puml
    type !filename!.txt >> !filename!.puml
    echo } >> !filename!.puml
    echo @enduml >> !filename!.puml
    
    del !filename!.txt
    del env_vars.bat
    del input.png
    
    move /Y %%f .\files\.
    move /Y !filename!.puml .\files\.
    
    echo %_fBBlue%%_bBlack%=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=%_RESET%
)