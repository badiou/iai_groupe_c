from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
#import sys

app=Flask(__name__)
motdepasse=quote_plus('B@diou2015')
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@localhost:5432/appg3".format(motdepasse)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Etudiant(db.Model):
    __tablename__='etudiants'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(50),nullable=False)
    prenom=db.Column(db.String(100),nullable=False)
    adresse=db.Column(db.String(100),nullable=True)

db.create_all()

#Liste des tous les étudiants dans la base de données
@app.route('/',methods=['GET'])
def get_all_students():
    etudiants=Etudiant.query.all()
    return render_template('index.html',data=etudiants)

@app.route('/create',methods=['GET'])
def afficher_form_create():
    return render_template('create.html')

@app.route('/add',methods=['GET','POST'])
def ajouter_etudiant():
    try:
        if request.method=='GET':
            return render_template('create.html')
        
        elif  request.method=='POST':  
            new_nom=request.form.get('nom','')
            new_adresse=request.form.get('adresse','')
            new_prenom=request.form.get('prenom','')
            etudiant=Etudiant(nom=new_nom,prenom=new_prenom,adresse=new_adresse)
            db.session.add(etudiant)
            db.session.commit()
            return redirect(url_for('get_all_students'))
    except:
        db.session.rollback()
        #print(sys.exc_info())
    finally:
        db.session.close()
    
    


    
