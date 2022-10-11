import sqlite3
# import appDetails
from flask import Flask, render_template,redirect,request
import json,requests
from support import get_data as get_data
from support import get_issue_data as get_issue_data
# from data import data
# creating the flask app
app = Flask(__name__)





data = {
    "Anirudh":['vn.selly', '1217507712', 'com.idevspro.author.customers', 'com.fab.personalbanking', 'com.zingbusbtoc.zingbus', 'com.ht.ottplay', 'com.kriptrade.mobile', '1225034537', '749133753', 'com.goodluck777.panther', '1274924764', 'ae.etisalat.smiles', 'com.monsterindia.seeker.views', '1535521299', 'tv.sweet.player', 'com.centraldepartment.app', 'com.jago.digitalBanking', '889910218', 'com.prudential.pulse.onepulse', 'com.zipcarapp', 'ru.ritmmedia.yappy', 'com.app.ketitik.ketitik', 'com.travel.almosafer', 'fit.cure.android', 'com.ciceksepeti.lolaflora', '518158653', 'kr.goodchoice.abouthere', 'com.igs.mjstar31', 'com.disrapp.coinkeeper3', 'com.mcdonalds.mobileapp', 'za.co.travelstart.flapp', 'com.actify', '1471639720', 'com.williamsinteractive.jackpotparty', '1503482896', 'jp.co.rakuten.fashionAndroid', 'com.square_enix.android_googleplay.FFBEWW', 'com.app.balaan.balaanboutique', 'com.pozitron.hepsiburada', '1591396836', '1527156320', 'io.chatyapp'],
    "Aniket":['com.joinroot.root', 'in.swiggy.android', 'com.carshering', '523106486', 'com.bharatmatrimony', 'com.fastrunkitchen', 'com.shopee.vn', 'com.rynatsa.xtrendspeed', 'com.showtimeapp', 'com.neowiz.games.poker', 'com.mobile.legends', 'com.ssk.android', 'jp.wifishare.townwifi', 'com.bitoasis', 'com.intermiles.app', '1494139203', 'com.mfine', '531324961', '1300116604', 'com.applications.lifestyle', '1163514668', 'kr.co.kbc.cha.android', 'com.app.danube', 'com.airlive.miya', 'ru.start.androidmobile', 'com.gaana', '1566301002', 'com.shopee.th', 'com.gshopper.gapp', 'com.lulu.luluone', 'com.mosaicwellness.manmatters', 'com.indiaBulls', '331177714', 'my.com.goshop.app', 'com.boomegg.nineke', 'com.sabiamedia.riseup', 'com.gotchosen.influencers', 'com.etoro.openbook', 'com.playspare.watersort3d', 'com.weedmaps.app.android', 'com.socialswag.app', 'com.goodok.mts', 'kr.co.sincetimes.gxhgnew', '1078997450', '1158877342', 'com.aaptiv.android', '1055590420', 'com.bandagames.mpuzzle.gp', 'com.tejimandi.android', 'com.qidian.Int.reader', '1560996072', 'com.avail.easyloans.android', 'co.gradeup.android', 'com.expertoption', 'com.zoomcar', 'com.vng.tanomg3q', 'com.kreditpintar', 'com.squats.fittr', 'com.osn.go', 'com.solagame.zhvn.an', 'com.zodiactouch', '862390640', '1008719792', 'com.audible.application', '1051208330', '350189835', 'in.medibuddy', 'com.didiglobal.passenger', 'app.crazyloop.appsuccess', '829587759', 'in.amazon.mShop.android.shopping'],
    "Shrey":['com.belongtail.belong', 'com.algorythma.retail.prod', 'com.dreame.reader', 'com.bosco.boscoApp', '1498302242', 'com.nextdoor', 'com.akode.tosla', '1393913947', '744361908', '1439041310', '1401500803', '1153808931', 'com.igs.TMD', 'com.kwai.video', 'com.scbabacus.l2020', 'com.adidas.app', 'com.jumia.android', 'com.treebo.starscream', 'com.machipopo.media17', 'in.india.upi.flexpay', 'la.manzana_verde_app', 'com.snapdeal.main', 'com.theentertainerme.entertainer', 'com.akinon.samsung', 'com.localqueen', '784389203', 'com.radio.pocketfm', 'com.bitso.wallet', 'com.netway.phone.advice', 'com.priceminister.buyerapp', 'com.gudangada.gudangada', 'com.superplaystudios.dicedreams', 'com.gzone.yyvi', 'com.fordeal.android', 'com.epic.docubay', 'com.latto.tv.dogtv', 'com.bomenas.baximo', 'com.grabtaxi.passenger', 'com.univision.prendetv', 'me.dailymeal.main', 'com.scsoft.boribori', '907394059', '1493956050', 'com.fastbanking', 'com.merqueo', 'co.tslc.cashe.android', '1268959718', 'com.bitbnspay', 'kr.co.teamblind.bleet', '1486135528', 'com.axiaodiao.melo', 'org.fxclub.libertex', 'com.ahamove.user', 'com.astrotalk', 'tech.fplabs.score', 'com.valorem.flobooks', 'com.liveperson.kasamba.android', 'com.phrendly', 'io.chingari.app', 'com.shopping.limeroad', 'com.mashreq.NeoApp', 'com.fondeadora.bank', 'com.gma.water.sort.puzzle', 'com.planetart.fpfr', 'com.zoodel.kz', 'com.paymaya', 'com.topenland', 'com.growthunit.palace', 'com.boyaa.enginetaiwanqp.main', 'io.attabot.app.paymeindia', 'hk.easyvan.app.client', 'rgyan.rgyan', 'com.stormgain.mobile', '1261770407', 'com.dobai.kis', 'tv.abema'],
    "Jitendra":['1440611965', '710375963', 'com.mobile.pomelo', 'com.bplus.vtpay', 'com.coindcx.btc', 'com.everplay.music.app', 'br.com.vivo.vivoeasy', '1196302015', 'com.my.defense', 'com.saranyu.shemarooworld', 'com.amazon.mShop.android.shopping', 'com.theporter.android.customerapp', '1460593315', '1002320913', 'com.vuclip.viu', '991673877', 'com.coinswitch.kuber', 'com.dd.doordash', 'kr.co.lgfashion.lgfashionshop.v28', 'com.theepochtimes.news', '394685685', 'com.app.xxrideuser', '297606951', 'com.flipkart.shopsy', 'com.tinder', 'com.yaari', 'com.Plus500', '1462195529', '1437231181', '905953485', 'au.com.bws', 'com.vogo.android', '326861451', 'com.acciona.mobility.app', 'com.topclass.audiolive', '530488359', '750823886', 'ru.filit.mvideo.b2c', 'com.edamama.app', 'br.com.intermedium', 'com.rootbridge.ula', 'com.giottus.giottus_mobile', 'com.ocb.omniextra', '640360962', 'com.prodege.swagbucksmobile', 'com.dhan.live', 'id.moxa', 'com.phonepe.app', '1573112964', 'com.ss.android.ugc.trill', 'com.nirafinance.customer', 'com.clickastro.freehoroscope.astrology', 'com.balancehero.truebalance', '804641004', '1090987006', 'com.apalon.weatherradar.free', 'com.bukuwarung', '631927169', 'com.mox.app', 'com.creditsesame', 'com.pandats.evest', 'premom.eh.com.ehpremomapp', '1608184028', 'com.creativeinnovations.mea', 'mop.thglob.glaoebxdwesa', 'bajajfinserv.in.hrx.app', 'com.maiz.tangdoo', 'com.aia.rn.th.dp01', '1500326655', 'de.wetteronline.wetterapp'],
    "shreya":['com.doradogames.conflictnations.worldwar3', '1054302942', 'in.workindia.hireindia', 'com.mdf.repsol', 'com.qustodio.family.parental.control.app.screentime', '1471506070', 'com.viu.phone', 'in.burgerking.android', '1458102898', 'fr.youboox.mobile', 'com.traveloka.android', '1575135643', 'com.YsoCorp.NinjaHands', 'com.boloindya.boloindya', 'br.com.wine.app', 'vn.com.techcombank.bb.app', 'ru.utkonos.android.utkonoid', 'com.playmgmcasino.nj', '1585419012', 'com.cocacola.app.cee', 'company.coinpop.coinpop', 'com.julofinance.juloapp', 'get.lokal.localnews', 'com.dc.gok.google', 'com.generalmills.btfe', 'ajaib.co.id', '1403334281', 'com.tokopedia.tkpd', 'com.kobobooks.android', 'apms.apro.rush', 'com.trenbe.trenbehybrid', 'zero.finance.instantcash', '1514005355', 'com.aswat.carrefouruae', '1282962703', 'com.joyreading.wehear', 'coinone.co.kr.official', '1322399438', 'de.tchibo.app', 'com.fusionmedia.investing', 'net.bitburst.cryptobull', 'com.dreamplug.androidapp', 'com.ataexpress.tiklagelsin', 'id.maucash.app', 'com.lionsgateplay.videoapp', 'com.ashleymadison.mobile', 'com.mecl.la3eb', 'br.com.bancobmg.bancodigital.atletico', '1098083916', 'ru.sportmaster.app', '1558331986', 'com.nosmk.burgerking', 'ru.more.play', '1423221955', '1450978468', 'com.threesixteen.app', '928866584', 'com.exness.android.pa', 'com.ada.astrapay', '1133463693', 'connectiq.miles.app', 'com.wingloryinternational.mydailycash', '1474068436', '1352398887'],
    "Deepak":['id.astra.adp.movic', 'de.clark.app', 'ae.ahb.digital', 'com.trafficsource.nodepositbonusescom', '1022831885', 'com.cleartrip.android', 'com.sisal.sisalpay', 'ru.x5.perekrestok.darkstore', 'com.dsfgland.goat', 'com.robokiller.app', 'br.com.meutudo', '1463510745', 'com.dbs.in.digitalbank', 'com.photobook.android', 'com.survjun', '347000153', 'com.unionbankph.online', 'com.eterno', 'deezer.android.app', 'com.playmgm.nj.sports', 'com.iqoption', 'com.homingos.ar', '1375736043', 'zebpay.Application', 'com.minuet.byapps', '288113403', 'com.amazon.mp3', 'com.faces.androidapp', 'in.product.salary', 'com.kilogroup.ketocycle', 'com.ykb.android', 'com.policybazaar', 'com.atlasvpn.free.android.proxy.secure', 'com.linkdokter.halodoc.android', '1017261655', 'sports.caliente.mx.calientedeportes', 'ph.loans.mobile', 'www.undostres.com.mx', 'com.cashkarma.app', 'com.ncsoft.lineagew', 'com.defacto.android', 'com.kakaoent.kakaowebtoon', 'fr.telemaque.voyance', '909302093', '1400220482', '1486214495', 'com.perkwizmobile.prod', 'com.eterno.shortvideos', '1023721594', 'vng.game.gunny.mobi.classic.original', '1501720596', 'taxi.android.client', 'com.convert.app', 'vn.fimplus.app.and', '1592446684', '1479696509', 'com.lanterns.btaskee', '693137280', 'com.lezhin.comics', 'ru.alfadirect.app', 'com.indodana.app', 'my.com.myboost', '1569102341', 'com.conceptivapps.blossom', 'com.octafx', '1611276680'],
    "hitesh":['com.zain.pay', '1136298377', 'kr.co.fitpet', 'com.fugo.wow', 'com.greencar', 'com.noon.buyerapp', 'com.avatrade.mobile', 'com.rupeeredee.app', 'vn.kredivo.android', 'com.jar.app', '884043462', 'com.mediapark.rbm', 'com.innofinsolutions.lendenclub.lender', 'com.raizen.acelera', 'mx.com.procesar.aforemovil.nuevosura', '626805470', 'com.dealshare', '1074866833', 'vn.com.paysmart', 'ru.hoff.app', 'com.mediawill.findalljob', '1577168919', 'com.zvooq.openplay', 'com.pegipegi.android', '771946428', 'com.koinworks.app', 'com.drop.loyalty.android', 'com.withyotta.yotta', 'com.missjulie.homedesign', 'blibli.mobile.commerce', '1288441708', 'com.smallcase.android', '1568784560', 'com.earlysalary.android', 'com.monawa.giwon', '594506418', 'com.kreditbee.android', 'com.healthsignz.consumer.oliva', '719972451', 'com.xxqy.gs', '1367232195', 'com.globalegrow.app.dresslily', 'com.westernunion.moneytransferr3app.ae', 'co.go.fynd', 'com.taskbucks.taskbucks', '1156964115', 'com.ticno.olymptrade', 'com.nextbillion.groww', '1557241541', 'com.lightinthebox.android', '1435773823', 'com.myglamm.ecommerce', 'br.com.projetopolishop.mobile', '458627086', 'com.cartlow.android', '1399907836', 'com.innofinsolutions.instamoney', 'com.tpb.mb.gprsandroid', '1086466469', 'com.mason.wooplus', 'com.trastra.mobile', 'com.nojoto.cinco', 'com.rummycircle.lite.android', '1600014978', 'com.muna.lively'],
    "shraddha":['com.brightcapital.app', 'com.clickbus.mobile', 'ahaflix.tv', 'com.unocoin.unocoinwallet', 'com.apollo.patientapp', 'com.msf.kbank.mobile', 'com.spinny.consumer', 'com.yinshan.program.banda', 'ru.migcredit.ma', 'com.byu.id', '1492707205', 'com.okcupid.okcupid', '1459024696', '877286524', 'com.niyo.equitassavingsaccount', 'in.startv.hotstar', '549837264', 'com.viewlift.hoichoi', 'com.kudu.androidapp', '301987699', '1467451327', 'com.NHNEnt.MSudda', 'com.lamoda.lite', 'com.banggood.client', 'com.nhnent.pokerclassic', '1531713996', '1141857583', 'com.healthifyme.basic', 'com.surfshark.vpnclient.android', '1105812423', '1212024125', '996325726', 'com.btckorea.bithumb', 'br.com.bancopan.cartoes', 'app.snoop', 'com.niyo.sbm', '1018207358', 'com.kwai.bulldog', 'net.mbc.shahid', 'com.bybit.app', '1457173515', 'ru.beeline.services', '414461255', 'com.bnb.paynearby', 'com.netease.dhhzlggkr', 'com.unacademyapp', 'com.landmarkgroup.maxstores', 'com.fiverr.fiverr', 'kr.co.monoplatform.whistle', 'kr.co.captv.pooqV2', 'com.amazon.sellermobile.android', 'kr.co.richnco.goodrich', 'com.phablecare', '1263814273', 'com.intech.c66app', 'com.tatadigital.tcp', 'com.woowahan.vn.baemin', '589328270', 'com.wajual', 'ru.sbcs.store', '1140806268', 'com.psafe.msuite', 'bwin.de.sports', '1491590039', 'com.cogaming.comeoncasino.dga'],
    "praveen":['com.Dominos', 'com.betterhalf', 'com.demaecan.androidapp', 'com.akbank.android.apps.akbank_direkt', 'com.licious', 'com.paysend.app', 'com.playtimekarma.app', 'com.getbux.android.stocks', '592978487', 'io.cleanfox.android', 'xyz.be.cake', '457792991', '1184577212', 'mx.com.bancoazteca.bazdigitalmovil', '1011085984', '1021268294', 'com.planetart.fpuk', 'com.byte.customer', '879915134', 'com.gopaysense.android.boost', '749083919', 'com.mrd.food', '1317811457', 'com.byjus.thelearningapp', 'ru.mts.music.android', '988141624', 'com.careem.acma', 'com.dunzo.user', 'com.pointsbet.app', 'com.naviapp', 'com.koo.app', 'com.fineappstudio.android.petfriends', 'com.inbox.clean.free.gmail.unsubscribe.smart.email.fresh.mailbox', 'com.canva.editor', 'com.pocketaces.locostudio', '938506958', 'com.mbmobile', 'net.igapi.android.istegelsin', 'net.bitburst.easybucks', 'aptip.app', 'com.globe.gcash.android', 'com.bradesco', 'com.shopee.ph', '1487453649', 'com.netmarble.skrv', 'com.app.rehlat', 'com.dhgate.buyermob', 'com.carrefoursa.ecommerce', 'com.btg.pactual.digital.mobile', 'com.igg.android.lordsmobile', '664973122', '1507757760', '319557427', 'ru.zdravcity.app', 'com.bankofhodlers.mobile', 'com.zzkko', '541492660', 'com.nolbal.nolbal', 'com.myntra.android', 'com.zap.surveys', 'com.il.mcdelivery', 'xyz.be.customer', 'com.surveysampling.mobile.quickthoughts', 'com.imaginbank.app', '1085470991'],
    "sanil":['com.interfocusllc.patpat', '966740633', '785385147', '1511043796', 'com.zeptoconsumerapp', 'com.garanti.cepsubesi', 'ru.ostin.android.app', 'icici.lombard.ghi', '323678768', 'com.zalora.android', 'com.sa.maana', 'com.acko.android', 'com.herofincorp.simplycash', 'com.lazada.android', 'com.oyo.consumer', 'in.workindia.nileshdungarwal.workindiaandroid', 'com.app.abhibus', 'net.bitburst.pollpay', '905869418', 'com.notissimus.allinstruments.android', 'com.arammeem.android.apps.toyou', 'com.mobile.justmop', 'com.okinc.okex.gp', 'com.nexon.kart', '1393945933', 'com.tmon', '1554981586', 'com.toluna.webservice', 'net.ib.android.smcard', '1270161188', 'com.cmcm.uangme', 'qureka.live.game.show', 'com.nhnent.Qpoker', 'com.borrowell.strangelove', 'com.ticker.android.cryptowire', 'kr.co.finda.finda', 'com.akbank.android.apps.axess', 'com.kotakcherry.app', 'com.kth.kshop', '1100171914', 'com.unicostudio.braintest', 'com.youhodler.youhodler', 'com.app.smytten', '560516360', '1107705982', 'com.aranoah.healthkart.plus', 'com.pizzahut.phd', 'ru.kfc.kfc_delivery', 'com.graymatrix.did', 'com.simpl.android', 'air.com.ace2three.mobile', '713206884', '777645417', 'ru.burgerking', 'com.appkarma.app', 'com.stc.xplay', 'com.parimatch.pmuk014', 'ru.lenta.lentochka', 'com.GMA.Ball.Sort.Puzzle', 'com.reglobe.cashify', 'com.phocket', 'com.mpokket.app', '1469351696', 'com.zhiliaoapp.musically']
}


@app.route('/')
def Home():

    ref = {'test':'0','Anirudh':[],'Aniket':[],'Shrey':[],'Jitendra':[],'shreya':[],'Deepak':[],'hitesh':[],'shraddha':[],'praveen':[],'sanil':[],'checked':[],'app_data':{}}

    con = sqlite3.connect("working.db")  
    con.row_factory = sqlite3.Row
    cur = con.cursor()  
    quer = que  ="SELECT *  FROM 'packageId'"
    quer2 = que  ="SELECT *  FROM 'checkedid'"
    cur.execute(quer)
    tmp_lis = cur.fetchall()
    lis = []
    for a in tmp_lis:
        lis.append(a[0])
    cur.execute(quer2)
    rows1 = cur.fetchall()
    list2 = [dict(ix) for ix in rows1]
    lis3 = []
    # print(list2)
    for i in list2:
        tm = i.get('PackageId')
        lis3.append(tm)
    # print(lis3)
    for z in lis3:
        if z in lis:
            # print("Present")
            pass
        else:
            # print("Not in")
            # print(len(lis))
            lis.append(z)
    # print(lis)
    for x in lis:
        i = x
        if i in data.get('Anirudh'):
            ref['Anirudh'].append(i)
            # if i in tm:
            #     ref[i] = "True"
        elif i in data.get('Aniket'):
            ref['Aniket'].append(i)
        elif i in data.get('Shrey'):
            ref['Shrey'].append(i)
        elif i in data.get('Jitendra'):
            ref['Jitendra'].append(i)
        elif i in data.get('shreya'):
            ref['shreya'].append(i)
        elif i in data.get('Deepak'):
            ref['Deepak'].append(i)
        elif i in data.get('hitesh'):
            ref['hitesh'].append(i)
        elif i in data.get('shraddha'):
            ref['shraddha'].append(i)
        elif i in data.get('praveen'):
            ref['praveen'].append(i)
        elif i in data.get('sanil'):
            ref['sanil'].append(i)
        else:
            pass
    for j in lis:
        if j in lis3:
            # print("added")
            ref['checked'].append(j)
        else:
            pass
    
    ref['app_data'] = get_data(lis)
    print("*"*100)
    print( get_issue_data(lis))
    print("*"*100)
    ref['issue_data'] = get_issue_data(lis)
    

    return render_template('games.html',out_data=ref)




def get_db_connection():
    conn = sqlite3.connect('working.db')
    # conn.row_factory = sqlite3.Row
    conn.execute("create table IF NOT EXISTS packageId (PackageId TEXT PRIMARY KEY)")
    conn.execute("create table IF NOT EXISTS checkedid (PackageId TEXT PRIMARY KEY, status TEXT)")
    conn.execute("create table IF NOT EXISTS Issue (PackageId TEXT PRIMARY KEY, Issue TEXT)")

  
# print("Table created successfully")  
    return conn


@app.route('/d')
def refresh():
    ref = {'test':'1'}
    url = "https://affise.c2a.in/app_working_link.php?fetch_campaigns=List+Campaigns"
    res = requests.get(url)
    t = json.loads(res.text)
    lis = t.get('suggestedApps')

    get_db_connection()
    try:
        con = sqlite3.connect("working.db")  

        con.execute('DELETE FROM packageId')
        con.commit()
    except:
        pass
    insert_rows = []
    for k in lis:
        to_append = "('"+k+"')"
        if to_append not in insert_rows:
            insert_rows.append(to_append)
    if len(insert_rows) > 0:
        values = ', '.join(map(str, insert_rows))
        sql = "INSERT INTO packageId VALUES {}".format(values)
        # print(sql)
        cur = con.cursor() 
        cur.execute(sql)  
        con.commit()
    return redirect('/')

from flask_restful import reqparse

def parse_arg_from_requests(arg, **kwargs):
    parse = reqparse.RequestParser()
    parse.add_argument(arg, **kwargs)
    args = parse.parse_args()
    return args[arg]

@app.route('/datapost',methods=['GET','POST'])
def datapost():
    da = {}
    try:
        user = request.form['username']
        # print("find"*10)
        # print(user)
        # print("find"*10)
        con = get_db_connection()
        checked = "checked"
        # con.execute('DELETE FROM checkedid')
        id = "'"+user+"'"+",'"+checked+"'"
        sql = "INSERT INTO checkedid VALUES ("+id+")"
        # print(sql)
        cur = con.cursor() 
        cur.execute(sql)
        con.commit()
        da['hello'] = user
    except:
        pass
    return redirect('/')

@app.route('/datapostdelet',methods=['GET','POST'])
def datapostdel():
    da = {}
    try:
        user = request.form['username']
        # print("find"*10)
        # print(user)
        # print("find"*10)
        con = get_db_connection()
        # checked = "checked"
        # con.execute('DELETE FROM checkedid')
        id = "'"+user+"'"
        sql = "DELETE  FROM checkedid WHERE PackageId = "+id
        print(sql)
        cur = con.cursor() 
        print(cur.execute(sql))
        con.commit()
        da['hello'] = user
    except:
        pass
    return redirect('/')


@app.route('/getdata', methods=['GET','POST'])
def get_form_data():
    print("*"*100)
    refres = {}
    if request.method == 'GET':
            return render_template('my-form.html',out_data = refres)
    else:
        print(request.form)
        if request.form.get('name'):
            li = request.form['name']
            l2 = request.form.get('app_id')
            con = get_db_connection()
            # con.execute("create table IF NOT EXISTS Issue (PackageId TEXT PRIMARY KEY, Issue TEXT)")
            query = "SELECT PackageId FROM Issue WHERE PackageId ="+"'"+l2+"'"
            print(query)
            cur = con.cursor()
            cur.execute(query)
            con.commit()
            rows = cur.fetchall() 
            print(rows)
            print("A"*100)
            if len(rows) > 0:
                    sql1 = "UPDATE Issue SET  Issue = '"+str(li)+"' WHERE PackageId =  '{}'".format(l2)
                    print(sql1)
                    cur = con.cursor()
                    cur.execute(sql1)  
                    con.commit()
                
            else:
                sql = "('"+l2+"','"+str(li)+"')"
                sql2 = "INSERT INTO Issue VALUES {}".format(sql)
                print(sql2)
                cur = con.cursor() 
                cur.execute(sql2)  
                con.commit()
    return redirect('/')
    
    






if __name__ == '__main__':
    app.run(debug = True)
