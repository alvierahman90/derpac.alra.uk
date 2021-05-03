# derpac.designs

vote for your favorite [derpac](https://github.com/derpac/) design!

1. Install docker
2. 
        ```
        $ docker build -t derpac.designs .
        $ docker run -p 8000:80 \
            --mount type=bind,source=`pwd`/votes.json,target=/usr/src/app/votes.json \
            --mount type=bind,source=`pwd`/options.json,target=/usr/src/app/options \
            -t derpac.designs
        ```

## features

- sad faces
- not using a real database
- doughnuts
