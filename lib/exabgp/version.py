import os

commit = "765dd59f"
release = "4.2.11-frr"
json = "4.2.11"
text = "4.2.11"
version = os.environ.get('EXABGP_VERSION',release)

# Do not change the first line as it is parsed by scripts

if __name__ == '__main__':
    import sys
    sys.stdout.write(version)
