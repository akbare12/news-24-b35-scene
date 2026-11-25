import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png'); SB='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'; SN='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; SNB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(s,b=False,serif=False):
    try: return ImageFont.truetype((SB if serif else SNB) if (b or serif) else SN, s)
    except Exception: return ImageFont.load_default()
def T(d,x,y,s,f,fill='#111111',anchor='la'): d.text((x,y),s,font=f,fill=fill,anchor=anchor)
def WR(d,x,y,w,s,f,fill='#222222',lh=None):
    words=s.split(); lines=[]; cur=''
    for wd in words:
        t=(cur+' '+wd).strip()
        if d.textlength(t,font=f)<=w: cur=t
        else: lines.append(cur); cur=wd
    if cur: lines.append(cur)
    lh=lh or int(f.size*1.25)
    for i,ln in enumerate(lines): d.text((x,y+i*lh),ln,font=f,fill=fill)
    return y+len(lines)*lh
def CHIP(d,x,y,s,c):
    f=F(7,True); w=int(d.textlength(s,font=f))+10; d.rounded_rectangle([x,y,x+w,y+13],radius=3,fill=c); d.text((x+5,y+1),s,font=f,fill='white'); return x+w+4
def BAR(d,x,y,w,parts):
    xx=x
    for label,n,col in parts:
        sw=w*n/38; d.rectangle([xx,y,xx+sw,y-1+22],fill=col); T(d,xx+4,y+4,f'{label} {n}',F(8,True),'white'); xx+=sw
    return xx
im=Image.new('RGB',(W,H),'#f7f1e3'); d=ImageDraw.Draw(im); d.rectangle([0,0,W,7],fill='#b01e24')
T(d,10,12,'THE WORLD ON ONE DAY',F(10,True),'#b01e24'); T(d,1014,12,'38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS',F(10,True),'#111111',anchor='ra')
T(d,10,28,'Tuesday 24 November 2026',F(31,True,True),'#111111'); T(d,1014,44,'TUESDAY',F(11,True),'#b01e24',anchor='ra')
T(d,10,64,'Houthi drone hits Riyadh tower again  \u00b7  Chen Jining probed in Shanghai  \u00b7  Huawei guilty on 10 of 12 counts.',F(11,True,True),'#b01e24')
BAR(d,10,84,1004,[('Europe',9,'#1f4e79'),('Middle East',8,'#b01e24'),('Asia',8,'#c07a00'),('Africa',2,'#2e7d32'),('Americas',7,'#6a4a9e'),('World/Space',4,'#0f766e')])
d.rectangle([10,110,1014,134],fill='#1f2937'); T(d,18,113,'THE DAY IN UTC',F(9,True),'#fbbf24')
utc=[('00:52','Megaspeed blacklisted'),('02:15','NATO vows space defence'),('08:16','Hanoi blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
xx=130
for tm,ev in utc:
    T(d,xx,113,tm,F(8,True),'#fbbf24'); T(d,xx,122,ev,F(7),'#f7f1e3'); xx+=112
d.rectangle([10,138,1014,162],fill='#fff8e1',outline='#c07a00'); T(d,18,141,'THE DAY IN NUMBERS',F(9,True),'#b01e24')
nums=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow, first over 50k'),('+8.99%','Taiex record'),('25','killed / missing, Yemen'),('26','Cikande fire toll')]
xx=170
for n,lab in nums:
    T(d,xx,140,n,F(13,True),'#111111'); T(d,xx,154,lab,F(7),'#444444'); xx+=142

def HERO(x,y,w,scene):
    d.rectangle([x,y,x+w,y+218],outline='#111111',width=1,fill='white'); scene(x+1,y+1,w-2,112); return x+1,y+116,w-2
def SC1(x,y,w,h):
    d.rectangle([x,y,x+w,y+h],fill='#0b1e3a'); d.ellipse([x+w-52,y+10,x+w-22,y+40],fill='#f5d76e')
    for bx,bw,bh in [(0,42,62),(46,34,84),(84,40,58),(210,44,70),(258,36,54)]: d.rectangle([x+bx,y+h-bh,x+bx+bw,y+h],fill='#1e3a5f')
    for bx,bw,bh in [(0,42,62),(46,34,84),(84,40,58),(210,44,70),(258,36,54)]:
        for wy in range(y+h-bh+8,y+h-6,12):
            for wx in range(x+bx+6,x+bx+bw-6,10): d.rectangle([wx,wy,wx+4,wy+5],fill='#f5d76e')
    d.polygon([(x+128,y+h-108),(x+128,y+h-6),(x+196,y+h-6),(x+196,y+h-108)],fill='#274b73'); d.polygon([(x+128,y+h-108),(x+162,y+h-112),(x+196,y+h-108)],fill='#3b6ea5')
    for wy in range(y+h-100,y+h-10,14):
        for wx in range(x+136,x+188,12): d.rectangle([wx,wy,wx+6,wy+7],fill='#ffd166')
    d.ellipse([x+205,y+18,x+245,y+52],fill='#9aa5b1'); d.ellipse([x+222,y+30,x+262,y+58],fill='#c0392b'); d.ellipse([x+240,y+8,x+268,y+30],fill='#e67e22'); d.polygon([(x+150,y+22),(x+168,y+30),(x+150,y+38),(x+132,y+30)],fill='#222222'); d.rectangle([x+148,y+28,x+152,y+52],fill='#222222')
def SC2(x,y,w,h):
    d.rectangle([x,y,x+w,y+h],fill='#f3d9c8'); d.rectangle([x,y+h-26,x+w,y+h],fill='#2e7d32'); d.rectangle([x+18,y+34,x+w-18,y+h-26],fill='#8e1b1b'); d.rectangle([x+30,y+22,x+w-30,y+40],fill='#5c0f0f'); d.text((x+w//2,y+25),'SHANGHAI',font=F(11,True),fill='#f5d76e',anchor='ma')
    for cx in range(x+44,x+w-40,38): d.rectangle([cx,y+52,cx+12,y+h-26],fill='#d8c9a3')
    d.rectangle([x+130,y+52,x+196,y+h-26],fill='#3a0d0d'); d.ellipse([x+156,y+66,x+170,y+80],fill='#f5d76e')
    d.rectangle([x+22,y+h-52,x+118,y+h-8],fill='white',outline='#111111'); d.rectangle([x+208,y+h-52,x+304,y+h-8],fill='white',outline='#111111')
    for i,yy in enumerate(range(y+h-46,y+h-12,8)): d.line([x+30,yy,x+110,yy],fill='#333333',width=1); d.line([x+216,yy,x+296,yy],fill='#333333',width=1)
    d.ellipse([x+236,y+h-46,x+268,y+h-16],outline='#b01e24',width=2); T(d,x+252,y+h-38,'CCDI',F(8,True),'#b01e24',anchor='mm')
def SC3(x,y,w,h):
    d.rectangle([x,y,x+w,y+h],fill='#dbe7f3'); d.rectangle([x+14,y+30,x+w-14,y+58],fill='#e8e2d2',outline='#111111'); d.polygon([(x+8,y+32),(x+w//2,y+6),(x+w-8,y+32)],fill='#1f4e79')
    for cx in range(x+36,x+w-36,52): d.rectangle([cx,y+58,cx+16,y+h-22],fill='#f7f1e3',outline='#111111')
    d.rectangle([x+14,y+h-22,x+w-14,y+h-12],fill='#1f4e79'); T(d,x+w//2,y+66,'HUAWEI',F(15,True),'#c0392b',anchor='ma')
    d.rectangle([x+210,y+84,x+292,y+96],fill='#5b3a1e'); d.rectangle([x+246,y+84,x+258,y+104],fill='#5b3a1e'); d.rectangle([x+206,y+78,x+296,y+86],fill='#7a4a22'); d.rectangle([x+24,y+92,x+120,y+104],fill='white',outline='#111111'); T(d,x+72,y+94,'10 / 12',F(9,True),'#111111',anchor='mm')
hx=[10,348,686]
for i,(sc,kick,chip,chipc,head,deck,src) in enumerate([(SC1,'1  RIYADH \u00b7 MIDDLE EAST','CONFIRMED','#2e7d32','Houthi drone hits Riyadh\u2019s tallest tower again, 11 hurt','A Houthi drone struck the PIF tower, Riyadh\u2019s tallest, for the second time in a week. Eleven people were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.','(Saudi officials \u00b7 14:27 UTC)'),(SC2,'2  SHANGHAI \u00b7 ASIA','OFFICIAL','#1f4e79','China probes Shanghai party chief Chen Jining','Chen Jining, 62, is probed for \u201cserious violations\u201d by the CCDI. He is the fourth Politburo member to fall under investigation this year.','(CCDI)'),(SC3,'3  NEW YORK \u00b7 US / TECH','CONFIRMED','#2e7d32','Huawei guilty on 10 of 12 counts','A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering. Sentencing is set for Sep 2027, and Huawei will appeal.','(US court \u00b7 20:41 UTC)')]):
    X,Y,Wd=HERO(hx[i],166,328,sc); T(d,X,Y,'',F(9,True)); T(d,X,Y+2,kick,F(9,True),'#b01e24'); CHIP(d,X,Y+18,chip,chipc); T(d,X+62,Y+18,src,F(7),'#555555'); WR(d,X,Y+34,Wd-4,head,F(13,True,True),'#111111',lh=15); WR(d,X,Y+68,Wd-4,deck,F(9),'#222222',lh=11)

def CSC(i,x,y,w,h):
    cols=['#0b1e3a','#2e7d32','#0f766e','#1f4e79','#b01e24','#6a4a9e','#c07a00','#1f2937','#8e5b2e','#5b3a1e']; d.rectangle([x,y,x+w,y+h],fill=cols[i%10])
    if i==0: d.ellipse([x+w-30,y+4,x+w-8,y+22],fill='#f5d76e'); d.polygon([(x+20,y+16),(x+34,y+20),(x+20,y+24),(x+8,y+20)],fill='#111111')
    if i==1: d.polygon([(x+w//2-16,y+6),(x+w//2+16,y+6),(x+w//2+8,y+22),(x+w//2-8,y+22)],fill='#f5d76e'); d.rectangle([x+w//2-4,y+22,x+w//2+4,y+26],fill='#f5d76e')
    if i==2: d.rectangle([x+14,y+12,x+w-14,y+22],fill='#e8e2d2'); d.rectangle([x+w//2-3,y+2,x+w//2+3,y+12],fill='#e8e2d2')
    if i==3: d.line([x+6,y+22,x+w//3,y+12,x+2*w//3,y+16,x+w-6,y+4],fill='#fbbf24',width=3)
    if i==4: d.rectangle([x+12,y+8,x+34,y+24],fill='#111111'); d.rectangle([x+40,y+8,x+62,y+24],fill='#333333'); d.rectangle([x+68,y+8,x+90,y+24],fill='#b01e24')
    if i==5: d.ellipse([x+16,y+8,x+44,y+20],fill='#9aa5b1'); d.rectangle([x+44,y+14,x+70,y+18],fill='#9aa5b1')
    if i==6: d.rectangle([x+18,y+10,x+w-18,y+22],fill='#e8e2d2'); d.rectangle([x+w//2-14,y+14,x+w//2+14,y+18],fill='#b01e24')
    if i==7: d.polygon([(x+16,y+24),(x+30,y+8),(x+44,y+24)],fill='#f5d76e'); d.polygon([(x+60,y+24),(x+74,y+8),(x+88,y+24)],fill='#e8e2d2')
    if i==8: d.rectangle([x+20,y+12,x+70,y+22],fill='#e8e2d2'); d.ellipse([x+30,y+20,x+38,y+26],fill='#111111'); d.ellipse([x+56,y+20,x+64,y+26],fill='#111111')
    if i==9: d.polygon([(x+w//2-4,y+2),(x+w//2+4,y+2),(x+w//2+8,y+16),(x+w//2-8,y+16)],fill='#f7f1e3'); d.ellipse([x+w//2-14,y+16,x+w//2+14,y+24],fill='#fbbf24')
CARDS=[(4,'ZAPORIZHZHIA \u00b7 EUROPE / WAR','REPORTED','#5b6abf','Russian attacks kill 9 across Ukraine in a day','Nine were killed and 81 hurt in a day. Russia launched 96 drones and 73 were shot down.','(Kyiv \u00b7 11:37 UTC)'),(5,'CAS \u00b7 AFRICA / SPORT','OFFICIAL','#1f4e79','CAS hands Senegal back the AFCON title','CAS restored the Africa Cup title to Senegal after Morocco forfeited 3-0, making it 1-0.','(CAS)'),(6,'HORMUZ \u00b7 MIDDLE EAST','REPORTED','#5b6abf','IRGC attacks container ship in Hormuz','A container ship was attacked in Hormuz at 18:58 UTC and its navigation was disabled.','(UKMTO)'),(7,'NEW YORK \u00b7 WORLD / MARKETS','CONFIRMED','#2e7d32','Dow closes above 50,000 for the first time','The Dow closed at 50,018, its first finish above 50,000, while the Taiex rose 8.99 percent.','(Market close)'),(8,'REDMOND \u00b7 WORLD / TECH','REPORTED','#5b6abf','Microsoft declares \u2018Code Red\u2019 after historic outage','After a 24-hour Exchange Online outage, Microsoft set a one-hour global recovery target.','(Reuters)'),(9,'ESKISEHIR \u00b7 EUROPE','REPORTED','#5b6abf','Turkish military helicopter crash kills 5','A Turkish military AS-532 helicopter crashed in Eskisehir, killing five people at 19:52 UTC.','(Turkish officials)'),(10,'CARTAGENA \u00b7 AMERICAS','REPORTED','#5b6abf','Supermarket hostages: 25 held in Cartagena','Twenty-five were held hostage in a Cartagena supermarket and five elderly women were freed.','(Colombia officials \u00b7 17:35 UTC)'),(11,'ADEN \u00b7 MIDDLE EAST','REPORTED','#5b6abf','Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden in Yemen, wires reported at 16:51 UTC.','(Wires)'),(12,'LAHJ \u00b7 MIDDLE EAST','REPORTED','#5b6abf','Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes in Wadi Maabaq, Lahj, killed or left missing 25 people and wounded six.','(Yemeni officials \u00b7 10:42 UTC)'),(13,'JIUQUAN \u00b7 WORLD / SPACE','OFFICIAL','#1f4e79','China names first foreign astronaut for Tiangong','The Shenzhou-24 crew includes Muhammad Zeeshan Ali of Pakistan, the first foreign astronaut.','(CMSA)')]
for k,(n,kick,chip,cc,head,deck,src) in enumerate(CARDS):
    cx=10+(k%5)*202; cy=390+(k//5)*108; d.rectangle([cx,cy,cx+194,cy+104],outline='#111111',fill='white'); CSC(k-4,cx+1,cy+1,192,26); T(d,cx+5,cy+30,f'{n}  {kick}',F(7,True),'#b01e24'); CHIP(d,cx+5,cy+41,chip,cc); T(d,cx+62,cy+41,src,F(6),'#555555'); WR(d,cx+5,cy+56,184,head,F(9,True),'#111111',lh=10); WR(d,cx+5,cy+78,184,deck,F(7,True) if False else F(7),'#222222',lh=9)

T(d,10,610,'WORLD MAP \u2014 13 PINNED STORIES',F(10,True),'#111111'); T(d,1014,610,'Pins 3 + 7 share New York; pin 12 is offset from Aden.',F(7),'#555555',anchor='ra')
MX,MY,MW,MH=242,632,540,180
def LL(lon,lat): return MX+(lon+180)/360*MW, MY+(75-lat)/130*MH
d.rectangle([MX,MY,MX+MW,MY+MH],fill='#cfe3ee',outline='#111111')
NA=[(-168,66),(-140,70),(-125,72),(-110,73),(-95,80),(-85,70),(-80,73),(-65,60),(-55,47),(-70,42),(-75,35),(-80,26),(-85,30),(-90,20),(-95,18),(-105,22),(-115,28),(-125,40),(-140,60),(-165,60)]; SA=[(-80,10),(-60,8),(-50,0),(-35,-8),(-40,-20),(-48,-28),(-58,-35),(-70,-40),(-73,-50),(-70,-55),(-75,-35),(-80,-20),(-80,0)]; EU=[(-10,36),(-9,43),(0,50),(5,58),(10,58),(18,56),(23,60),(30,70),(40,68),(35,60),(30,45),(23,40),(15,38),(10,44),(0,43),(-2,37)]; AF=[(-17,15),(-10,30),(0,35),(10,37),(20,32),(30,31),(35,28),(43,12),(51,10),(48,0),(40,-10),(35,-20),(30,-30),(20,-35),(15,-28),(12,-18),(13,-5),(9,4),(-8,5),(-15,12)]; AS=[(40,68),(60,70),(80,73),(110,75),(140,72),(170,66),(178,65),(162,60),(158,52),(142,45),(140,38),(130,35),(127,33),(122,30),(120,25),(110,20),(105,10),(100,8),(95,15),(90,22),(85,20),(80,8),(77,8),(72,20),(65,25),(60,25),(55,26),(50,30),(48,30),(43,12),(40,55)]; AU=[(113,-22),(114,-30),(120,-34),(130,-32),(140,-38),(150,-37),(153,-27),(146,-19),(142,-11),(135,-12),(130,-13),(122,-17)]
for poly in [NA,SA,EU,AF,AS,AU]: d.polygon([LL(lo,la) for lo,la in poly],fill='#c9d6a8',outline='#5a6b3f')
for i,(lon,lat,dx,dy) in enumerate([(46.7,24.7,0,0),(121.5,31.2,0,0),(-74.0,40.7,0,0),(35.2,47.8,0,0),(-17.4,14.7,0,0),(56.0,26.5,0,0),(-74.0,40.7,16,-14),(-122.1,47.7,0,0),(30.5,39.8,0,0),(-75.5,10.4,0,0),(45.0,12.8,0,0),(44.9,13.0,16,12),(98.5,39.7,0,0)],start=1):
    px,py=LL(lon,lat); qx,qy=px+dx,py+dy
    if dx or dy: d.line([px,py,qx,qy],fill='#b01e24',width=1)
    d.ellipse([qx-8,qy-8,qx+8,qy+8],fill='#b01e24',outline='white',width=1); T(d,qx,qy-5,str(i),F(7,True),'white',anchor='ma')
T(d,10,636,'HOW TO READ',F(8,True),'#b01e24'); WR(d,10,650,220,'Red pins are stories 1\u201313. Europe 9, Middle East 8, Asia 8, Africa 2, Americas 7, World/Space 4. Pin 8 Redmond sits on the US west coast, below the Canada border.',F(8),'#222222',lh=11)
T(d,800,636,'PINNED',F(8,True),'#b01e24'); WR(d,800,650,214,'1 Riyadh  2 Shanghai  3 New York  4 Zaporizhzhia  5 Dakar  6 Hormuz  7 New York  8 Redmond  9 Eskisehir  10 Cartagena  11 Aden  12 Lahj  13 Jiuquan.',F(8),'#222222',lh=11)
T(d,10,816,'ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES',F(10,True),'#111111')
ALSO=['14 Ankara: Haftar visits Turkey for the first time.','15 London: UK sanctions Houthis + 4 officials.','16 Villavicencio: Car bomb injures 23.','17 Gaza: Israel kills Hamas internal security chief.','18 Baghdad: Iraq orders federal control of Kurdish oilfields.','19 Gaza: Meningitis epidemic alert; 272 cases in Oct.','20 DR Congo: Missing Cessna 208; rebels claim shootdown.','21 Hanoi: Hot-pot explosion kills at least 6.','22 Gulf of Finland: Ukraine hits Russian ship Sparta II.','23 Kuala Lumpur: Malaysia to return thousands of migrants.','24 Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ.','25 Dhaka: Hasina plans return on 16 Dec.','26 The Hague: 14 nations endorse ICJ Myanmar ruling.','27 Jakarta: Indonesia nominates 2 VP candidates.','28 Beijing: China sentences official Ma to death for spying.','29 Brussels: NATO vows defence against space threat.','30 Mexico City: El Chapo Isidro: US drone aided capture Fri 20 Nov.','31 San Salvador: Bukele names 3 soldiers killed in Haiti.','32 Ottawa: Pentagon rebukes Canada \u2014 only 41.9% of air fleet ready.','33 Washington: US adds Megaspeed to trade blacklist.','34 Kyiv: Zelensky urges Ukraine/Russia/US/Europe talks soon.','35 Ras Al Khaimah: UAE bus-truck crash kills 13.','36 London: England record 5,258 heat deaths in summer 2026.','37 Kourou: Ariane 6 lofts 36 Amazon satellites.','38 Cikande: Factory-fire toll rises to 26.']
for ci in range(3):
    for ri,txt in enumerate(ALSO[ci*9:(ci+1)*9]): T(d,10+ci*338,834+ri*11,txt,F(7),'#222222')
d.rectangle([10,932,1014,984],fill='#fde8e8',outline='#b01e24'); T(d,18,936,'DATE CHECK',F(9,True),'#b01e24'); WR(d,18,950,988,'Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov); Huang returns as Nvidia CEO (Mon 23 Nov); EU sanctions package 22 (Mon 23 Nov); COP31 ends with no deal (Sun 22 Nov); corvette Merkury sunk (Sat 22 Nov); El Chapo Isidro arrested (Fri 20 Nov); Cikande factory fire started (Sat 21 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC); MPR session picks VP (11 Dec); Huawei sentencing (Sep 2027); Hasina returns (16 Dec).',F(8),'#222222',lh=11)
T(d,10,990,'Sources: dailysummaryof.com/world/2026-11-24 \u00b7 Astrova News \u00b7 Horizon \u00b7 WSOC / AP \u00b7 Reuters \u00b7 CCDI \u00b7 CAS \u00b7 CMSA \u00b7 UKMTO.',F(7),'#444444'); T(d,10,1002,'CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side\u2019s claim. Scenes are drawn illustrations, not photographs.',F(7),'#444444')
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); im.save(OUT); print(OUT,im.size)
