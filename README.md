Raid - Simple HTTP's requests generator
=======================================

[![Build Status](https://travis-ci.org/javidgon/raid.png)](https://travis-ci.org/javidgon/raid)

Raid, in some few words, is a simple **HTTP's requests generator**.
It's pretty handy for *testing high loads* in development
environments. Allows **concurrency** *(workers)* and **sequentiality**
*(requests per worker)*.

**Supported options:**

  - **-u, --url**: Requests' target *(Default: http://127.0.0.1:8000)*
  - **-w, --workers**: Number of workers in parallel *(Default: 1)*
  - **-r, --requests**: Number of requests per worker *(Default: 1)*

**In a nutshell:**
```
	python raid.py -u http://127.0.0.1:8000 -w 5 -r 10
```

*Friday, 11th January, 2013*
