#!/bin/bash
PACKAGES=( pyyaml )
VENV=".venv"
RUNF="run.sh"
if ! [ -d "$VENV" ]; then
    echo "Making $VENV directory"
    python3 -m venv .venv
fi
if [ -d "$VENV" ]; then
    echo "Installing PIP packages"
    source ".venv/bin/activate"
    for i in "${PACKAGES[@]}"; do
        pip install "$i"
    done
    deactivate
fi

if ! [ -f "$RUNF" ] && [ -d "$VENV" ]; then
    echo "Making $RUNF file"
    echo "#!/bin/bash" >> "$RUNF"
    echo "" >> "$RUNF"
    echo "DIR=\"\$(dirname \"\$0\")\"" >> "$RUNF"
    echo "export PYTHONPATH=\"\$DIR\"" >> "$RUNF"
    echo "" >> "$RUNF"
    echo "for i in \$(ls \"\$DIR\"); do" >> "$RUNF"
    echo "  d=\"\$DIR\"/\"\$i\"" >> "$RUNF"
    echo "  if [ -d \"\$i\" ]; then" >> "$RUNF"
    echo "      if [ -f \"\$d/__init__.py\" ]; then" >> "$RUNF"
    echo "          export PYTHONPATH+=\":\$d\"" >> "$RUNF"
    echo "      fi" >> "$RUNF"
    echo "  fi" >> "$RUNF"
    echo "done" >> "$RUNF"
    echo "" >> "$RUNF"
    echo "source $VENV/bin/activate" >> "$RUNF"
    echo "python __main__.py" >> "$RUNF"
    echo "deactivate" >> "$RUNF"
    chmod +x "$RUNF"
fi