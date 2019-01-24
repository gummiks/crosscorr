import CCF

def calculate_ccf(w,f,v,mask_l,mask_h,mask_w,berv=0.,wavel_clip_edges=2.):
    """
    Calculate a weighted binary mask CCF.

    INPUT:
        w - array of wavelengths for one order
        f - array of fluxes for one order
        v - velocity grid to loop over in km/s
        mask_l - left edges of binary mask
        mask_h - right edges of binary mask
        mask_w - weight of binary mask
        berv - barycentric velocity in km/s
        wavel_clip_edges - not use lines that are this close to the edge of the order

    OUTPUT:
        ccf - array of ccf evaluated at velocity grid v

    NOTES:
        - Uses the CCF fortran algorithm in CERES. Super fast.
        - Note that that algorithm uses the 1d Doppler EQ.
    """
    N = len(v)
    ccf = np.zeros(N)
    II = np.where( (mask_l > wavel_clip_edges+w.min()) & (mask_h < w.max()-wavel_clip_edges))
    nlines = len(II)

    # This is an additional scaling parameter in the CERES CCF generation, we don't need that so set to 1
    sn = np.ones(len(f))
    try:
        for k in range(N):
            nlines[k] = len(mask_l[II])
            ccf[k] = CCF.ccf(mask_l[II], 
                             mask_h[II], 
                             w,
                             f,
                             mask_w[II],
                             sn, # Additional SNR scaling factor, just setting to 1
                             v[k]-berv, # Doing similar to paras_mask_shift.pro
                             0.) # Additional velocity that is not needed
        return ccf
    except Exception as e:
        print(e)
        return np.zeros(len(v))
