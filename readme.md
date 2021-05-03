# derpac.designs

vote for your favorite [derpac](https://github.com/derpac/) design!

1. Install docker
2. 
    ```bash
    $ git clone https://github.com/alvierahman90/derpac.designs
    $ cd derpac.designs
    $ docker build -t derpac.designs .
    $ mkdir options && echo '{}' > votes.json
    $ docker run -d -p 8000:80 \
        --name derpac.designs \
        --restart unless-stopped \
        --mount type=bind,source=`pwd`/votes.json,target=/usr/src/app/votes.json \
        --mount type=bind,source=`pwd`/options,target=/usr/src/app/options \
        -t derpac.designs
    ```

## features

- sad faces
- not using a real database
- doughnuts
