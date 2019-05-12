import os
import pandas as pd
import barycorrpy
import numpy as np

def ccf_mask_combine(filenames,outname='',shift_to_stellarframe=True,rv=0.,targetname=""):
    """
    A function to combine different CCF mask files.
    
    INPUT:
        filenames - 
        shift_to_stellarframe: if true, shift from barycenter to stellar rest frame
        - For this either rv or targetname needs to be supplied
    
    NOTES:
        This assumes that the wavelengths in the *.mas files are in the barycentric frame
    
    EXAMPLE:
        files_mas = sorted(glob.glob("0_CCFS/GJ699/20190309/MASK/*.mas"))
        ccf_mask_combine(files_mas,shift_to_stellarframe=True,rv=1.,targetname='')
        ccf_mask_combine(files_mas,shift_to_stellarframe=True,targetname='GJ 699')
    """
    dfs = []
    for i in filenames:
        dfs.append(pd.read_csv(i,sep="\t",header=None,names=["wi","wf","w"]))
    df_all = pd.concat(dfs)
    df_all = df_all.sort_values("wi").reset_index(drop=True)
    dirname = os.path.dirname(os.path.abspath(filenames[0]))
    if shift_to_stellarframe:
        if targetname!="":
            print('Querying target {}'.format(targetname))
	    rv  = barycorrpy.get_stellar_data(targetname)[0]['rv']/1000.
            #target = targ.getServalTarget(targetname)
            #rv = target.rv
        print('Shifting to stellar restframe using RV={}km/s'.format(rv))
        df_all.wi = redshift(df_all.wi.values,0.,ve=rv)
        df_all.wf = redshift(df_all.wf.values,0.,ve=rv)
        comment = '# stellarframe, RV ={}km/s\n'.format(rv)
        if outname=='':
            savename = os.path.join(dirname,'0_COMBINED','combined_stellarframe.mas')
    else:
        print('Not shifting to stellarframe')
        comment = '# barycentricframe\n'
        if outname=='':
            savename = os.path.join(dirname,'0_COMBINED','combined_barycentricframe.mas')
    savedir = os.path.dirname(os.path.abspath(savename))
    try:
    	os.makedirs(savedir)
        print('Made directory {}'.format(savedir))
    except Exception as e:
        print('Skipping creating directory {}'.format(savedir))
    with open(savename,'w') as f:
        f.write(comment)
        df_all.to_csv(f,index=False,header=False,sep='\t')
    print('Wrote to {}'.format(savename))

def redshift(x, vo=0., ve=0.,def_wlog=False):
   """
   x: The measured wavelength.
   v: Speed of the observer [km/s].
   ve: Speed of the emitter [km/s].

   Returns:
      The emitted wavelength l'.

   Notes:
      f_m = f_e (Wright & Eastman 2014)
   """
   c = 299792.4580   # [km/s]
   if np.isnan(vo): vo = 0     
   a = (1.0+vo/c) / (1.0+ve/c)
   if def_wlog:
      return x+np.log(a)   # logarithmic
   else:
      return x*a
