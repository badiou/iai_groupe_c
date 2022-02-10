
import os
from flask import Flask, abort, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

################################################################
#
#           Configuration de la chaine de connexion
#
################################################################
motdepasse=quote_plus(os.getenv('db_password'))
host=os.getenv('hostname')
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:{}@{}:5432/appg3".format(motdepasse,host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


################################################################
#
#             Classe Etudiant
#
################################################################
class Etudiant(db.Model):
    __tablename__='etudiants'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(50),nullable=False)
    prenom=db.Column(db.String(100),nullable=False)
    adresse=db.Column(db.String(100),nullable=True)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit() 
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id':self.id,
            'nom':self.nom,
            'adresse':self.adresse,
            'prenom':self.prenom
        }
db.create_all()
'''
Les endpoints de l'API
GET /etudiants (liste de tous les étudiants)
GET /etudiants/id (selectionner un étudiant en particulier)
POST /etudiants (Créer un nouvel étudiant)
PATCH /etudiants/id (Modifier un étudiant)
DELETE /etudiants/id (Supprimer un étudiant)
'''

################################################################
#
#             Endpoint liste de tous les étudiants
#
################################################################
@app.route('/etudiants',methods=['GET'])
def liste_etudiants():
    # requete avec SQLAlchemy pour récupérer la liste de tous les étudiants
    etudiants=Etudiant.query.all()
    etudiants_formatted=[et.format() for et in etudiants]
    return jsonify({
        'success':True,
        'total_etudiants':Etudiant.query.count(),
        'etudiants':etudiants_formatted
    })
    
################################################################
#
#             Endpoint selectionner un étudiant
#
################################################################
@app.route('/etudiants/<int:id>')
def selectionner_un_etudiant(id):
    #requete pour selectionner un etudiant avec SQLAlchemy
    etudiant=Etudiant.query.get(id)
    # verifions si cet etudiant existe dans la base
    if etudiant is None:
        abort(404) 
        #404 est le status code pour dire que la ressoruce n'existe pas
    else:
        return jsonify({
            'success':True,
            'selected_id':id,
            'etudiant':etudiant.format()
        })
################################################################
#
#             Endpoint créer un nouvel etudiant
#
################################################################
@app.route('/etudiants',methods=['POST'])
def ajouter_etudiant():
    body=request.get_json() #recupérer les données json
    new_nom=body.get('nom',None)
    new_prenom=body.get('prenom',None)
    new_adresse=body.get('adresse',None)
    etudiant=Etudiant(nom=new_nom,prenom=new_prenom,adresse=new_adresse)
    etudiant.insert()
    return jsonify({
        'success':True,
        'totat_etudiants':Etudiant.query.count(),
        'etudiants':[ et.format() for et in Etudiant.query.all()]
    })

################################################################
#
#             Endpoint Supprimer un etudiant
#
################################################################
@app.route('/etudiants/<int:id>',methods=['DELETE'])
def delete_etudiant(id):
    etudiant=Etudiant.query.get(id)
    if etudiant is None:
        abort(404)
    else:
        #supprimer la personne
        etudiant.delete()
        return jsonify({
            'success':True,
            'id':id,
            'etudiant':etudiant.format(),
            'total_etudiants':Etudiant.query.count()
        })
################################################################
#
#             Endpoint Modifier un etudiant
#
################################################################   
@app.route('/etudiants/<int:id>',methods=['PATCH'])
def modifier_etudiant(id):
    
    etudiant=Etudiant.query.get(id)
    if etudiant is None:
        abort(404)
    else:
        body=request.get_json()
        etudiant.nom=body.get('nom')
        etudiant.prenom=body.get('prenom')
        etudiant.adresse=body.get('adresse')
        etudiant.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'etudiant':etudiant.format()
        })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
    
@app.errorhandler(500)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 500,
        "message": "Internal server Error"
        }), 500

@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Mauvaise requete"
        }), 400