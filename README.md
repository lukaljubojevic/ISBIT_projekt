# SEMINARSKI RAD

INFORMACIJSKA SIGURNOST I BLOCKCHAIN TEHNOLOGIJE

Pametni ugovor i testiranje na Ganache testnoj mreži

Izradili:
 Luka Ljubojević i Marko Gajić

Sadržaj

1. Uvod
2. Opis pametnog ugovora
3. Konstruktor
4. Mapping
5. Funkcije
6. Testiranje na Ganache testnoj mreži
7. Bonus
8. Zaključak

## Uvod

Pametni ugovori su računalni programi koji se izvršavaju na blockchain mreži i omogućavaju automatizirano provođenje ugovora i transakcija. Solidity je jezik za pisanje pametnih ugovora na Ethereum blockchainu. U ovom seminarskom radu opisat ćemo jedan pametni ugovor koji je definiran Solidity kodom. Radi se o ugovoru nazvanom SimpleToken.

## Opis pametnog ugovora

SimpleToken pametni ugovor sastoji se od nekoliko dijelova. Prvi dio su detalji tokena, uključujući ime, simbol i ukupnu količinu tokena koji su izdani. Sljedeći dio je mapiranje adrese na stanje tokena. To znači da se svakoj adresi na Ethereum mreži dodjeljuje određena količina tokena koju ta adresa posjeduje. Zatim imamo događaj transfera koji se emitira kad se tokeni prenose s jedne adrese na drugu. Ovaj događaj omogućava praćenje transfera tokena i lako se može integrirati s drugim aplikacijama. Sljedeći dio je adresar vlasnika ugovora koji se koristi za provjeru identiteta vlasnika i omogućava pristup funkcijama koje samo vlasnik ugovora može pozvati. Konačno, imamo funkcije za prebacivanje tokena, provjeru stanja tokena, povećavanje ukupne količine tokena i smanjivanje ukupne količine tokena.

## Konstruktor

Kada se ugovor implementira, konstruktor se poziva samo jednom i služi za inicijalizaciju ugovora. Konstruktor za SimpleToken pametni ugovor prima tri parametra: ime tokena, simbol i ukupnu količinu tokena koju treba izdati. Nakon inicijalizacije, ova tri parametra se pohranjuju u varijable ugovora name, symbol i totalSupply. Također se dodjeljuje vlasnik ugovora, što je osoba koja je stvorila ugovor i ima kontrolu nad njim. Ovdje se koristi msg.sender koji je u ovom slučaju adresa osobe koja stvara ugovor. Na kraju, vlasniku se dodjeljuje ukupna količina tokena koja je izdana.

## Mapping

U ovom ugovoru, mapping je korišten za mapiranje adresa korisnika na količinu tokena koju posjeduju. Ovaj mapping se definira kao mapping(address => uint256) public balances;.

address je ključ mape, koji je adresa korisnika, dok je uint256 vrijednost mape, koja predstavlja količinu tokena koju korisnik posjeduje. Modifikator public omogućuje čitanje i upisivanje u mapu izvan samog ugovora, tako da bilo koji drugi ugovor ili aplikacija može pristupiti vrijednosti mape za određenog korisnika.

## Funkcije

Ovaj ugovor sadrži nekoliko funkcija koje omogućuju upravljanje tokenima:

* transfer(address _to, uint256_value) - Ova funkcija se koristi za prijenos tokena od jedne adrese do druge. msg.sender adresa mora imati dovoljno tokena za prijenos kako bi transakcija bila uspješna. Ako msg.sender adresa nema dovoljno tokena, transakcija se neće izvršiti. Ako se transakcija uspješno izvrši, poziva se događaj Transfer, koji emitira informacije o prijenosu tokena.

* balanceOf(address _address) - Ova funkcija se koristi za dohvaćanje trenutne količine tokena koju određena adresa korisnika posjeduje.

* mint(uint256 _value) - Ova funkcija se koristi za povećanje ukupne količine tokena ugovora. Ova funkcija je dostupna samo vlasniku ugovora.

* burn(uint256 _value) - Ova funkcija se koristi za smanjenje ukupne količine tokena ugovora. Ova funkcija je dostupna samo vlasniku ugovora i samo ako vlasnik ugovora ima dovoljno tokena.

## Testiranje na Ganache testnoj mreži

Ovaj programski kod omogućuje korisniku da se poveže na Ethereum mrežu putem Web3 biblioteke i Ganache-a, a zatim izvrši neke osnovne operacije s pametnim ugovorom.
Najprije se uvoze potrebne biblioteke i definiraju varijable koje će biti korištene za povezivanje s Ganache-om i razmjenu podataka s Ethereum mrežom. Ovaj kod koristi lokalni Ganache poslužitelj koji se pokreće na adresi 0.0.0.0:8545.

Također se definira identifikacijski broj mreže (chain_id), adresa računa vlasnika (my_address) i njezin privatni ključ (private_key).
Sljedeći korak je čitanje sadržaja SimpleToken.sol datoteke i njegova kompilacija u bytecode i ABI pomoću solcx paketa. ABI (Application Binary Interface) je definicija funkcija i događaja koje pametni ugovor nudi korisnicima. Bytecode je strojni jezik na kojem pametni ugovor radi.
Nakon što je pametni ugovor uspješno kompajlan, koristi se bytecode i ABI za stvaranje Python sučelja za pametni ugovor. Zatim se koristi nonce za stvaranje transakcije koja će se koristiti za raspoređivanje pametnog ugovora. Transakcija se stvara pomoću SimpleToken.constructor() metode i njezina hash vrijednost se šalje Ethereum mreži.
Sljedeći korak je čekanje dok se transakcija ne potvrdi i dobivanje adrese pametnog ugovora. Zatim se stvara instanca pametnog ugovora pomoću te adrese i koristi se za izvršavanje metoda ugovora.
U ovom slučaju, prvo se dohvaća saldo vlasnika pametnog ugovora pozivanjem balanceOf() metode. Zatim se prenose tokeni drugom računu pozivanjem transfer() metode, a transakcija se potpisuje i šalje Ethereum mreži. Nakon što se transakcija uspješno potvrdi, dohvaćaju se ažurirani saldovi oba računa i ispisuju se na ekranu.
Ovaj kod služi kao primjer kako se može stvoriti i rasporediti pametni ugovor na Ethereum mreži pomoću Python sučelja i kako se može koristiti Web3 biblioteka za interakciju s ugovorom.

## Bonus

Ovaj programski kod koristi biblioteku Web3 za povezivanje s Ethereum mrežom i interakciju s pametnim ugovorima na Ethereumu. Prvo se uvozi biblioteka Web3. Zatim se stvara novi objekt web3 koji se povezuje s Ethereum mrežom. U ovom slučaju, programski kod koristi lokalnu Ethereum mrežu, koja se nalazi na adresi localhost:8545.

Nakon toga se postavlja adresa implementiranog pametnog ugovora te ABI (Application Binary Interface) pametnog ugovora. ABI sadrži informacije o funkcijama koje su dostupne na pametnom ugovoru. Ovdje se definiraju tri funkcije: constructor, transfer i balances. Sljedeći korak je stvaranje instance objekta ugovora i nakon toga se poziva funkcija balanceOf, koja se nalazi u pametnom ugovoru, kako bi se dobio saldo adrese koja je predana kao argument.

Ova funkcija se poziva asinkrono i vraća vrijednost salda preko callback funkcije koja ispisuje saldo u konzoli.
Naposljetku, programski kod šalje novu transakciju koja se poziva funkcijom transfer, koja se nalazi u pametnom ugovoru. Ova funkcija se također poziva asinkrono i šalje novu transakciju s adresom pošiljatelja, adresom primatelja i iznosom koji se šalje. Callback funkcija ispisuje hash transakcije u konzoli.

## Zaključak

Zaključno ovaj projekt kreiran je u Solidityju. Solidity je jezik programiranja koji se koristi za pisanje pametnih ugovora na Ethereum blockchainu. Kreirani pametni ugovor je  decentralizirani program koji se izvršava automatski kada su ispunjeni zadani uvjeti. Ganache je testna mreža na kojoj je testiran prema zadanim pravilima, a ona se općenito koristi za razvoj i testiranje pametnih ugovora, omogućujući programerima da simuliraju stvarni Ethereum blockchain, bez trošenja stvarnih sredstava. Korištenje testne mreže poput Ganachea omogućuje programerima da isprobaju svoj kod prije nego ga postave na stvarni Ethereum blockchain.
