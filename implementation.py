#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 14:14:20 2025

@author: psg
"""

import pandas as pd
import numpy as np
import pickle
from rdkit import DataStructs
from rdkit import Chem
from rdkit.Chem import AllChem
import bz2file as bz2

with bz2.open('final_fp.pbz2', 'rb') as f:
    df_indexed1 = pickle.load(f)
    
with bz2.open('clf_model.pbz2', 'rb') as f:
    clf = pickle.load(f)
    
with open('protein_names.pckl', 'rb') as file:
    name=pickle.load(file)
    
EC=pd.read_excel('all_EC_reteived.xlsx')

EC_name=pd.read_excel('EC data.xlsx')

EC_abundance=pd.read_excel('Ec_tax_genus_abun.xlsx')

l=[] 
for i in range(3001,4410):
    l.append(i) 
df_indexed1.columns = l

def CRCGMMetaPredict(sm):
    h=Chem.MolFromSmiles(sm)
    fpgen=AllChem.GetRDKitFPGenerator()
    h1=fpgen.GetFingerprint(h)
    h2=np.zeros((0,),dtype=np.int8)
    DataStructs.ConvertToNumpyArray(h1,h2)
    h4=pd.DataFrame(h2)
    h5=h4.transpose()
    h5['SMILES']=sm
    new_df=h5
    df1=new_df.iloc[:,0:2048]
    df4=pd.merge(df1, df_indexed1, how='cross')
    y_pred = clf.predict(df4)
    y_pred_df=pd.DataFrame(y_pred)
    res=name.join(y_pred_df)
    filtered_res = res[res[0] == 1]
    uni_jn=pd.merge(EC,filtered_res,left_on='Entry',right_on='PROTEIN_ID',how='right')
    uni_jn1=pd.merge(EC_name,uni_jn,left_on='EC',right_on='EC number',how='right')

    EC_only=uni_jn1[['EC number','Name']].drop_duplicates()
    uni_jn2=pd.merge(EC_abundance,EC_only,left_on='EC',right_on='EC number',how='right')
    uni_jn3=uni_jn2[['EC','Name','Genus','abundance']]
    uni_jn4=uni_jn3.dropna()

    return uni_jn4





