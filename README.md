# link shortener

Shorts or links. This is an old proof of concept

# docker usage

```bash
  docker run -p 5000:5000 maxwittig/link_shortener
```

## installation

* Install python virtualenv
  ```bash
  python3 -m venv venv
  ```
  
* Source virtualenv
  ```bash
  source venv/bin/activate
  ```
  
* Install requirements
  ```bash
  pip install --require-hashes -r requirements.txt
  ```

## usage

* Start the server
  ```bash
  BASE_URL=https://your-url python3 __main__.py
  ```

* Goto localhost:5000 to see the result
