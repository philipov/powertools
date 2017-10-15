@setlocal
@ECHO off

set THIS_PATH=%~dp0
set PROJECT_PATH=%THIS_PATH%..\..
set PIP_CONFIG_FILE=C:\dev\secrets\pip.ini
@pushd %PROJECT_PATH%

rem -- ToDo: macro to obtain __version__
twine upload %PROJECT_PATH%\dist\powertools-0.0.4-py3-none-any.whl --comment "add click extension"

@popd
@endlocal
