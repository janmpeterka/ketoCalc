"""TODO: delete!

Revision ID: efe33eafa19a
Revises: 2a3e83689c3d
Create Date: 2020-04-01 21:49:48.672134

"""
# from alembic import op
# import sqlalchemy as sa
# from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "efe33eafa19a"
down_revision = "2a3e83689c3d"
branch_labels = None
depends_on = None


def upgrade():
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.execute(
    #     """
    #     INSERT INTO ingredients
    #         (name,calorie,fat,sugar,protein,is_shared,is_approved,source,author)
    #     VALUES ('Ananas',212,0.2,12.6,0.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Angrešt',186,0.2,11.3,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Artyčok',261,0.6,16.7,3.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Avokádo',697,16.5,6.3,1.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Banány',415,0.3,23.9,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Borůvky',213,0.6,12.3,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Brambory rané',303,0.2,16.1,2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Brambory sladké (batáty, jamy)',277,0.2,16.1,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Brambory zimní',330,0.3,17.2,2.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Brokolice',153,0.3,6.1,4.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Broskve',205,0.2,11.5,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Brusinky',204,0.7,11.7,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Celer bulvový',117,0.3,7.1,1.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Celer řapíkatý',69,0.2,5.3,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cibule',164,0.3,8.7,1.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cibule červená',191,0.2,10.4,1.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cibule šalotka',187,0.1,10.3,1.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Citróny',149,0.4,8.4,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cizrna',1285,5.8,60.7,20,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cuketa',57,0.1,2.8,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cukr řepný, bílý',1700,0,99.9,0,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Cukr třtinový',1680,0,98.9,0,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Česnek',636,0.4,31.7,6.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Česnek medvědí',155,1,5.1,3.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Čočka',1372,0.7,63.5,23.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Čočka červená',1317,1.3,61.8,24.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Čočka, černá',1271,1.5,59.9,26.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Dýně, Hokkaidó',154,0.6,7.7,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Dýně, máslová',161,0.2,8.4,1.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Fazole bílé, sušené',1411,0.8,69.7,21.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Fazole černé',1129,1.4,61.3,20.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Fazole červené',1151,1.7,65,18.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Fíky',323,0.3,19.1,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Goji, plody kustovnice čínské, sušené',1454,3.3,71.9,12.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Grapefruit',170,0.2,9.8,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Hlíva ústřičná',85,0.1,5.4,1.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Hrách',1429,1.8,67.3,19.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Hrášek',325,0.4,15.3,6.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Hrušky',238,0.3,14.6,0.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Hřib smrkový',170,0.6,5.2,5.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Chřest bílý',80,0.1,3.7,1.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Jablka',219,0.4,12.8,0.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Jáhly',1522,2.5,72.8,11.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Jahody zahradní',158,0.4,8.6,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra hovězí',548,4,4.3,19.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra husí',493,2.7,1.26,21.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra kachní',510,3.3,2.2,20.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra králičí',466,3.4,0,20,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra krůtí',478,3.1,0.57,20.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra kuřecí',509,5,2.4,16.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra telecí',634,6.1,3,21.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Játra vepřová',496,2.7,3.9,19.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kapusta hlávková',161,0.7,7.1,3.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kapusta kadeřavá',134,0.5,3.38,3.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kapusta růžičková',204,0.5,8.6,4.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kedlubna',114,0.1,5.7,2.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kiwi',244,0.8,13.1,1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kokos mletý',2830,65.7,23.8,6.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Kopr',143,0.3,7.1,2.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření nové',1430,7,74.8,5.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, bazalka, sušená',988,2.9,54.7,18.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, fenykl',1289,16.1,51.3,16.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, hřebíček',1510,17.2,63.6,5.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, kardamom',1138,2,74.5,8.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, kmín',1360,13.7,57.5,12.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, kmín římský',1564,22.9,43.8,19.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, kurkuma',1296,1.7,74.2,9.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, majoránka, sušená',1090,5.6,58.9,14.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, muškátový květ',1700,26.4,54.6,5.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, muškátový oříšek',2020,36.3,43.9,7.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, paprika, sladká, mletá',1344,13.8,56.9,15,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, pepř, černý',1400,8.6,62.7,11.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, tymián, sušený',1180,7.4,64,9.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Koření, zázvor, mletý',1400,4.7,71.9,7.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Křen',339,0.5,18.8,3.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Květák',110,0.2,4.9,2.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Lilek',77,0,5,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Limetka',148,0,9.9,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Mák',2043,38.9,25.7,21.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Maliny',209,0.6,13.2,1.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Mandarinky',176,0.2,10,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Mandle',2450,47.9,20.2,28.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Mango',292,0.5,16.4,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Marakuja (mučenka jedlá)',389,3.4,18.4,2.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Meruňky',223,0.1,13.8,0.5,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Mrkev',151,0.2,9,1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Nashi',183,0.1,11.3,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Nektarinky',200,0.3,11,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Okurky',48,0.1,2.2,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy kešu',2470,45.6,29.4,17.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy lískové',2724,61.4,21.2,14.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy lískové loupané',2869,66.5,14.3,14.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy para',2837,65.2,12.3,16.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy pekan',2933,69.6,13.7,12.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy píniové',2419,44.5,31.3,17.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy pistáciové',2500,50,23.9,20.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ořechy vlašské',2740,61.2,17.4,16.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ostružiny',225,1,12.4,1.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Paprika zeleninová, bílá',72,0.2,4.4,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Paprika zeleninová, červená',124,0.4,6,1.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Paprika zeleninová, zelená',87,0.3,4.6,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Paprika zeleninová, žlutá',98,0.3,4.7,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Patizon',66,0.1,4.2,0.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pažitka',131,0.7,5.1,2.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Petržel, kořen',222,0.5,11.5,2.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Petržel, nať',226,0.42,10.3,4.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pohanka, loupaná, lámanka',1462,2.1,72.7,11.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pohanka, neloupaná',1307,2.3,73.5,10.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Polníček',79,0.4,2.8,2.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pomelo',170,0.1,9.2,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pomeranče',209,0.2,12,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Pórek',136,0.3,6.6,2.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Quinoa, semena',1470,6.1,68.4,12.4,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Rebarbora',63,0,4.4,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Rukola',74,0.3,2.1,2.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Rybíz bílý',218,1.1,12.8,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Rybíz černý',258,0.3,16.4,1.2,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Rybíz červený',205,0.2,13.4,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ředkev bílá',83,0.1,4.2,1.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Ředkvička',45,0,2.6,0.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Řepa červená',166,0.2,8.9,1.3,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Skořice mletá',973,1.9,80.8,3.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Sůl jedlá',0,0,0,0,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Špenát',106,0.4,3.9,2.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Švestky',250,0.2,14.9,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Třešně',274,0.4,15.4,0.9,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Tuřín (brukev řepka)',63,0.1,3.6,0.8,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Víno - hrozny',302,0.4,17.3,0.7,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Višně',234,0.5,12.6,1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Zázvor',115,0.2,6.8,1.1,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Zelí hlávkové, bílé',123,0.2,6.6,1.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Zelí hlávkové, červené',122,0.2,6.5,1.6,1,0,'nutridatabaze','admin_nutridatabaze'),
    #     ('Žampiony',98,0.3,3.1,2.9,1,0,'nutridatabaze','admin_nutridatabaze')
    #     """
    # )
    # # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
