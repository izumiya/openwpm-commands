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

Follow these steps to begin crawling:

In your terminal, run the following command to generate the runner.sh script:

```bash
./generate_runner.sh openwpm $(pwd)/main.py
```

Start the crawling process by executing the runner.sh script:

```bash
./runner.sh
```

Please note that the process will time out after 10 minutes.

To stop the crawling process manually, enter "about:finish" into the location bar of your crawler browser. This action will signal the crawler to stop crawling.