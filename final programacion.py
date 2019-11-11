import numpy as np
import pandas as pd    #para que este codigo funcione es nescesario instalar la libreria "panda"
a=input("valor del credito")
global credito
credito = int(a)
global tasames   #se definen variables globales que se utilizaran en todos los metodos 
r=input ("porcentaje de interes mensual")
tasames= float(r)

def periodo1():
    amort=float("{0:.2f}".format(credito/12))
    
    p=(tasames*credito)/100
    u=amort+p
    po=credito-amort
    o=(tasames*po)/100
    i=amort+o
    y=po-amort
    
    oy=(tasames*y)/100    #notese que este trozo de codigo se repite con diferentes variables para ajustar los valores en la tabla
    iy=amort+oy
    yy=y-amort      # es el porcentaje del interes del saldo osea el 2,5 % de 200000 y luego para la segunda el 2,5 % de 183000, porque la deuda se disminuye
     
    ow=(tasames*yy)/100
    iw=amort+ow
    e=(tasames*yy)/100
    yw=yy-amort
    r=amort+e
    t=yw-amort
    
    ee=(tasames*t)/100
    re=amort+ee
    te=t-amort
    
    h=(tasames*te)/100
    c=amort+h
    q=te-amort
    
    hf=(tasames*q)/100
    cf=amort+hf
    qf=q-amort
    
    lo=(tasames*qf)/100
    la=amort+lo
    le=qf-amort
    
    io=(tasames*le)/100
    ia=amort+io
    ie=le-amort
    
    ko=(tasames*ie)/100
    ka=amort+ko
    ke=ie-amort
    
    ow=(tasames*ke)/100
    aw=amort+ow
    ew=ke-amort
    
    
    df = pd.DataFrame(
	    [[1,credito,amort,p,u,po],
	    [2,po,amort,o,i,y],
	    [3,y,amort,oy,iy,yy],
	    [4,yy,amort,ow,iw,yw],
	    [5,yw,amort,e,r,t],
	    [6,t,amort,ee,re,te],
	    [7,te,amort,h,c,q],
	    [8,q,amort,hf,cf,qf],
	    [9,qf,amort,lo,la,le],
	    [10,le,amort,io,ia,ie],
	    [11,ie,amort,ko,ka,ke],
	    [12,ke,amort,ow,aw,0]],
	
    columns = ['Cuota','Saldo','Amortizacion','Intereses','Valor Cuota ','Saldo final'])
    print(df)

def periodo2():
    amort=float("{0:.2f}".format(credito/24))
    p=(tasames*credito)/100
    u=amort+p
    po=credito-amort
    o=(tasames*po)/100
    i=amort+o
    y=po-amort
    oy=(tasames*y)/100    #notese que este trozo de codigo se repite con diferentes variables para ajustar los valores en la tabla
    iy=amort+oy
    yy=y-amort      
    ow=(tasames*yy)/100
    iw=amort+ow
    yw=yy-amort
    e=(tasames*yw)/100
    r=amort+e
    t=yw-amort
    ee=(tasames*t)/100
    re=amort+ee
    te=t-amort
    h=(tasames*te)/100
    c=amort+h
    q=te-amort
    hf=(tasames*q)/100
    cf=amort+hf
    qf=q-amort
    lo=(tasames*qf)/100
    la=amort+lo
    le=qf-amort
    io=(tasames*le)/100
    ia=amort+io
    ie=le-amort
    ko=(tasames*ie)/100
    ka=amort+ko
    ke=ie-amort
    fw=(tasames*ke)/100
    aw=amort+fw
    ew=ke-amort
    pi=(tasames*ew)/100
    pa=amort+pi
    pe=ew-amort
    zw=(tasames*pe)/100
    pw=amort+zw
    rw=pe-amort
    og=(tasames*rw)/100
    ag=amort+og
    eg=rw-amort
    ox=(tasames*eg)/100
    ax=amort+ox
    ex=eg-amort
    oj=(tasames*ex)/100
    aj=amort+oj
    ej=ex-amort
    ol=(tasames*ej)/100
    al=amort+ol
    el=ej-amort
    
    wi=(tasames*el)/100
    wu=amort+wi
    wl=el-amort
    
    s=(tasames*wl)/100
    sw=amort+s
    sd=wl-amort
    
    sg=(tasames*sd)/100
    sh=amort+sg
    sk=sd-amort
    
    sf=(tasames*sk)/100
    sa=amort+sf
    se=sk-amort
    
    sfw=(tasames*se)/100
    saw=amort+sfw
    sew=se-amort
    
    sfe=(tasames*sfw)/100
    sae=amort+sfe
    see=0
    df = pd.DataFrame(
	    [[1,credito,amort,p,u,po],
	    [2,po,amort,o,i,y],
	    [3,y,amort,oy,iy,yy],
	    [4,yy,amort,ow,iw,yw],
	    [5,yw,amort,e,r,t],
	    [6,t,amort,ee,re,te],
	    [7,te,amort,h,c,q],
	    [8,q,amort,hf,cf,qf],
	    [9,qf,amort,lo,la,le],
	    [10,le,amort,io,ia,ie],
	    [11,ie,amort,ko,ka,ke],
	    [12,ke,amort,ow,aw,ew],
        [13,ew,amort,pi,pa,pe],
        [14,pe,amort,zw,pw,rw],
        [15,rw,amort,og,ag,eg],
	    [16,eg,amort,ox,ax,ex],
	    [17,ex,amort,oj,aj,ej],
	    [18,ej,amort,ol,al,el],
	    [19,el,amort,wi,wu,wl],
	    [20,wl,amort,s,sw,sd],
	    [21,sd,amort,sg,sh,sk],
	    [22,sk,amort,sf,sa,se],
	    [23,se,amort,sfw,saw,sew],
	    [24,sew,amort,sfe,sae,see]],
    columns = ['Cuota','Saldo','Amortizacion','Intereses','Valor Cuota ','Saldo final'])
    print(df)


def periodo3():
    amort=float("{0:.2f}".format(credito/36))
    p=(tasames*credito)/100
    u=amort+p
    po=credito-amort
    o=(tasames*po)/100
    i=amort+o
    y=po-amort
    oy=(tasames*y)/100    #notese que este trozo de codigo se repite con diferentes variables para ajustar los valores en la tabla
    iy=amort+oy
    yy=y-amort      # acordarse de preguntar bien por la formula de interes
    ow=(tasames*yy)/100
    iw=amort+ow
    yw=yy-amort
    e=(tasames*yw)/100
    r=amort+e
    t=yw-amort
    ee=(tasames*t)/100
    re=amort+ee
    te=t-amort
    h=(tasames*te)/100
    c=amort+h
    q=te-amort
    hf=(tasames*q)/100
    cf=amort+hf
    qf=q-amort
    lo=(tasames*qf)/100
    la=amort+lo
    le=qf-amort
    io=(tasames*le)/100
    ia=amort+io
    ie=le-amort
    ko=(tasames*ie)/100
    ka=amort+ko
    ke=ie-amort
    fw=(tasames*ke)/100
    aw=amort+fw
    ew=ke-amort
    pi=(tasames*ew)/100
    pa=amort+pi
    pe=ew-amort
    zw=(tasames*pe)/100
    pw=amort+zw
    rw=pe-amort
    og=(tasames*rw)/100
    ag=amort+og
    eg=rw-amort
    ox=(tasames*eg)/100
    ax=amort+ox
    ex=eg-amort
    oj=(tasames*ex)/100
    aj=amort+oj
    ej=ex-amort
    ol=(tasames*ej)/100
    al=amort+ol
    el=ej-amort
    
    wi=(tasames*el)/100
    wu=amort+wi
    wl=el-amort
    
    s=(tasames*wl)/100
    sw=amort+s
    sd=wl-amort
    
    sg=(tasames*sd)/100
    sh=amort+sg
    sk=sd-amort
    
    sf=(tasames*sk)/100
    sa=amort+sf
    se=sk-amort
    
    sfw=(tasames*se)/100
    saw=amort+sfw
    sew=se-amort
    
    sfe=(tasames*sew)/100
    sae=amort+sfe
    see=sew-amort
    
    ghu=(tasames*see)/100
    zas=amort+ghu
    zes=see-amort
    
    xwj=(tasames*zes)/100
    bve=amort+xwj
    uiy=zes-amort
    
    eda=(tasames*uiy)/100
    ade=amort+eda
    qwe=uiy-amort
    
    bjee=(tasames*qwe)/100
    hdf=amort+bjee
    fds=qwe-amort
    
    pls=(tasames*fds)/100
    sjh=amort+pls
    wqp=fds-amort
    
    sal=(tasames*wqp)/100
    zxc=amort+sal
    xma=wqp-amort
    
    vbs=(tasames*xma)/100
    tor=amort+vbs
    fin=xma-amort
    
    gop=(tasames*fin)/100
    zop=amort+gop
    hui=fin-amort
    
    dio=(tasames*hui)/100
    cun=amort+dio
    rin=hui-amort
    
    adi=(tasames*rin)/100
    bpn=amort+adi
    pio=rin-amort
    
    tro=(tasames*pio)/100
    yui=amort+tro
    kpy=pio-amort
    
    klp=(tasames*kpy)/100
    ndi=amort+klp
    ldf=kpy-amort
    
    
    df = pd.DataFrame(
	    [[1,credito,amort,p,u,po],
	    [2,po,amort,o,i,y],
	    [3,y,amort,oy,iy,yy],
	    [4,yy,amort,ow,iw,yw],
	    [5,yw,amort,e,r,t],
	    [6,t,amort,ee,re,te],
	    [7,te,amort,h,c,q],
	    [8,q,amort,hf,cf,qf],
	    [9,qf,amort,lo,la,le],
	    [10,le,amort,io,ia,ie],
	    [11,ie,amort,ko,ka,ke],
	    [12,ke,amort,ow,aw,ew],
        [13,ew,amort,pi,pa,pe],
        [14,pe,amort,zw,pw,rw],
        [15,rw,amort,og,ag,eg],
	    [16,eg,amort,ox,ax,ex],
	    [17,ex,amort,oj,aj,ej],
	    [18,ej,amort,ol,al,el],
	    [19,el,amort,wi,wu,wl],
	    [20,wl,amort,s,sw,sd],
	    [21,sd,amort,sg,sh,sk],
	    [22,sk,amort,sf,sa,se],
	    [23,se,amort,sfw,saw,sew],
	    [24,sew,amort,sfe,sae,see],
        [25,see,amort,ghu,zas,zes],
        [26,zes,amort,xwj,bve,uiy],
        [27,uiy,amort,eda,ade,qwe],
        [28,qwe,amort,bjee,hdf,fds],
	    [29,fds,amort,pls,sjh,wqp],
	    [30,wqp,amort,sal,zxc,xma],
	    [31,xma,amort,vbs,tor,fin],
	    [32,fin,amort,gop,zop,hui],
	    [33,hui,amort,dio,cun,rin],
	    [34,rin,amort,adi,bpn,pio],
	    [35,pio,amort,tro,yui,kpy],
	    [36,kpy,amort,klp,ndi,0]],
	    
        columns = ['Cuota','Saldo','Amortizacion','Intereses','Valor Cuota ','Saldo final'])
    print(df)


def periodo4():
    amort=float("{0:.2f}".format(credito/48))
    p=(tasames*credito)/100
    u=amort+p
    po=credito-amort
    o=(tasames*po)/100
    i=amort+o
    y=po-amort
    oy=(tasames*y)/100    #notese que este trozo de codigo se repite con diferentes variables para ajustar los valores en la tabla
    iy=amort+oy
    yy=y-amort      # es posible reutilizar las variables para cada uno de los metodos, porque son locales y no afectan al reso de metodos
    ow=(tasames*yy)/100
    iw=amort+ow
    yw=yy-amort
    e=(tasames*yw)/100
    r=amort+e
    t=yw-amort
    ee=(tasames*t)/100
    re=amort+ee
    te=t-amort
    h=(tasames*te)/100
    c=amort+h
    q=te-amort
    hf=(tasames*q)/100
    cf=amort+hf
    qf=q-amort
    lo=(tasames*qf)/100
    la=amort+lo
    le=qf-amort
    io=(tasames*le)/100
    ia=amort+io
    ie=le-amort
    ko=(tasames*ie)/100
    ka=amort+ko
    ke=ie-amort
    fw=(tasames*ke)/100
    aw=amort+fw
    ew=ke-amort
    pi=(tasames*ew)/100
    pa=amort+pi
    pe=ew-amort
    zw=(tasames*pe)/100
    pw=amort+zw
    rw=pe-amort
    og=(tasames*rw)/100
    ag=amort+og
    eg=rw-amort
    ox=(tasames*eg)/100
    ax=amort+ox
    ex=eg-amort
    oj=(tasames*ex)/100
    aj=amort+oj
    ej=ex-amort
    ol=(tasames*ej)/100
    al=amort+ol
    el=ej-amort
    
    wi=(tasames*el)/100
    wu=amort+wi
    wl=el-amort
    
    s=(tasames*wl)/100
    sw=amort+s
    sd=wl-amort
    
    sg=(tasames*sd)/100
    sh=amort+sg
    sk=sd-amort
    
    sf=(tasames*sk)/100
    sa=amort+sf
    se=sk-amort
    
    sfw=(tasames*se)/100
    saw=amort+sfw
    sew=se-amort
    
    sfe=(tasames*sew)/100
    sae=amort+sfe
    see=sew-amort
    
    ghu=(tasames*see)/100
    zas=amort+ghu
    zes=see-amort
    
    xwj=(tasames*zes)/100
    bve=amort+xwj
    uiy=zes-amort
    
    eda=(tasames*uiy)/100
    ade=amort+eda
    qwe=uiy-amort
    
    bjee=(tasames*qwe)/100
    hdf=amort+bjee
    fds=qwe-amort
    
    pls=(tasames*fds)/100
    sjh=amort+pls
    wqp=fds-amort
    
    sal=(tasames*wqp)/100
    zxc=amort+sal
    xma=wqp-amort
    
    vbs=(tasames*xma)/100
    tor=amort+vbs
    fin=xma-amort
    
    gop=(tasames*fin)/100
    zop=amort+gop
    hui=fin-amort
    
    dio=(tasames*hui)/100
    cun=amort+dio
    rin=hui-amort
    
    adi=(tasames*rin)/100
    bpn=amort+adi
    pio=rin-amort
    
    tro=(tasames*pio)/100
    yui=amort+tro
    kpy=pio-amort
    
    klp=(tasames*kpy)/100
    ndi=amort+klp
    ldf=kpy-amort
    
    sdf=(tasames*ldf)/100
    vbn=amort+sdf
    tgn=ldf-amort
    
    cgo=(tasames*tgn)/100
    njl=amort+cgo
    nfd=tgn-amort
    
    ier=(tasames*nfd)/100
    gsj=amort+ier
    yop=nfd-amort
    
    adp=(tasames*yop)/100
    fty=amort+adp
    iqw=yop-amort
    
    suc=(tasames*iqw)/100
    vsp=amort+suc
    ish=iqw-amort
    
    tsh=(tasames*ish)/100
    jña=amort+tsh
    spi=ish-amort
    
    zkd=(tasames*spi)/100
    lqd=amort+zkd
    xzs=spi-amort
    
    huj=(tasames*xzs)/100
    nzu=amort+huj
    clr=xzs-amort
    
    mur=(tasames*clr)/100
    nxk=amort+mur
    ahg=clr-amort
    
    lvb=(tasames*ahg)/100
    uta=amort+lvb
    epo=ahg-amort
    
    yuy=(tasames*epo)/100
    wñp=amort+yuy
    ccc=epo-amort
    
    www=(tasames*ccc)/100
    aaa=amort+www
    bbb=ccc-amort
    
    yuyr=(tasames*bbb)/100
    wñpr=amort+yuyr
    cccr=bbb-amort
    
    df = pd.DataFrame(
	    [[1,credito,amort,p,u,po],
	    [2,po,amort,o,i,y],
	    [3,y,amort,oy,iy,yy],
	    [4,yy,amort,ow,iw,yw],
	    [5,yw,amort,e,r,t],
	    [6,t,amort,ee,re,te],
	    [7,te,amort,h,c,q],
	    [8,q,amort,hf,cf,qf],
	    [9,qf,amort,lo,la,le],
	    [10,le,amort,io,ia,ie],
	    [11,ie,amort,ko,ka,ke],
	    [12,ke,amort,ow,aw,ew],
        [13,ew,amort,pi,pa,pe],
        [14,pe,amort,zw,pw,rw],
        [15,rw,amort,og,ag,eg],
	    [16,eg,amort,ox,ax,ex],
	    [17,ex,amort,oj,aj,ej],
	    [18,ej,amort,ol,al,el],
	    [19,el,amort,wi,wu,wl],
	    [20,wl,amort,s,sw,sd],
	    [21,sd,amort,sg,sh,sk],
	    [22,sk,amort,sf,sa,se],
	    [23,se,amort,sfw,saw,sew],
	    [24,sew,amort,sfe,sae,see],
        [25,see,amort,ghu,zas,zes],
        [26,zes,amort,xwj,bve,uiy],
        [27,uiy,amort,eda,ade,qwe],
        [28,qwe,amort,bjee,hdf,fds],
	    [29,fds,amort,pls,sjh,wqp],
	    [30,wqp,amort,sal,zxc,xma],
	    [31,xma,amort,vbs,tor,fin],
	    [32,fin,amort,gop,zop,hui],
	    [33,hui,amort,dio,cun,rin],
	    [34,rin,amort,adi,bpn,pio],
	    [35,pio,amort,tro,yui,kpy],
	    [36,kpy,amort,klp,ndi,ldf],
        [37,ldf,amort,sdf,vbn,tgn],
        [38,tgn,amort,cgo,njl,nfd],
        [39,nfd,amort,ier,gsj,yop],
        [40,yop,amort,adp,fty,iqw],
        [41,iqw,amort,suc,vsp,ish],
	    [42,ish,amort,tsh,jña,spi],
	    [43,spi,amort,zkd,lqd,xzs],
	    [44,xzs,amort,huj,nzu,clr],
	    [45,clr,amort,mur,nxk,ahg],
	    [46,ahg,amort,lvb,uta,epo],
	    [47,epo,amort,yuy,wñp,ccc],
	    [48,ccc,amort,www,aaa,0]],
	    
        columns = ['Cuota','Saldo','Amortizacion','Intereses','Valor Cuota ','Saldo final'])
    print(df)

def periodo5():
    amort=float("{0:.2f}".format(credito/60))
    p=(tasames*credito)/100
    u=amort+p
    po=credito-amort
    o=(tasames*po)/100
    i=amort+o
    y=po-amort
    oy=(tasames*y)/100    #notese que este trozo de codigo se repite con diferentes variables para ajustar los valores en la tabla
    iy=amort+oy
    yy=y-amort      # es posible reutilizar las variables para cada uno de los metodos, porque son locales y no afectan al reso de metodos
    ow=(tasames*yy)/100
    iw=amort+ow
    yw=yy-amort
    e=(tasames*yw)/100
    r=amort+e
    t=yw-amort
    ee=(tasames*t)/100
    re=amort+ee
    te=t-amort
    h=(tasames*te)/100
    c=amort+h
    q=te-amort
    hf=(tasames*q)/100
    cf=amort+hf
    qf=q-amort
    lo=(tasames*qf)/100
    la=amort+lo
    le=qf-amort
    io=(tasames*le)/100
    ia=amort+io
    ie=le-amort
    ko=(tasames*ie)/100
    ka=amort+ko
    ke=ie-amort
    fw=(tasames*ke)/100
    aw=amort+fw
    ew=ke-amort
    pi=(tasames*ew)/100
    pa=amort+pi
    pe=ew-amort
    zw=(tasames*pe)/100
    pw=amort+zw
    rw=pe-amort
    og=(tasames*rw)/100
    ag=amort+og
    eg=rw-amort
    ox=(tasames*eg)/100
    ax=amort+ox
    ex=eg-amort
    oj=(tasames*ex)/100
    aj=amort+oj
    ej=ex-amort
    ol=(tasames*ej)/100
    al=amort+ol
    el=ej-amort
    
    wi=(tasames*el)/100
    wu=amort+wi
    wl=el-amort
    
    s=(tasames*wl)/100
    sw=amort+s
    sd=wl-amort
    
    sg=(tasames*sd)/100
    sh=amort+sg
    sk=sd-amort
    
    sf=(tasames*sk)/100
    sa=amort+sf
    se=sk-amort
    
    sfw=(tasames*se)/100
    saw=amort+sfw
    sew=se-amort
    
    sfe=(tasames*sew)/100
    sae=amort+sfe
    see=sew-amort
    ghu=(tasames*see)/100
    zas=amort+ghu
    zes=see-amort
    xwj=(tasames*zes)/100
    bve=amort+xwj
    uiy=zes-amort
    eda=(tasames*uiy)/100
    ade=amort+eda
    qwe=uiy-amort
    bjee=(tasames*qwe)/100
    hdf=amort+bjee
    fds=qwe-amort
    pls=(tasames*fds)/100
    sjh=amort+pls
    wqp=fds-amort
    sal=(tasames*wqp)/100
    zxc=amort+sal
    xma=wqp-amort
    vbs=(tasames*xma)/100
    tor=amort+vbs
    fin=xma-amort
    gop=(tasames*fin)/100
    zop=amort+gop
    hui=fin-amort
    dio=(tasames*hui)/100
    cun=amort+dio
    rin=hui-amort
    adi=(tasames*rin)/100
    bpn=amort+adi
    pio=rin-amort
    tro=(tasames*pio)/100
    yui=amort+tro
    kpy=pio-amort
    klp=(tasames*kpy)/100
    ndi=amort+klp
    ldf=kpy-amort
    sdf=(tasames*ldf)/100
    vbn=amort+sdf
    tgn=ldf-amort
    cgo=(tasames*tgn)/100
    njl=amort+cgo
    nfd=tgn-amort
    ier=(tasames*nfd)/100
    gsj=amort+ier
    yop=nfd-amort
    adp=(tasames*yop)/100
    fty=amort+adp
    iqw=yop-amort
    suc=(tasames*iqw)/100
    vsp=amort+suc
    ish=iqw-amort
    tsh=(tasames*ish)/100
    jña=amort+tsh
    spi=ish-amort
    zkd=(tasames*spi)/100
    lqd=amort+zkd
    xzs=spi-amort
    huj=(tasames*xzs)/100
    nzu=amort+huj
    clr=xzs-amort
    mur=(tasames*clr)/100
    nxk=amort+mur
    ahg=clr-amort
    lvb=(tasames*ahg)/100
    uta=amort+lvb
    epo=ahg-amort
    yuy=(tasames*epo)/100
    wñp=amort+yuy
    ccc=epo-amort
    www=(tasames*ccc)/100
    aaa=amort+www
    bbb=ccc-amort
    yuyr=(tasames*bbb)/100
    wñpr=amort+yuyr
    cccr=bbb-amort
    wzñ=(tasames*cccr)/100
    kkk=amort+wzñ
    rrr=cccr-amort
    qwer=(tasames*rrr)/100
    wert=amort+qwer
    erty=rrr-amort
    rtyu=(tasames*erty)/100
    tyui=amort+rtyu
    yuio=erty-amort
    ykyr=(tasames*yuio)/100
    whpr=amort+ykyr
    oipu=yuio-amort
    uiop=(tasames*oipu)/100
    iopa=amort+uiop
    iops=oipu-amort
    opas=(tasames*iops)/100
    pasd=amort+opas
    asdf=iops-amort
    sdfg=(tasames*asdf)/100
    dfgh=amort+sdfg
    fghj=asdf-amort
    ghjk=(tasames*fghj)/100
    hjkl=amort+ghjk
    dedo=fghj-amort
    mnbv=(tasames*dedo)/100
    nbvc=amort+mnbv
    bvcx=dedo-amort
    endme=(tasames*bvcx)/100
    helpe=amort+endme
    war=dedo-amort
    yjyj=(tasames*war)/100
    hjhj=amort+yjyj
    phph=war-amort
    rout=(tasames*phph)/100
    roui=amort+rout
    mela=phph-amort
    df = pd.DataFrame(
	    [[1,credito,amort,p,u,po],
	    [2,po,amort,o,i,y],
	    [3,y,amort,oy,iy,yy],
	    [4,yy,amort,ow,iw,yw],
	    [5,yw,amort,e,r,t],
	    [6,t,amort,ee,re,te],
	    [7,te,amort,h,c,q],
	    [8,q,amort,hf,cf,qf],
	    [9,qf,amort,lo,la,le],
	    [10,le,amort,io,ia,ie],
	    [11,ie,amort,ko,ka,ke],
	    [12,ke,amort,ow,aw,ew],
        [13,ew,amort,pi,pa,pe],
        [14,pe,amort,zw,pw,rw],
        [15,rw,amort,og,ag,eg],
	    [16,eg,amort,ox,ax,ex],
	    [17,ex,amort,oj,aj,ej],
	    [18,ej,amort,ol,al,el],
	    [19,el,amort,wi,wu,wl],
	    [20,wl,amort,s,sw,sd],
	    [21,sd,amort,sg,sh,sk],
	    [22,sk,amort,sf,sa,se],
	    [23,se,amort,sfw,saw,sew],
	    [24,sew,amort,sfe,sae,see],
        [25,see,amort,ghu,zas,zes],
        [26,zes,amort,xwj,bve,uiy],
        [27,uiy,amort,eda,ade,qwe],
        [28,qwe,amort,bjee,hdf,fds],
	    [29,fds,amort,pls,sjh,wqp],
	    [30,wqp,amort,sal,zxc,xma],
	    [31,xma,amort,vbs,tor,fin],
	    [32,fin,amort,gop,zop,hui],
	    [33,hui,amort,dio,cun,rin],
	    [34,rin,amort,adi,bpn,pio],
	    [35,pio,amort,tro,yui,kpy],
	    [36,kpy,amort,klp,ndi,ldf],
        [37,ldf,amort,sdf,vbn,tgn],
        [38,tgn,amort,cgo,njl,nfd],
        [39,nfd,amort,ier,gsj,yop],
        [40,yop,amort,adp,fty,iqw],
        [41,iqw,amort,suc,vsp,ish],
	    [42,ish,amort,tsh,jña,spi],
	    [43,spi,amort,zkd,lqd,xzs],
	    [44,xzs,amort,huj,nzu,clr],
	    [45,clr,amort,mur,nxk,ahg],
	    [46,ahg,amort,lvb,uta,epo],
	    [47,epo,amort,yuy,wñp,ccc],
	    [48,ccc,amort,www,aaa,bbb],
	    [49,bbb,amort,yuyr,wñpr,cccr],
        [50,ldf,amort,wzñ,kkk,rrr],
        [51,tgn,amort,qwer,wert,erty],
        [52,nfd,amort,rtyu,tyui,yuio],
        [53,yop,amort,yuyr,whpr,oipu],
        [54,iqw,amort,uiop,iopa,iops],
	    [55,ish,amort,opas,pasd,asdf],
	    [56,spi,amort,sdfg,dfgh,fghj],
	    [57,xzs,amort,ghjk,hjkl,dedo],
	    [58,dedo,amort,endme,helpe,war],
	    [59,bvcx,amort,yjyj,hjhj,phph],
	    [60,epo,amort,rout,roui,0]],
	    
        columns = ['Cuota','Saldo','Amortizacion','Intereses','Valor Cuota ','Saldo final'])
    print(df)

o = input("A cuantos años sera el prestamo, hasta 5 años")
r =int(o)

if r==1:                      #este pedazo, define que metodo llamar en funcion de los años en los que este el prestamo
    periodo1()
elif r==2:
    periodo2()
elif r==3:
    periodo3()
elif r==4:
    periodo4()
elif r==5:
    periodo5()    
else:
    print("el numero de años debe estar entre 1 y 5")

j=tasames*12 #j es la tasa de interes efectivo anual
if j >28.55: # el condicional se activa cuando se supera la tasa de usura
    print("La tasa de interes esta por encima de la tasa de usura")
