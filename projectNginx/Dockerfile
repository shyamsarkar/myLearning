FROM nginx

COPY conf/ /etc/nginx/

# COPY conf.d/my_custom_config.conf /etc/nginx/conf.d/my_custom_config.conf

COPY html/ /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# docker run --name nginx-server -p 80:80 -v ./:/etc/nginx -v ./:/usr/share/nginx/html nginx
