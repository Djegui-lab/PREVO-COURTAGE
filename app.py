from dotenv import load_dotenv
import streamlit as st
load_dotenv() 
import os 
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
load_dotenv() 

# Ajouter du CSS personnalisé pour définir les couleurs de fond
st.markdown(
    """
    <style>
        div.stApp {
            background-color: #FF69B4;  /* Couleur de fond globale */
        }
        
        .stTextInput {
            background-color: #808080;  /* Couleur de fond du champ de saisie (rose) */
        }
    </style>
    """,
    unsafe_allow_html=True
)


def envoyer_email(nom, prenom, email, piece_jointe=None):
    smtp_server = os.environ.get("SMTP_SERVER")
    port = int(os.environ.get("SMTP_PORT", 465))  # 465 est le port sécurisé SSL par défaut
    adresse_expediteur = os.environ.get("ADRESSE_EXPEDITEUR")  # Remplacez par votre adresse e-mail Gmail
    mot_de_passe = os.environ.get("MOT_DE_PASSE")  # Remplacez par votre mot de passe Gmail

    sujet = f"Votre demande de devis pour l'assurance auto ! {nom}"
    corps = f"""<span style="color: black;">
Nous attirons votre attention sur la validité de ce devis.<br>
<br>
Il est important de noter que ce tarif ne prend pas en considération d'éventuelles remises qui pourraient être appliquées.<br>
<br>
Nous sommes reconnaissants de l'opportunité de vous fournir cette offre, et nous restons à votre entière disposition pour toute clarification ou information supplémentaire que vous pourriez nécessiter concernant ce devis.<br>
<br>
Nous espérons que notre proposition correspondra à vos attentes.<br>
<br>
 Dans l'attente de votre retour, veuillez agréer, l'expression de nos salutations distinguées.<br>
 <br>
 <br>

 Cordialement,</span><br>
 <br>
 <br>  
    <div align="left">
    <table style="border:none;border-collapse:collapse;">
        <tbody>
            <tr>
                <td rowspan="6" style="border-right:solid #ffffff 2.25pt;border-bottom:solid #000000 1pt;">
                    <p><strong><span style="font-size:13pt;"><span style="border:none;"><img src="https://lh7-us.googleusercontent.com/2vko0U6hVs7QEedSkslTBsZMlnNMmtzgcqttsOqGkCLqWSV9bYjGVS0D96kCa0y3i7_roF1k_PCLd7_8hmB2i6wTJagJDcrjGxOy4ws_9rI4seXxAuagietzKyaUx81sONKNwgdF4qACA9MC2dZ_DgM" width="246" height="246"></span></span></strong></p>
                </td>
                <td style="border-left:solid #ffffff 2.25pt;border-bottom:solid #000000 1pt;">
                    <p><strong><span style="font-size:15pt;">&nbsp;DJEGUI WAGUE</span></strong></p>
                </td>
            </tr>
            <tr>
                <td style="border-left:solid #ffffff 2.25pt;border-top:solid #000000 1pt;border-bottom:solid #000000 1pt;">
                    <p><span style="color:#666666;font-size:12pt;">&nbsp;Responsable IARD-assurances-AUTO</span></p>
                </td>
            </tr>
            <tr>
                <td style="border-left:solid #ffffff 2.25pt;border-top:solid #000000 1pt;border-bottom:solid #000000 1pt;">
                    <p><strong><span style="font-size:11pt;">&nbsp;Votre&nbsp;&nbsp;Devis-</span></strong><a href="https://insurance-cwkdswptfjufg9aaenebsp.streamlit.app/"><strong><u><span style="color:#1155cc;font-size:11pt;">assurance-auto.com</span></u></strong></a></p>
                </td>
            </tr>
            <tr>
                <td style="border-left:solid #ffffff 2.25pt;border-top:solid #000000 1pt;"><br></td>
            </tr>
            <tr>
                <td style="border-left:solid #ffffff 2.25pt;"><br></td>
            </tr>
            <tr>
                <td style="border-left:solid #f3f3f3 2.25pt;">
                    <p><span style="font-size:11pt;">&nbsp;&nbsp;</span><span style="font-size:11pt;"><span style="border:none;"><img src="https://lh7-us.googleusercontent.com/OVDAIYrbrboOggfCiI0GkssYnC9fnVzT65HyIf3mOhBjknURfJAPHM1TK4IhtxNA35k7VI_eMzMPfoXtUwsdBH_m62fqbwe5JO5DOoX1Uz5GES2x0KPePzVCdzLLaJzhP3JG7TaVFLPbwE51JetS4jk" width="32" height="32"></span></span><span style="font-size:11pt;">&nbsp;</span><span style="font-size:11pt;"><span style="border:none;"><img src="https://lh7-us.googleusercontent.com/g6QATbg0CQFr5aC3ipVsWpkmt14reIaBRGNm9Pv0PFhCPL5AVxenKKS-pbjezlTeFf6sz-Rrx-YbhiwTBzjQiL11f3WQyzToo5XsNqTe4g8rnD8BTGrGiNbQAXpeRGmoQg9y6vQUnz4CVuGwS2OLKxI" width="32" height="32"></span></span><a href="https://wa.me/message/FGBNI52KKKQCG1"><u><span style="color:#1155cc;font-size:11pt;"><span style="border:none;"><img src="https://lh7-us.googleusercontent.com/pgCWst6sFNLx1G08dFdTsjq99wpUDPpNXKsVa0mlw57aIJmySaW1Yo5BxpJSYlV_Z44tasT8E6kqtGXP-3okdSIsHMfh5oWPzxBcO1onV9FnOUiotPFNAvvdl0RwbR-5pUwToj5AEPXM36lq_I0uT0o" width="32" height="32"></span></span></u></a></p>
                </td>
            </tr>
        </tbody>
    </table>
    </span>"""

    # Créer un objet MIMEMultipart
    message = MIMEMultipart()
    message["From"] = adresse_expediteur
    message["To"] = email
    message["Subject"] = sujet

    # Ajouter le corps du message
    message.attach(MIMEText(corps, "html"))  # Utilisation du type "html" pour le corps du message

    # Ajouter la pièce jointe PDF si elle est fournie
    if piece_jointe:
        nom_fichier = piece_jointe.name
        piece_jointe_mime = MIMEApplication(piece_jointe.read(), _subtype="pdf")
        piece_jointe_mime.add_header("Content-Disposition", f"attachment; filename={nom_fichier}")
        message.attach(piece_jointe_mime)

    # Spécifier l'encodage UTF-8
    message = message.as_string().encode("utf-8")

    contexte_ssl = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=contexte_ssl) as server:
            server.login(adresse_expediteur, mot_de_passe)
            server.sendmail(adresse_expediteur, email, message)
        statut_envoi = "Envoyé avec succès"
    except smtplib.SMTPConnectError:
        # Ajouter une connexion explicite si la connexion n'est pas déjà établie
        with smtplib.SMTP_SSL(smtp_server, port, context=contexte_ssl) as server:
            server.connect(smtp_server, port)
            server.login(adresse_expediteur, mot_de_passe)
            server.sendmail(adresse_expediteur, email, message)
        statut_envoi = "Envoyé avec succès après connexion"

    except Exception as e:
        statut_envoi = f"Erreur d'envoi : {str(e)}"

    # Retourner les détails de l'envoi
    return {
        "Nom": nom,
        "Prénom": prenom,
        "E-mail": email,
        "Pièce jointe": nom_fichier if piece_jointe else None,
        "Statut": statut_envoi,
        "Date d'envoi": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# Fonction pour afficher l'historique
def afficher_historique(enregistrements):
    st.title("Historique des Enregistrements")
    if not enregistrements:
        st.info("Aucun enregistrement trouvé.")
    else:
        st.dataframe(enregistrements)

# Fonction principale
def main():
    st.title("Application web d'automatisation ")
    
    # Utiliser le concept de "state" pour gérer les différentes pages
    page = st.sidebar.selectbox("Navigation", ["Accueil", "Envoyer E-mail", "Historique"])

    # "state" pour stocker les enregistrements
    if "enregistrements" not in st.session_state:
        st.session_state.enregistrements = []

    if page == "Accueil":
        st.write("Bienvenue sur la page d'accueil.")

    elif page == "Envoyer E-mail":
        with st.form("formulaire_email"):
            st.write("Veuillez saisir vos informations :")
            nom = st.text_input("Nom:")
            prenom = st.text_input("Prénom:")
            email = st.text_input("E-mail:")
            fichier_pdf = st.file_uploader("Choisir un fichier PDF", type=["pdf"])

            submitted = st.form_submit_button("Envoyer l'e-mail de bienvenue")

            if submitted:
                if nom and prenom and email and fichier_pdf:
                    # Appel de la fonction envoyer_email avec les valeurs des champs du formulaire
                    details_envoi = envoyer_email(nom, prenom, email, piece_jointe=fichier_pdf)
                    st.success(f"E-mail de bienvenue envoyé à {email}")

                    # Ajouter les détails de l'envoi à l'historique
                    st.session_state.enregistrements.append(details_envoi)

                else:
                    st.warning("Veuillez remplir tous les champs et choisir un fichier PDF.")

    elif page == "Historique":
        afficher_historique(st.session_state.enregistrements)

if __name__ == "__main__":
    main()