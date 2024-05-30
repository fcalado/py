# Verson 1.0

from datetime import datetime, timedelta, date, time
from dateutil.relativedelta import relativedelta

## Put format AAAA-MM-DD for year + month + day
def fn_data_referencia(AAAA_MM_DD):
    global I_AAAAMMDD, U_AAAAMMDD, I_AAAAMMDD1, U_AAAAMMDD1, I_AAAA_MM_DD, U_AAAA_MM_DD, I_AAAA_MM_DD1, U_AAAA_MM_DD1, AAAAMM, AAAAMM1
    quote = "'"
    dString = AAAA_MM_DD

    #First day of next month
    P_DIA_MES_SEGUINTE = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=+1)).strftime('%Y-%m')+ '-01' 

    #First day of this month
    P_DIA_MES_ATUAL = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=+0)).strftime('%Y-%m')+ '-01' 

    #First day of this month without - (hyphen)
    I_AAAAMMDD = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=+0)).strftime('%Y%m')+ '01'

    #Last day of this month without - (hyphen)
    U_AAAAMMDD = (date(int(P_DIA_MES_SEGUINTE[0:4]),int(P_DIA_MES_SEGUINTE[5:7]),int(P_DIA_MES_SEGUINTE[8:10])) + relativedelta(days=-1)).strftime('%Y%m%d')

    #First day of last month without - (hyphen)
    I_AAAAMMDD1 = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=-1)).strftime('%Y%m')+ '01'

    #Last day of last month without - (hyphen)
    U_AAAAMMDD1 = (date(int(P_DIA_MES_ATUAL[0:4]),int(P_DIA_MES_ATUAL[5:7]),int(P_DIA_MES_ATUAL[8:10])) + relativedelta(days=-1)).strftime('%Y%m%d')

    #First day of this month with - (hyphen)
    I_AAAA_MM_DD = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=+0)).strftime('%Y-%m')+ '-01'

    #Last day of this month with - (hyphen)
    U_AAAA_MM_DD = (date(int(P_DIA_MES_SEGUINTE[0:4]),int(P_DIA_MES_SEGUINTE[5:7]),int(P_DIA_MES_SEGUINTE[8:10])) + relativedelta(days=-1)).strftime('%Y-%m-%d')

    #First day of last month with - (hyphen)
    I_AAAA_MM_DD1 = (date(int(dString[0:4]),int(dString[5:7]),int(dString[8:10])) + relativedelta(months=-1)).strftime('%Y-%m')+ '-01'

    #Last day of last month with - (hyphen)
    U_AAAA_MM_DD1 = (date(int(P_DIA_MES_ATUAL[0:4]),int(P_DIA_MES_ATUAL[5:7]),int(P_DIA_MES_ATUAL[8:10])) + relativedelta(days=-1)).strftime('%Y-%m-%d')

    #This Month format YYYYMM
    AAAAMM = I_AAAAMMDD[0:6]

    #Last Month format YYYYMM
    AAAAMM1 = I_AAAAMMDD1[0:6]