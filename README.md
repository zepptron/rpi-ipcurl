# rpi-ncup

### what?

This Container is build for ARM devices like the Raspberry. It updates the DynDNS Record at Namecheap. It's useful if you have multiple (sub)domains defined that needs to be updated but your router can only update one of them.

### how?

pass some environment variables (compose example):
```
version: "3"

services:
  ncup:
    image: zepp/rpi-ncup:latest
    environment:
      pass: "_YOUR_TOKEN_"
      domain: "cest.io"
      host: "*"
      host2: "@"
    deploy:
      restart_policy:
        condition: on-failure
```

Take the Dockerfile, adjust it to your needs and build it for any other architecture if you want.
If you need to add some more Hosts you have to adjust the `main.py`. It's super easy, feel free to use.