# jobguy-data-fetch
Fetch jobguy data using python with the JobGuy's public api.

#What is this?
It's a python script that will get data for companies on jobguy.ir that includes:
- Copmany info
- Reviews from former employees with related comments
- Interview experiences anyone shared with related comments

I wrote this script because jobguy.ir will shutdown very soon. I did not include any data in this repository, but you can use this script to fetch any data you want.

# How to use
First clone this repository from CLI:
`git clone https://github.com/imaun/jobguy-data-fetch.git`
You must have python installed in order to run blow scripts.

## Get All Companies
For generating the list of all companies run :
`python companyApi.py`
This will tries to get all of the companies on jobguy page by page, the limit of the pagination size is 50 I think. In the CLI you will see that the program will report which page is being fetched, if by any chance the program stucked at any page, you can set the `index` variable in the source by hand to the last page number that faced exception. At the end, all of the companies will be in a file named `companies.json`.

## Get specefic Company data
For fetching reviews, interviews and comments for each company, you can pass the name of that company to `companyReviews.py` script. For example if you want to get AliBaba company's data, from CLI run :
`python companyReview.py -company alibaba`
This will generate a directory named `alibaba` under data directory at the root of the script.

### What's Next
This repository will update soon to support all the jobguy's public api. But it will be useless after the shutdown. Hurry up if you want any data from it!

### Disclaimer
The Author of this software is not responsible for the data or any other information this software will generates.



