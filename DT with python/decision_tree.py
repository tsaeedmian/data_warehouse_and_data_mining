import pandas as pd
import numpy as np
df=pd.read_csv('Test_Decisiontree.csv')
def calc_field_gain(df, field_name):
    #CALC info_D
    info_D=calc_total_info(df)

    #extract the column you want to calculate entropy for 
    df1_column = df[field_name]
    #extract counts of the values in that column
    data_vals=df1_column.value_counts()
    # extract the name of each value count, categorical values
    index_vals=data_vals.index.values
  
    info_age=0
    for i in range(len(index_vals)):
        # get data table of the first categorical value, data table for sepcific categorical value
        df_sub=df.query(field_name + '=="' + index_vals[i] + '"')
        # get last column for the above sub data table
        df_sub_last_column=df_sub.iloc[:,-1]
        # count how manyes yess and nos in the above sub data table
        vals=df_sub_last_column.value_counts()
        # if the nubmer of yess is not zeor or the number of nos is not zero
        if(len(vals)>1):
            info_age += (df_sub.count()[0]/df.count()[0]*info(list(vals)))
        else:
            # if yes count or no count is 0 then log2(1) with give 0, so info result is always zero
            info_age += 0
    return info_D-info_age

def info(val_lst):
    tot = sum(val_lst)
    tot_info=0
    for x in val_lst:
        tot_info -= x/tot*np.log2(x/tot)
    return tot_info

def calc_total_info(df):
    #CALC info_D
    # extract the last column, the decision column
    df1_decision=df.iloc[:,-1]
    # get counts of total yess and nos
    total_yes_no=df1_decision.value_counts()
    # calculate info of the entire table
    info_D=info(list(total_yes_no))
    return info_D

if __name__ == '__main__':
    field_name='credit_rating'
    print('info gain of ' + field_name + ':',calc_field_gain(df,field_name))