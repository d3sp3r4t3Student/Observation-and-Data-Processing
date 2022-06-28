import numpy as np; import inspect; import re

def print_array(A, showinfo=False):
    '''
    Displays values of an array.
    If the size of the array is larger than 20 in any dimension, an equally distributed subset of 20 indices is displayed.
    Args: 
	A: a numpy array with arbitrary dimension
	showinfo: a bolean flag determining if additional information (type, range of values, average) should be displayed
    Returns: 
	none
    '''
    A2=A*1
    frame = inspect.currentframe()
    try:
        context = inspect.getframeinfo(frame.f_back).code_context
        varname = ''.join([line.strip() for line in context])
        m = re.search(r'print_array\s*\((.+?)\)$', varname)
        if m:
            varname = m.group(1)
    finally:
        del frame
    s=A2.shape;
    if len(s)==1:
        A2=np.reshape(A2,(s[0],1))
        s=(s[0],1)
    maxshowx=15
    maxshowy=15
    if (type(A.flat[0]) is np.uint8) and np.max(A2)>0:
        d=int(np.log10(np.max(A2)))+1
        fs="%"+str(d)+"i"
        maxshowy=int(125/(d+2))
    elif (type(A.flat[0]) is np.int32) or (type(A.flat[0]) is np.int64) or (type(A.flat[0]) is np.bool_):
        d=int(np.log10(np.max(A2)+1))+2
        fs="% "+str(d)+"i"
        maxshowy=int(125/(d+2))
    else:
        if (np.max(A2)>1e4) or (np.max(np.abs(A2))<0.01):
            if np.min(A2)>0:
                fs="% 4.1e"
            else:
                fs="% 4.2e"
        else:
            fs="% 8.2f"
    if showinfo:
        print('name:',varname[:-5], 'shape:',A.shape,'type:',\
         type(A.flat[0]).__name__,'values:('+str(np.min(A))+\
         '-'+str(np.max(A))+') mean:', np.mean(A), end='')
        print('(~x coord.)' if s[0]>maxshowx else '', end='')
        print('(~y coord.)' if s[1]>maxshowy else '')
    else:
        print(varname+':')
    if len(s)>2:
        A2=np.resize(A2,(s[0],s[1]))
    xc=np.rint(np.linspace(0,s[0]-1,num=min(maxshowx,s[0]),endpoint=True)).astype(int)
    yc=np.rint(np.linspace(0,s[1]-1,num=min(maxshowy,s[1]),endpoint=True)).astype(int)
    for x in xc:
        for y in yc:
            print((fs%A2[x,y]), end='')
        print()
    if (len(s)==3) and (s[2]>1) and (s[2]<5):
        A2=np.reshape(A,(s[0],s[1],s[2]))
        for i in range(1,s[2]):
            print('channel',i)
            print_array(A2[:,:,i])
    return
