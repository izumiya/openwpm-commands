# openwpm-commands

### Install

An installation script, `install.sh` is included to: install the conda environment,
install unbranded firefox, and build the instrumentation extension.

All installation is confined to your conda environment and should not affect your machine.
The installation script will, however, override any existing conda environment named openwpm.

To run the install script, run

```bash
./install.sh
```

After running the install script, activate your conda environment by running:

```bash
conda activate openwpm
```

## Quick Start

To begin crawling, run the following command in your terminal:

```bash
python demo.py
```

Please note that you have 10 minutes until the process times out.
