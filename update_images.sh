GITHUB_REPOSITORY=brleinad/guamapa-api
GUAMAPA_API_IMAGE=docker.pkg.github.com/$GITHUB_REPOSITORY/api:latest
NGINX_IMAGE=docker.pkg.github.com/$GITHUB_REPOSITORY/nginx:latest

echo $GUAMAPA_API_IMAGE
echo $NGINX_IMAGE
docker build -f ./nginx/Dockerfile -t $NGINX_IMAGE ./nginx && \
docker push $NGINX_IMAGE 
# docker build -f ./Dockerfile.prod -t  $GUAMAPA_API_IMAGE . && \
# docker push $GUAMAPA_API_IMAGE