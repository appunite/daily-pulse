# daily-pulse

### What it is?
This repo is a set of scripts related to "Prasówka BAU/ADR" project. This project aims to share knowledge about AI in AU and make everyone up-to-date with changes in the company mentioned in ADRs and BAUs.

### Installation and running
Each script has mentioned steps for installation and running, as it might vary between them.

### MVP
The initial implementation consists of summarizing all ADRs which were decided the previous day and post a summary of them on Slack using GPT-3.5-turbo model.
It works like this:
1. Export ADRs from Notion
2. Run Python script which will:
  - Summarize them using GPT API
  - Forma  catchy message
  - Post it on Slack
  
### Versions
The current go-to version is the one in the directory `catchy`. The rest of them are not ready to run and require some more work (they are a different approach to this project).
