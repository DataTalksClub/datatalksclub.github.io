# else nvm won't load
. ~/.nvm/nvm.sh
nvm use v10.17.0

# docker run -it \
#     -v $(pwd)/_posts:/app/_posts \
#     -v $(pwd)/_people:/app/_people \
#     -v $(pwd)/images:/app/images \
#     -u $(id -u ${USER}):$(id -g ${USER}) \
#     datatalks-cover-generator \
#     _posts/${POST}.md \
#     images/posts/${POST}/cover.jpg


cd previews

POST=$1

echo "post: ${POST}"

node render.js \
    ../_posts/${POST}.md \
    ../images/posts/${POST}/cover.jpg