*Εχω βαλει και με τον φακελο προελευσης καθως στο vsc το χρειαζεται
 για να τρεξει σε σχεση μκε το pycharm

1)Για ενεργοποιηση του virtualenv:
.\virtualenv-ThKaralis\Scripts\Activate.ps1
.\Sw_finder\virtualenv-ThKaralis\Scripts\Activate.ps1

2)Για την αναζητηση :
python .\main.py search Darth
python .\Sw_finder\main.py search luke


3)Για πιο εξειδικευμενη αναζητηση (Πλανητης,πληθυσμος,αναλογια χρονου):
python .\main.py search Darth --world
python .\Sw_finder\main.py search Darth --world

4)Για να τεσταρουμε και τη λανθασμενη αναζητηση :
python .\Sw_finder\main.py search Thodoris  (Δυστηχως οχι)
python .\main.py search Thodoris

5)Για καθαρισμο του cache:
python .\Sw_finder\main.py cache --clean
python .\main.py cache --clean


6)Για να δουμε τις αναζητησεις απο το cache αρχειο μας :
python .\Sw_finder\main.py cache --show
python .\main.py cache --show