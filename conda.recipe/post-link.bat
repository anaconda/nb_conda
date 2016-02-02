"%PREFIX%\Scripts\python.exe" -m nb_conda.setup install --enable --prefix="%PREFIX%"

"%PREFIX%\python.exe" -c "import sys; print(sys.executable)"
