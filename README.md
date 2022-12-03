# Spring4Shell-PoC
Spring Framework vulnerability "Spring4Shell" (CVE-2022-22965) PoC

Spring4Shell is a vulnerability found on March 2022, the vulnerability leads to RCE on
servers running Spring Framework (Spring Core <=5.3.17 (the only confirmed exploit is on Tomcat)).

The vulnerability has patch available. 

## Information

 - [trendmicro](https://www.trendmicro.com/en_us/research/22/d/cve-2022-22965-analyzing-the-exploitation-of-spring4shell-vulner.html)
 - [lunasec](https://www.lunasec.io/docs/blog/spring-rce-vulnerabilities/)

## Deployment

- requirements Python3, Docker
Clone the PoC

```bash
git clone https://github.com/SheL3G/Spring4Shell-PoC.git
```

Change directory

```bash
cd Spring4Shell-PoC/
```

Download the python requirements

```bash
pip install -r requirements.txt
```

To run the vulnerable Docker you need to run the following command:

**Note** Docker needs to run as root (sudo)

```bash
  docker run -p 8080:8080 -p 8000:8000 --rm ghcr.io/denniskniep/vulnerable-app-spring4shell:latest
```

Now your vulnerable machine is up!

You should access to it Here: http://localhost:8080/helloworld/greeting

Run the Python PoC

```python
python3 Spring4Shell.py http://localhost:8080/helloworld/greeting
```

After that RCE (webshell) will pop up on your terminal (if the machine is vulnerable)

## Credits

- Vulnerable Docker machine [@denniskniep](https://github.com/denniskniep/Spring4Shell-vulnerable-app)

## License

[MIT](https://choosealicense.com/licenses/mit/)