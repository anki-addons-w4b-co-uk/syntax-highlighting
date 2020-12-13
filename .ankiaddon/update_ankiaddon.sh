clear
echo updating -- syntax-highlighting ankiaddon
7z u syntax_highlighting.ankiaddon ../src/* -xr0!__pycache__ -xr!__pycache__
echo done
start syntax_highlighting.ankiaddon
exec $SHELL
