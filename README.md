### Examining NFT data from the NEAR blockchain

These scripts are intended to query the NEAR Blockchain for BI analysis and visualization. Using [NEAR Indexer](https://github.com/near/near-indexer-for-explorer) to access a Postgres database with live data. Performing some data cleaning and manipulation and exporting each record as individual JSON objects for input into [AWS Quicksight](https://aws.amazon.com/quicksight/) and perhaps other visualization tools. 

To run these you will need to go through a somewhat extensive setup of [NEAR CLI](https://docs.near.org/tools/near-cli). A cool feature of this project has been using Python to get input from a remote Postgres database, send that input to a local CLI, and cleaning the CLI output for storage and later processing. 

### Postgres Schema (NEAR Indexer database): 
![](https://github.com/sayerjk/blockchain-data/blob/main/near-indexer-for-explorer-db.png)
