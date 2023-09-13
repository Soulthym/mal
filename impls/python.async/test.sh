pushd ../..
make "test^python.async^step${1:-A}"
popd
