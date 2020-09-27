# T035_Winsoft
This repository contains a website made in ACM-E-Cell Hackathon in September 2020.
The problem statement is to decrypt an encrypted message and find the optimal location in a given graph according to this.

## How the project works:
This project is built on two algorithms :
  * Decryption algorithm  (Takes O(N) time)
  * BFS on graphs (Takes O(V^2) time)
  
## What the project is:
We have written down the algorithms, and connected them to a website. The website is built in django.

* The first step when you go to this site is to login. 

![login_page](https://iili.io/2chrPa.md.png)

* The next step is to enter the encrypted message and key. You can provide a custom graph in the third field, or leave it bank to use the default graph.

![home_page](https://iili.io/2chPcv.md.png)

* You can now see the output

![home_page](https://iili.io/2chL9p.md.png)

