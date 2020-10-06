# 0x1A-application_server



![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201006%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201006T095604Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9bcd47827a4bfa1d08f27a6f446222cb773f4de6cbac27615a14077c12720338)


## Background Context :

[![IMAGE_ALT_TEXT_HERE](https://img.youtube.com/vi/pSrKT7m4Ego/0.jpg)](https://www.youtube.com/watch?v=pSrKT7m4Ego)


Your web infrastructure is already serving web pages via Nginx that you installed in your [first web stack project](https://github.com/Boul3ez85/holberton-system_engineering-devops/tree/master/0x0C-web_server). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.



## Resources


<B>Read or watch:</B>

- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [
How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in [route](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route) - strict_slashes
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)



## Requirements


### General

- A README.md file, at the root of the folder of the project, is mandatory
- Everything Python-related must be done using python3
- All config files must have comments



### Bash Scripts


- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

