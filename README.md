
**Paycheck Protection Program(PPP): Tracking and analyzing loans distribution among small businesses in New York City**

PPP’s goal is to provide small businesses with the necessary resources to maintain payroll, hire back employees who may have 
been laid off and cover applicable overhead through Small Business Association(SBA)-guaranteed private loans from commercial banks. 
As a result, PPP enables small businesses continuity, fewer jobs lost and more small business staying afloat while contributing to 
overall economic recovery.

Considering there is limited preliminary data on the impact and effectiveness of PPP as a policy, this analysis focuses on 
private loans' distribution among small businesses in New York City covering the 5 boroughs that make up NYC. The objective 
of this repository and analysis is to quantify PPP loans distribution among Small Businesses in New York City.  

**Inputs**
1. The "ppp_loans_state_NY.csv" csv file contains all the data for the loans distribution analysis among small businesses analysis, 
generating "cleaned_ppp_nyc_data.csv" as the output.
2. Graph of top industries before PPP, which shows the latest records by the Census of the top industries in NY State.

**Scripts**
1. The "ppp_data_cleaning.py" file reads and filters the "ppp_loans_state_NY.csv" file to clean and narrow down the focus on the 5
boroughs of NYC, selecting only the variables of interest for analysis purposes and creates the "cleaned_ppp_nyc_data.csv" 
as the output for the next script, "ppp_data_analysis.py".
2. In the "ppp_data_analysis.py" file uses the clean data from the previous script to track and analyse the loans distribution among
small businesses while generating all of the table and pie charts as png files in the deliverables. 

**Deliverables**
1. The output "cleaned_ppp_data.csv"  filters the data with the interest variables and narrows it down to the 5 boroughs that make up New York City 
2. Several key graphs:

    2.1 Boroughs vs loan amount shows the total loans distribution by borough.
  
    2.2 Top 10 industries vs loan amount showcases which were the top 10 industries with the numbers of small businesses receiving loans.
  
    2.3 Top 10 lenders vs loan amount displays the top lenders providing loans for small businesses.
  
    2.4 Jobs reported by borough shows the number of jobs reported that were covered by PPP loans for payroll.
  
    2.5 Number of lenders for each borough highlights the influx of private loans.
    
    2.6 PPP loans in New York State by zipcode lays out loans distribution by zip code focused on NYC laying out NY State using Tableau.
  
3. PPP.pptx is the power point presentation for the PPP's analysis.

4. **Next steps:**
    4.1 Analyze the impact and effectiveness of PPP as a policy when data becomes available.






