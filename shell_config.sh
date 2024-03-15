alias ls="ls -aolh --color=auto"
alias grep="grep --color -hn"
PYDEVD_WARN_EVALUATION_TIMEOUT=500

# Add python file to path
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHONPATH="${PYTHONPATH}:${SCRIPT_DIR}"

function zlib_decompress() {
    python3 -c 'from term_tools import zlib_decompress; zlib_decompress()' $1
}

function zlib_compress() {
    python3 -c 'from term_tools import zlib_compress; zlib_compress()' $1
}