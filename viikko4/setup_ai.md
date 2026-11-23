Pyysin agenttia siirtämään testien yhteiset alustukset setUp-metodiin niin, että testien toiminnallisuus ei muutu.

Mielestäni agentti poisti toisteisuuden järkevästi. Mockit, varaston saldo- ja hae_tuote-toteutukset sekä kaupan luonti ovat nyt setUp-metodissa, ja jokaisessa testissä on vain ostostapahtuman vaiheet ja tarkistus. Testitiedosto lyheni noin 190 rivistä noin 80 riviin, ja testeistä näkee nopeasti mitä niissä ostetaan ja mikä summa odotetaan. Kutsu aloita_asiointi jäi testeihin, koska se on osa testattavaa tapahtumaa.

Agentti ei heikentänyt tarkistuksia. Kaikki assert_called_with-tarkistukset ja odotetut summat ovat samat, ja ensimmäinen testi käyttää edelleen assert_called-metodia kuten tehtävänannossa. Testeihin tuli yksi muutos: aiemmin loppunut tuote oli tuote 2, mutta yhteisessä setUpissa tuotetta 2 tarvitaan varastossa olevana, joten agentti lisäsi loppuneeksi tuotteeksi tuotteen 3. Testit menevät läpi, ja tarkistin, että loppuneen tuotteen testi kaatuu edelleen, jos kaupasta poistetaan saldon tarkistus.

Minun ei tarvinnut korjata agentin muutoksia.
