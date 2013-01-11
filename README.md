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

BSD LICENSE
-----------

Copyright (c) 2012 by Jose Vidal.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

    * The names of the contributors may not be used to endorse or
      promote products derived from this software without specific
      prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
