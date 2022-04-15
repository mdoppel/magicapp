from click import password_option
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, logout_user, LoginManager, login_user, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import except_all, false
from config import Config
from forms import LoginForm, userRegistration
from datetime import date
from datetime import datetime 
from flask_sqlalchemy import SQLAlchemy
import json

#-------------------------------------
#Import Files

with open('AllPrintings.json', encoding='utf-8') as json_file:
    allprintresults = json.load(json_file)

with open('AllPrices.json', encoding='utf-8') as json_file:
    allpriceresults = json.load(json_file)    

#-------------------------------------
application = Flask(__name__)
application.config.from_object(Config)
login_manager= LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return users.query.get(int(id))

#Add Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
application.config['SECRET_KEY'] = 'magiceveryeverywhere'
db = SQLAlchemy(application)


class card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    set = db.Column(db.String(100))
    number = db.Column(db.String(100))
    foil = db.Column(db.String(100))
    UUID = db.Column(db.String(100))
    cardName = db.Column(db.String(100))
    cardRarity = db.Column(db.String(100))
    CKbuylistfoil = db.Column(db.String(100))
    CKretailfoil = db.Column(db.String(100))

class users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = false)
    email = db.Column(db.String(100), nullable = false, unique=True)
    password_hash = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
       self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash)

    def __repr__(self):
        return '<Name %r>' % self.name
  
#Home Route
@application.route("/")
def home():
    return render_template("home.html")




#Signup Route
@application.route("/signup/add", methods=['GET', 'POST'])
def signup():
    name = None
    form = userRegistration()
    if form.validate_on_submit():
        user = users.query.filter_by(email = form.email.data).first()
        if user is None:
            hashed_psw = generate_password_hash(form.password_hash.data, "sha256")
            user = users(name = form.name.data, email = form.email.data, password_hash=hashed_psw)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data=''
        form.email.data=''
        form.password_hash.data=''
        flash("User Added Successfully!")
        return render_template("login.html")
    return render_template("signup.html", form=form, name=name)

#Login Route
@application.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    form = LoginForm()
    if form.validate_on_submit():
        user = users.query.filter_by(email=form.email.data).first()
        if user:
            # Check the hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Password - Try Again!")
        else:
            flash("That User Doesn't Exist! Try Again...")
    return render_template('login.html', form=form)


@application.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

#Portfolio
@application.route("/portfolio")
@login_required
def portfolio():
    return redirect(url_for("dashboard"))


#Dashboard Route
@application.route("/dashboard")
@login_required
def dashboard():
    card_list = card.query.all()
    current_user_cards = card.query.filter_by(name_id = current_user.id)
    current_user_card_count = card.query.filter_by(name_id = current_user.id).count()
    set_list = allprintresults['data'].keys()
    #setcode=[]
    #for k, v in allprintresults['data'].items():
        #for k1,v1 in v.items():
            #if k1 == "name":
                #setcode.insert(0,v1)
    if current_user_card_count == 0:
        maxid = ""
        totalbuyprice = "0"
        totalretailprice = "0"
        maxprice = "0"
        countofcards = 0
        cardDates=''
        cardvalue=''
        unique_set = ""
    else:
        maxid= current_user_cards[-1]

        pricelistbuy=[]
        for prices in current_user_cards:
            i = float(prices.CKbuylistfoil)
            pricelistbuy.insert(0,i)
        totalbuyprice = round(sum(pricelistbuy),2)

        pricelistretail=[]
        for prices in current_user_cards:
            i = float(prices.CKretailfoil)
            pricelistretail.insert(0,i)
        totalretailprice = round(sum(pricelistretail),2)

        maxpricelist=[]  
        for prices in current_user_cards:
            i = float(prices.CKretailfoil)
            maxpricelist.insert(0,i)
            i = float(prices.CKbuylistfoil)
            maxpricelist.insert(0,i)
        maxprice = max(pricelistretail)

        countcards=[]
        for prices in current_user_cards:
            i = prices.cardName
            countcards.insert(0,i)
        countofcards=len(countcards)

        dates=[]
        priceDates={}
        cardvalue=[]
        cardDates=[]
        foilUUID = []
        nonFoilUUID = []
        for price in current_user_cards:
            if price.foil == "Foil":
                dates.append(allpriceresults['data'][price.UUID]['paper']['cardkingdom']['retail']['foil'])
            else:
                dates.append(allpriceresults['data'][price.UUID]['paper']['cardkingdom']['retail']['normal'])
    
        for k in dates:
            for k, v in k.items():
                if k in priceDates:
                    priceDates[k].append(v)
                else:
                    priceDates[k]=[v]
        for k, v in priceDates.items():
            cardDates.append(k)
            total = sum(v)
            cardvalue.append(total)

        unique_set={}
        for object in current_user_cards:
            if object.set in unique_set:
                unique_set[object.set] += 1
            else:
                unique_set[object.set] = 1
    return render_template("dashboard.html", card_list=card_list, unique_set=unique_set, last_name=maxid, set_list=set_list, totalbuyprice=totalbuyprice, 
                                        totalretailprice = totalretailprice, maxprice=maxprice, countofcards=countofcards, cardvalue = cardvalue, cardDates = cardDates)


#Add Card Route
@application.route("/add", methods=["POST"])
def add():
    name_id = current_user.id
    number = request.form.get("number")
    if "f" in number:
        number1 = number.replace('f','')
        foil = "Foil"
    else:
        number1 = number
        foil = "Not Foil"
    set = request.form.get("set")
    count = 0
    for i in allprintresults['data'][set]['cards']:
        if number1 == allprintresults['data'][set]['cards'][count]['number']:
            card_name = allprintresults['data'][set]['cards'][count]['name']
            card_uuid = allprintresults['data'][set]['cards'][count]['uuid']
            card_rarity= allprintresults['data'][set]['cards'][count]['rarity']
            if foil == "Foil":
                try: 
                    CKfoil_buylistprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['buylist']['foil']
                    ckbuylistkey = list(CKfoil_buylistprice.keys())[-1]
                    ckbuylistprice = CKfoil_buylistprice[ckbuylistkey]
                except:
                    ckbuylistprice = "0"
                try:
                    CKfoil_retailprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['retail']['foil']
                    ckretailkey = list(CKfoil_retailprice.keys())[-1]
                    ckretailprice = CKfoil_retailprice[ckretailkey]
                except:
                    ckretailprice = "0"
                break
            elif foil=="Not Foil":
                try:
                    CKfoil_buylistprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['buylist']['normal']
                    ckbuylistkey = list(CKfoil_buylistprice.keys())[-1]
                    ckbuylistprice = CKfoil_buylistprice[ckbuylistkey]
                except:
                    ckbuylistprice = "0"
                try:    
                    CKfoil_retailprice = allpriceresults['data'][card_uuid]['paper']['cardkingdom']['retail']['normal']
                    ckretailkey = list(CKfoil_retailprice.keys())[-1]
                    ckretailprice = CKfoil_retailprice[ckretailkey]
                except:
                    ckretailprice = "0"
                break
            else:
                ckbuylistprice= "0"
                ckretailprice = "0"      
            break
        else:
            count=count+1
        
    new_card = card(number=number1, name_id = name_id, 
                    set=set, foil=foil, UUID = card_uuid, cardName=card_name, 
                    cardRarity = card_rarity, CKbuylistfoil=ckbuylistprice, CKretailfoil=ckretailprice)
    db.session.add(new_card)
    db.session.commit()
    return redirect(url_for("dashboard"))

#Delete Card Route
@application.route("/delete/<int:card_id>")
def delete(card_id):
    carddel = card.query.filter_by(id=card_id).first()
    db.session.delete(carddel)
    db.session.commit()
    return redirect(url_for("dashboard"))


#404 Route
@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#500 Route
@application.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

