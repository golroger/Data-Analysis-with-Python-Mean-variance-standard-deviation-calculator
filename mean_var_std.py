import numpy as np

def calculate(list):

  if len(list) != 9 :
    raise ValueError("List must contain nine numbers.")
  elif len(list) == 9 :
    lar = np.array([list[0:3],list[3:6],list[6:9]])
    mean_l = [lar.mean(axis=0).tolist(), lar.mean(axis=1).tolist(),lar.mean()]
    var_l= [lar.var(axis=0).tolist(),lar.var(axis=1).tolist(), lar.var()]
    std_l =[lar.std(axis=0).tolist(),lar.std(axis=1).tolist() ,lar.std()]
    sum_l = [lar.sum(axis=0).tolist(),lar.sum(axis=1).tolist(),lar.sum()]
    max_l = [lar.max(axis=0).tolist(),lar.max(axis=1).tolist(),lar.max()]
    mix_l = [lar.min(axis=0).tolist(),lar.min(axis=1).tolist(),lar.min()]
     
    calculations ={
      'mean':mean_l,
      'variance':var_l,
      'standard deviation' :std_l ,
      'max' : max_l ,
      'min':mix_l ,
      'sum':sum_l
    }

    return calculations