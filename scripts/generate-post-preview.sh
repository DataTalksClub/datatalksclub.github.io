# else nvm won't load
. ~/.nvm/nvm.sh
nvm use v10.17.0


cd previews

POST=$1

echo "post: ${POST}"

mkdir -p ../images/posts/${POST}/

node render.js \
    ../_posts/${POST}.md \
    ../images/posts/${POST}/cover.jpg