@setlocal
@ECHO off
rem ---------------------------------

set THIS_PATH=%~dp0
set PROJECT_PATH=%THIS_PATH%..\..
set PROJECT_NAME=powertools

set PYTHONPATH=%PROJECT_PATH;%PYTHONPATH%
@pushd %PATH_PROJECT%


rem ---------------------------------

call sh\win\test
pip uninstall %PROJECT_NAME% --yes --verbose
pip install -e %PROJECT_PATH% --verbose


rem ---------------------------------
@popd
@endlocal
