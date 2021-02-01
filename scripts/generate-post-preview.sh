
POST=$1

docker run -it \
    -v $(pwd)/_posts:/app/_posts \
    -v $(pwd)/_people:/app/_people \
    -v $(pwd)/images:/app/images \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    datatalks-cover-generator \
    _posts/${POST}.md \
    images/posts/${POST}/cover.jpg
