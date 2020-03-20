import pandas as pd
def StackedBarSchemaDefination():
    dataFrame = pd.read_csv("disaster.csv")
    country_disaster = pd.DataFrame()
    outputCollector = pd.DataFrame()

    countryCode = dataFrame[['Entity', 'Code']].drop_duplicates(subset=['Entity'])
    countryCode = countryCode[countryCode["Code"].notnull()]
    start = 1996
    end = 2017
    rowList = []
    for Year in range(start,end):
        country_disaster = country_disaster.append(dataFrame[(dataFrame["Year"] == Year) & (dataFrame["Code"].notnull())])

    #Filtering each country
    range1 = country_disaster.query('Year >=1996 and Year<=2002')
    #print(range1.head(27))
    codeList = countryCode["Code"]
    range1.to_csv("output.csv")
    for code in codeList:
        range2 = range1[range1["Code"] == code]
        sumDeaths = int(round(range2["Deaths"].sum()))
        list = []
        list.append(code)
        list.append(sumDeaths)
        rowList.append(list)

    outputCollector = outputCollector.append(rowList)
    outputCollector.columns = ['Code', '1996-2002']

    range1 = country_disaster.query('Year >=2003 and Year<=2006')
    range2 = country_disaster.query('Year>=2007 and Year<=2010')
    range3 = country_disaster.query('Year>=2011 and Year<=2017')


    for code in codeList:
        #print(code)
        r1 = range1[range1["Code"] == code]
        r2 = range2[range2["Code"] == code]
        r3 = range3[range3["Code"] == code]
        print("range 2")
        print(range2)
        sumDeaths1 = int(round(r1["Deaths"].sum()))
        sumDeaths2 = int(round(r2["Deaths"].sum()))
        sumDeaths3 = int(round(r3["Deaths"].sum()))
        totalDeaths = sumDeaths1 + sumDeaths2 + sumDeaths3 + outputCollector.loc[outputCollector['Code']==code,'1996-2002']
        print(totalDeaths)


        outputCollector.loc[outputCollector['Code']==code,'2003-2006'] = sumDeaths1
        outputCollector.loc[outputCollector['Code']==code,'2007-2010'] = sumDeaths2
        outputCollector.loc[outputCollector['Code']==code,'2011-2017'] = sumDeaths3
        outputCollector.loc[outputCollector['Code']==code,'total'] = totalDeaths


    print(outputCollector)
    outputCollector.to_csv("stackBarData.csv")
StackedBarSchemaDefination()
